from django.contrib import admin
from django import forms
import re
from django.utils import timezone
from django.db.models.functions import Now
admin.site.disable_action('delete_selected')

#Import all models used. Keeping them in one place prevents duplicate loading.
from .models import System
from .models import Component
from .models import Cpu_table
from .models import Site
from .models import Purchase
from .models import *
    

##################
#Systems page

class Mysystempart(admin.TabularInline):
    model = Component
#    readonly_fields = ('Serial_number','Part_number','Label','Part_type',)
    exclude = ['Account','Rma',]
    extra = 0

class Mysystem(admin.ModelAdmin):
    inlines = (Mysystempart,)
    search_fields = ('Host_name','Ip_address','OS_info','System_info','Drive','Monitor','Isp','Added','User_id__First_name','User_id__Last_name','User_id__Account','Notes',)
    readonly_fields = ('Added', 'Check_in', 'Ip_address',)
    #readonly_fields = ('Added', 'Check_in', 'Ip_address', 'External_ipaddress', 'Cpufullstring','System_info','Check_in','Isp', 'System_update_status',)
    extra = 0
admin.site.register(System, Mysystem)

##################
#Processor table


class MyCputable(admin.ModelAdmin):
    extra = 0
admin.site.register(Cpu_table, MyCputable)

##################
#Sites

class Mysite(admin.ModelAdmin):
    extra = 0
admin.site.register(Site, Mysite)

#Purchases
class Asset_inline(admin.TabularInline):
        model = Asset
        extra = 0
#        readonly_fields=('Serial_number','User','Component','Purchase',)
        def has_add_permission(self, request, obj=None):
                return False
        def has_change_permission(self, request, obj=None):
                return False

class Mypurchase_component(admin.TabularInline):
        model = Component
        extra = 0
class Mypurchase(admin.ModelAdmin):
       fields = ( 'Receipt_tag', )
       readonly_fields = ('pk','Entry_date',)
       inlines = (Mypurchase_component,Asset_inline,)
admin.site.register(Purchase, Mypurchase)



