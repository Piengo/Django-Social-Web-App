from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, ProfileForm
from .models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django import forms


longitude = 0.0
latitude = 0.0

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'users_list'

    
    def get(self, request):
        global longitude
        global latitude
        me = request.user.profile
        user_location = Point(longitude, latitude)
        me.location = user_location
        me.save()
        other_people = Profile.objects.annotate(distance=Distance('location',user_location)).order_by('distance')[0:6]
        first_person = other_people[0] 
        return render(request, self.template_name, {'other_people': other_people, 'me':me, 'first_person':first_person})


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = reverse_lazy('home:index')
    fields = [
                'profile_picture',
                'Bio',
                # 'city',
                # 'country',
                # 'Are_you_an_indoors_or_outdoors_person',
                # 'Do_you_prefer_takeouts_or_homecooked_meals',
                # 'Are_you_religious_or_not',
                # 'religion_if_religious',
                # 'Are_you_traditional_or_not',
                # 'Do_you_prefer_science_or_business',
                # 'Do_you_prefer_texting_or_meeting_in_person',
                # 'Do_you_prefer_a_contact_or_personal_space_type_of_relationship',
                # 'Do_you_prefer_planning_or_living_in_the_moment',
                # 'Are_you_politically_active_or_not',
                'The_type_of_relationship_you_are_looking_for',
                'Preference',
                ]
    template_name_suffix = '_update_form'


class UserFormView(View):
    user_form_class = UserForm
    profile_form_class = ProfileForm
    template_name = 'home/registration_form.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})
        

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        profile_form = self.profile_form_class(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            # cleaned data
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            
            user.set_password(password)
            

            profile = profile_form.save(commit=False)
            


            user.save()
            profile.user = user
            profile.save()
            

            # returns valid user data
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home:index')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class LocationView(View):
    
    def post(self, request):
        global latitude 
        latitude = float(request.POST.get('lat', False))
        global longitude 
        longitude = float(request.POST.get('long', False))
        
        if longitude and latitude:
            return HttpResponse(status=204)
        return HttpResponse(status=500)


class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request):
        return render(request, self.template_name)