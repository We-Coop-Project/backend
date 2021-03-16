from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# class user_status(models.Model):
#     coop_start_date = models.DateField()
#     coop_expire_date = models.DateField()
#     coop_duration_code = models.CharField(max_length=255)
#     working_time = models.TimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return "user_status"
