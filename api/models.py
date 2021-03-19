from django.db import models

class HireType(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    coop_flag = models.BooleanField(default=False)
    working_time = models.TimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hire_type = models.ForeignKey(HireType, on_delete=models.CASCADE)
    
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
    coop_duration_code = models.CharField(max_length=255)
    coop_hours = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_statuses = models.ManyToManyField(Company, blank=True)

    class Meta:
        db_table = 'user_statuses'
        verbose_name = 'user_status List'
        verbose_name_plural = 'user_status'

        # ordering = ['first_name', 'last_name']
    
    def __str__(self):
        return self.uid