import uuid
import os

from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


# def image_file_path(instance, filename):
#     """Generate file path for new recipe image"""
#     ext = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'
#
#     return os.path.join('uploads/', filename)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, username, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not username:
            raise ValueError('The given phone must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(null=False, unique=True, blank=False, max_length=10,

                                # Biểu thức regex cho số điện thoại tại Việt Nam, bắt đầu bằng số 0
                                validators=[RegexValidator(
                                    r'^(03|05|07|08|09|01[2|6|8|9])+([0-9]{8})$')])  # Biểu thức regex cho số điện
    # email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='uploads/%Y/%m', null=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name="user_friends",
                                       blank=True,
                                       symmetrical=False)
    friends_requests = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name="user_friend_requests",
                                       blank=True,
                                       symmetrical=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # def number_of_followers(self):
    #     if self.followers.count():
    #         return self.followers.count()
    #     else:
    #         return 0
    #
    # def number_of_following(self):
    #     if self.following.count():
    #         return self.following.count()
    #     else:
    #         return 0

    def __str__(self):
        return self.username


# class Post(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='user_posts'
#     )
#     image = models.ImageField(
#         upload_to='posts/%Y/%m', default=None,
#         blank=False,
#         editable=False)
#     described = models.TextField(max_length=500, blank=True)
#     # location = models.CharField(max_length=30, blank=True)
#     posted_on = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
#                                    related_name="likers",
#                                    blank=True,
#                                    symmetrical=False)
#
#     class Meta:
#         ordering = ['-posted_on']
#
#     def number_of_likes(self):
#         if self.likes.count():
#             return self.likes.count()
#         else:
#             return 0
#
#     def __str__(self):
#         return f'{self.author}\'s post'
#
#
# class Comment(models.Model):
#     post = models.ForeignKey('Post',
#                              on_delete=models.CASCADE,
#                              related_name='post_comments')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                on_delete=models.CASCADE,
#                                related_name='user_comments')
#     text = models.CharField(max_length=100)
#     posted_on = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-posted_on']
#
#     def __str__(self):
#         return f'{self.author}\'s comment'
