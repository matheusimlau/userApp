from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Django User model inherited from AbstractUser
    Currently blank but allows for easier migration in the future
    """