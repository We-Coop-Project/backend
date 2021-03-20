from django.contrib import admin
from .models.api_v1 import User_status, Company, HireType
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    # list_display_links = None
    # list_editable = ('name',)
    search_fields =['name']
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Company, CompanyAdmin)
admin.site.register(User_status)
admin.site.register(HireType)
