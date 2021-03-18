from django.db import models

class User_status(models.Model):
    coop_start_date = models.DateField()
    coop_expire_date = models.DateField()
    coop_duration_code = models.CharField(max_length=255)
    working_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_statuses'
        verbose_name = 'user_status List'
        verbose_name_plural = 'user_status'
    
    def __str__(self):
        return "user_status"


class Company(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_statuses = models.ManyToManyField(User_status)

    class Meta:
        db_table = 'companies'
        verbose_name = 'company List'
        verbose_name_plural = 'companies'
    
    def __str__(self):
        return self.name