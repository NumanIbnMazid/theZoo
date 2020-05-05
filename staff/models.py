from django.db import models
from .utils import upload_image_path
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from middlewares.middlewares import RequestMiddleware
from django.db.models import Q


class StaffQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (Q(user__username__icontains=query) |
                   Q(user__first_name__icontains=query) |
                   Q(user__last_name__icontains=query) |
                   Q(role__icontains=query) |
                   Q(gender__icontains=query) |
                   Q(dob__icontains=query) |
                   Q(address__icontains=query) |
                   Q(phone__icontains=query) |
                   Q(posting__icontains=query) |
                   Q(insurance_cover__icontains=query)
                   )
        return self.filter(lookups).distinct()


class StaffManager(models.Manager):
    def get_queryset(self):
        return StaffQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def search(self, query):
        return self.get_queryset().search(query)


class Staff(models.Model):
    # STAFF_ROLE_CHOICES
    HIGH_LEVEL = 'High Level'
    MID_LEVEL = 'Mid Level'
    LOW_LEVEL = 'Low Level'
    STAFF_ROLE_CHOICES = (
        (HIGH_LEVEL, 'High Level'),
        (MID_LEVEL, 'Mid Level'),
        (LOW_LEVEL, 'Low Level'),
    )
    # GENDER_CHOICES
    MALE = 'Male'
    FEMALE = 'Female'
    OTHERS = 'Others'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE, related_name='user_staff', verbose_name='User'
    )
    role = models.CharField(
        max_length=100, choices=STAFF_ROLE_CHOICES, default='Low Level', verbose_name='Role'
    )
    gender = models.CharField(
        choices=GENDER_CHOICES, blank=True, null=True, max_length=10, verbose_name='gender'
    )
    dob = models.DateField(
        verbose_name='DOB', null=True, blank=True
    )
    address = models.CharField(
        max_length=255, verbose_name='Address', null=True, blank=True
    )
    phone = models.CharField(
        max_length=30, verbose_name='Phone', null=True, blank=True
    )
    posting = models.CharField(
        max_length=100, verbose_name='Posting', null=True, blank=True
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

    objects = StaffManager()

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_name(self):
        name = None
        if self.user.first_name or self.user.last_name:
            name = self.user.get_full_name()
        else:
            name = self.user.username
        return name

    def get_smallname(self):
        if self.user.first_name or self.user.last_name:
            name = self.user.get_short_name()
        else:
            name = self.user.username
        return name

    def get_dynamic_name(self):
        if len(self.get_username()) < 13:
            name = self.get_username()
        else:
            name = self.get_smallname()
        return name

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'x':
                return (field.name, self.x.title)
            else:
                value = "-"
                if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
                    value = field.value_from_object(self)
                return (field.name, value)
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        ordering = ['-created_at']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_staff(sender, instance, created, **kwargs):
    if created:
        try:
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request
            role = request.POST.get("role")
            Staff.objects.create(
                user=instance, role=role,
            )
        except:
            if instance.is_superuser:
                Staff.objects.create(
                    user=instance, role="High Level"
                )
            else:
                Staff.objects.create(
                    user=instance
                )
    instance.user_staff.save()
