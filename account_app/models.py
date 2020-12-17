import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.html import format_html


def user_avatar_image_file_path(instance, filename):
    """Generate file path for user avatar image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/avatar', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    gender = [
        ('M', 'مرد'),
        ('F', 'زن'),
    ]
    avatar = models.ImageField(upload_to=user_avatar_image_file_path, default='uploads/user/avatar/default.png',
                               null=True, blank=True, verbose_name='آواتار')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی حساب کاربری')
    gender = models.CharField(max_length=5, choices=gender, default=None, null=True, blank=True, verbose_name='جنسیت')
    website = models.URLField(max_length=50, null=True, blank=True, verbose_name='وبسایت')
    is_ban = models.BooleanField(default=False, verbose_name='مسدود', )
    mobile = models.CharField(max_length=15, null=True, blank=True, verbose_name='شماره موبایل')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='شماره تلفن')
    postal_code = models.CharField(max_length=15, null=True, blank=True, verbose_name='کدپستی')
    address = models.TextField(max_length=500, null=True, blank=True, verbose_name='آدرس')
    email = models.EmailField(max_length=255, unique=True, verbose_name='ایمیل')
    name = models.CharField(max_length=255, verbose_name='نام')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_staff = models.BooleanField(default=False, verbose_name='ویژه')
    is_seller = models.BooleanField(default=False, verbose_name='فروشنده')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آپدیت')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'

    def avatar_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.avatar.url))
    avatar_tag.short_description = "آواتار"

    def get_delete_user_url(self):
        return f"/admin/user/{self.id}/delete"

    def get_user_url(self):
        return f"/admin/user/{self.id}"
