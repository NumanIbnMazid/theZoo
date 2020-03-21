# from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from .models import Staff
from middlewares.middlewares import RequestMiddleware
from django.conf import settings
from django.template.defaultfilters import filesizeformat
import re
import os


# class CustomSignupForm(SignupForm):
#     def signup(self, request, user):
#         user.save()
#         user_staff, created = self.get_or_create(user=user)
#         user.user_staff.save()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name']


class UserStaffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # magic
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # self.uf = UserForm(*args, **kwargs)
        # magic end

        super(UserStaffForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)

        self.fields['dob'].widget.attrs.update({
            'id': 'datetimepicker_DOB',
            'autocomplete': 'off'
        })
        self.fields['address'].widget.attrs.update({
            'id': 'address',
            'maxlength': 200,
            'placeholder': 'Enter your address...'
        })
        self.fields['phone'].widget.attrs.update({
            'id': 'phone',
            'maxlength': 20,
            'placeholder': 'Enter your phone number...'
        })
        self.fields['posting'].widget.attrs.update({
            'id': 'posting',
            'maxlength': 100,
            'placeholder': 'Enter your posting...'
        })
        self.fields['insurance_cover'].widget.attrs.update({
            'id': 'insurance_cover',
            'maxlength': 100,
            'placeholder': 'Enter your insurance_cover...'
        })
        # Help Texts
        self.fields['first_name'].help_text = "Maximum length 15 and only these 'A-Za-z.,-' characters and spaces are allowed."
        self.fields['last_name'].help_text = "Maximum length 20 and only these 'A-Za-z.,-' characters and spaces are allowed."

    class Meta:
        model = Staff
        fields = ['image', 'insurance_cover', 'posting', 'phone', 'address', 'dob', 'gender']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image == None and not image == False:
            image_extension = os.path.splitext(image.name)[1]
            allowed_image_types = settings.ALLOWED_IMAGE_TYPES
            if not image_extension in allowed_image_types:
                raise forms.ValidationError("Only %s file formats are supported! Current file format is %s" % (
                    allowed_image_types, image_extension))
            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                raise forms.ValidationError("Please keep filesize under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_IMAGE_UPLOAD_SIZE), filesizeformat(image.size)))
        return image

    def save(self, *args, **kwargs):
        self.uf.save(*args, **kwargs)
        return super(UserStaffForm, self).save(*args, **kwargs)

    # def save(self, commit=True):
    #     user = super(UserStaffForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #         user.user_staff.save()
    #     return user
    


class BaseUserStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['role']


class BaseUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # magic
        self.uf = BaseUserStaffForm(*args, **kwargs)
        # magic end

        super(BaseUserForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        # self.initial.update(self.uf.initial)

        self.fields['first_name'] = forms.CharField(
            required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your first name...'})
        )
        self.fields['first_name'].widget.attrs.update({
            'id': 'profile_first_name',
            'maxlength': 15,
            'pattern': "^[A-Za-z.,\- ]{1,}$",
        })
        self.fields['last_name'] = forms.CharField(
            required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your last name...'})
        )
        self.fields['last_name'].widget.attrs.update({
            'id': 'profile_last_name',
            'maxlength': 20,
            'pattern': "^[A-Za-z.,\- ]{1,}$"
        })
        self.fields['email'] = forms.EmailField(
            required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your email...'})
        )
        self.fields['password'] = forms.CharField(
            required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password...'})
        )
        # Help Texts
        self.fields['first_name'].help_text = "Maximum length 15 and only these 'A-Za-z.,-' characters and spaces are allowed."
        self.fields['last_name'].help_text = "Maximum length 20 and only these 'A-Za-z.,-' characters and spaces are allowed."

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


    def save(self, commit=True):
        user = super(BaseUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AdminUserStaffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # magic
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)
        # self.uf = UserForm(*args, **kwargs)
        # magic end

        super(AdminUserStaffForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)

        self.fields['dob'].widget.attrs.update({
            'id': 'datetimepicker_DOB',
            'autocomplete': 'off'
        })
        self.fields['address'].widget.attrs.update({
            'id': 'address',
            'maxlength': 200,
            'placeholder': 'Enter your address...'
        })
        self.fields['phone'].widget.attrs.update({
            'id': 'phone',
            'maxlength': 20,
            'placeholder': 'Enter your phone number...'
        })
        self.fields['posting'].widget.attrs.update({
            'id': 'posting',
            'maxlength': 100,
            'placeholder': 'Enter your posting...'
        })
        self.fields['insurance_cover'].widget.attrs.update({
            'id': 'insurance_cover',
            'maxlength': 100,
            'placeholder': 'Enter your insurance_cover...'
        })
        # Help Texts
        self.fields['first_name'].help_text = "Maximum length 15 and only these 'A-Za-z.,-' characters and spaces are allowed."
        self.fields['last_name'].help_text = "Maximum length 20 and only these 'A-Za-z.,-' characters and spaces are allowed."

    class Meta:
        model = Staff
        fields = ['role', 'gender', 'dob', 'phone',
                  'address', 'image', 'insurance_cover', 'posting']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image == None and not image == False:
            image_extension = os.path.splitext(image.name)[1]
            allowed_image_types = settings.ALLOWED_IMAGE_TYPES
            if not image_extension in allowed_image_types:
                raise forms.ValidationError("Only %s file formats are supported! Current file format is %s" % (
                    allowed_image_types, image_extension))
            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                raise forms.ValidationError("Please keep filesize under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_IMAGE_UPLOAD_SIZE), filesizeformat(image.size)))
        return image

    def save(self, *args, **kwargs):
        self.uf.save(*args, **kwargs)
        return super(AdminUserStaffForm, self).save(*args, **kwargs)
