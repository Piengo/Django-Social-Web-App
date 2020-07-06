from django.db import models
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
                'date_of_birth',
                'Gender',
                'Preference',
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
                'profile_picture',
                'Bio',
                )
        widgets = {
            'location': forms.HiddenInput(),
        }