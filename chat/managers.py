from django.contrib.auth.models import UserManager as AbstractUserManager

from django.utils.translation import gettext_lazy as _


class CustomUserManager(AbstractUserManager):

    def get_or_create_for_cognito(self, jwt_token):
        if not jwt_token['email']:
            raise ValueError(_("The Email must be set"))
        
        user, created = self.get_or_create(email=jwt_token['email'], username=jwt_token['email'])
        return user

    # """
    # Custom user model manager where email is the unique identifiers
    # for authentication instead of usernames.
    # """
    # def create_user(self, email, password, **extra_fields):
    #     """
    #     Create and save a user with the given email and password.
    #     """
    #     if not email:
    #         raise ValueError(_("The Email must be set"))
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user

    # def create_superuser(self, email, password, **extra_fields):
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)
    #     extra_fields.setdefault("is_active", True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError(_("Superuser must have is_staff=True."))
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError(_("Superuser must have is_superuser=True."))
    #     return self.create_user(email, password, **extra_fields)
