from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserProfile(AbstractUser):
    class ClassName(models.TextChoices):
        SLO3A = 'slo3a', _('Klasa 3a SLO')
        TEST = 'test', _('Klasa testowa')

    class_name = models.CharField(
        max_length=5,
        choices=ClassName.choices,
        default=ClassName.SLO3A,
    )

    def is_upperclass(self):
        return self.class_name in {
            self.ClassName.SLO3A,
        }

    math_teacher = models.CharField(
        max_length=30,
    )

    english_teacher = models.CharField(
        max_length=30,
    )

    physics_teacher = models.CharField(
        max_length=30,
    )

    biology_teacher = models.CharField(
        max_length=30,
    )

    chemistry_teacher = models.CharField(
        max_length=30,
    )

    geography_teacher = models.CharField(
        max_length=30,
    )

    history_teacher = models.CharField(
        max_length=30,
    )

    polish_teacher = models.CharField(
        max_length=30,
    )

    pe_teacher = models.CharField(
        max_length=30,
    )

    german_teacher = models.CharField(
        max_length=30,
    )

    spanish_teacher = models.CharField(
        max_length=30,
    )

    french_teacher = models.CharField(
        max_length=30,
    )

    russian_teacher = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.username
