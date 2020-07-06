from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    date_of_birth = models.DateField('Date of birth', blank=False)

    gender = [ ('m', 'male'), ('f', 'female'), ('o', 'other') ]
    Gender = models.CharField('Gender', max_length=3, choices=gender, blank=False)
    
    
    # dating traits

    gender2 = [ ('m', 'male'), ('f', 'female'), ('bi', 'both') ]
    Preference = models.CharField('Attracted to?', max_length=3, choices=gender2, blank=False)

    # in_or_out = [ ('in', 'indoors'), ('out', 'outdoors') ]
    # Are_you_an_indoors_or_outdoors_person = models.CharField('Are you and indoors or outdoors person?', max_length=3, choices=in_or_out, blank=False)
    
    # takeouts_or_homecooked = [ ('ta', 'takeouts'), ('hm', 'homecooked meals') ]
    # Do_you_prefer_takeouts_or_homecooked_meals = models.CharField('Do you prefer homecooked meals or takeouts?', max_length=2, choices=takeouts_or_homecooked, blank=False)
    
    # religious_or_not = [ ('re', 'Yes'), ('nr', 'No') ]
    # Are_you_religious_or_not = models.CharField('Are you religious or not?', max_length=2, choices=religious_or_not, blank=False)

    # religion_if_religious = models.CharField('Your religion. (optional)', max_length=200, default=None, blank=True)

    # traditional_or_not = [ ('tr', 'traditional'), ('nt', 'not traditional') ]
    # Are_you_traditional_or_not = models.CharField('Are you a trad', max_length=2, choices=traditional_or_not, blank=False)

    # science_or_business = [ ('sc', 'science'), ('bu', 'business'), ('ot', 'other') ]
    # Do_you_prefer_science_or_business = models.CharField(max_length=2, choices=science_or_business, blank=False)
    
    # texting_or_meeting_in_person = [ ('te', 'texting'), ('mip', 'meeting in person') ]
    # Do_you_prefer_texting_or_meeting_in_person = models.CharField(max_length=3, choices=texting_or_meeting_in_person, blank=False)

    # cuddling_or_personal_space = [ ('cu', 'contact'), ('ps', 'personal space') ]
    # Do_you_prefer_a_contact_or_personal_space_type_of_relationship = models.CharField(max_length=2, choices=cuddling_or_personal_space, blank=False)
    
    # planning_or_living_in_the_moment = [ ('pl', 'planning'), ('lim', 'living in the moment') ]
    # Do_you_prefer_planning_or_living_in_the_moment = models.CharField(max_length=3, choices=planning_or_living_in_the_moment, blank=False)

    # politically_active_or_not = [ ('pa', 'politically active'), ('np', 'not politically active'), ('ot', 'other') ]
    # Are_you_politically_active_or_not = models.CharField(max_length=2, choices=science_or_business, blank=False)

    Rel_type = [('sr', 'A serious relationship.'), ('fr', 'Friend'), ('st', 'Someone to talk to.'), ('hk', 'A hook-up.')]
    The_type_of_relationship_you_are_looking_for = models.CharField('You are looking for a...', max_length=3, choices=Rel_type, blank=False)
    
    
    profile_picture = models.ImageField(upload_to='images/', blank=False)

    Bio = models.TextField('Bio (Express what makes you tick, this will be visible for others to view.)', blank=False)
    
    # longitude = models.FloatField(blank=True, null=True)
    # latitude = models.FloatField(blank=True, null=True)

    location = models.PointField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user.username

