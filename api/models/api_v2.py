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
        primary_key=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class UserStatus(models.Model):
    uid = models.CharField(max_length=100, primary_key=True)
    coop_start_date = models.DateField()
    coop_end_date = models.DateField()
    coop_hours = models.IntegerField(default=0)
    week_coop_working_hours =  models.IntegerField(blank=True, null=True, default=0)
    week_non_coop_working_hours =  models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_statuses'
        verbose_name = 'user_status List'
        verbose_name_plural = 'user_status'

        # ordering = ['first_name', 'last_name']
    
    def __str__(self):
        return self.uid

class Company(models.Model):
    name = models.CharField(max_length=255)
    working_time = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True, default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    hire_type = models.ForeignKey(HireType, on_delete=models.CASCADE, related_name='hire_type')
    user = models.ForeignKey(UserStatus, on_delete=models.CASCADE, related_name='company_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'companies'
        verbose_name = 'company List'
        verbose_name_plural = 'companies'
    
    def __str__(self):
        return self.name