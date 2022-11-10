from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'birth_date', 'password']

    class Meta:
        db_table = 'tb_gbl_accounts_user'

    def __str__(self):
        return "{name} {lastname}".format(name=self.first_name, lastname=self.last_name)

    @staticmethod
    def create_user(first_name, last_name, gender, birth_date, email, password, **extra_fields):
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birth_date=birth_date,
            email=email,
            username=email.split("@")[0],
            password=password,
            created_at=datetime.datetime.now(),
        )
        return user

    @staticmethod
    def desactivate_user(email):
        user = User.objects.get(email=email)
        user.is_active = False
        user.save()
        return user

    @staticmethod
    def update_user(first_name, last_name, gender, birth_date, email, password):
        user = User.objects.get(email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.gender = gender
        user.birth_date = birth_date
        user.email = email
        user.password = password
        user.save()


    def get_user_by_email(email):
        user = User.objects.get(email=email)
        return user

    def get_user_by_id(id):
        user = User.objects.get(id=id)
        return user


