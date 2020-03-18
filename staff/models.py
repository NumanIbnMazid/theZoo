from django.db import models
from .utils import upload_image_path
from django.conf import settings



class Staff(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_staff', verbose_name='User'
    )
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    dob = models.DateField(
        verbose_name='DOB', null=True, blank=True
    )
    address = models.CharField(
        max_length=255, verbose_name='Address', null=True, blank=True
    )
    phone = models.CharField(
        max_length=30, verbose_name='Phone'
    )
    posting = models.CharField(
        max_length=100, verbose_name='Posting'
    )
    insurance_cover = models.IntegerField(
        verbose_name='Insurance Cover', null=True, blank=True
    )
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True, verbose_name='Image'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        ordering = ['-created_at']
