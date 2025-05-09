# forms.py
from django import forms
from .models import Profile
from django.core.files.uploadedfile import UploadedFile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']

    def clean_profile_pic(self):
        profile_pic = self.cleaned_data.get('profile_pic')
        if profile_pic and isinstance(profile_pic, UploadedFile):
            # Validate file size (e.g., max 5MB)
            if profile_pic.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Profile picture size must be under 5MB.")
            # Validate file type (only JPEG/PNG allowed)
            if not profile_pic.content_type in ['image/jpeg', 'image/png']:
                raise forms.ValidationError(
                    "Only JPEG and PNG images are allowed.")
        return profile_pic
