from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.companies.models import Company
from apps.common.models import TimeStampedModel


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

class Role(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'company')
    
class CompanyUser(TimeStampedModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('invited', 'Invited'),
        ('suspended', 'Suspended'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='company_memberships'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='user_memberships'
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f"{self.user.email} → {self.company.name}"

