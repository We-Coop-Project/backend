from django.db import models

class HireType(models.Model):
    COOP = 'CO'
    OTHER = 'OT'
    COMPANY_TYPE_CHOICES = [
        (COOP, 'coop'),
        (OTHER, 'other'),
    ]

    name = models.CharField(
        max_length=255,
        choices=COMPANY_TYPE_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    coop_flag = models.BooleanField(default=False)
    working_time = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    hire_type = models.ForeignKey(HireType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'companies'
        verbose_name = 'company List'
        verbose_name_plural = 'companies'
    
    def __str__(self):
        return self.name


class User_status(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    coop_start_date = models.DateField()
    coop_end_date = models.DateField()
    coop_hours = models.IntegerField()
    company_statuses = models.ManyToManyField(Company, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_statuses'
        verbose_name = 'user_status List'
        verbose_name_plural = 'user_status'

        # ordering = ['first_name', 'last_name']
    
    def __str__(self):
        return self.uid