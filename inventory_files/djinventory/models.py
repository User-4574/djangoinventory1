from django.db import models
from datetime import datetime
from django.utils import timezone
from private_storage.fields import PrivateFileField


class Cpu_table(models.Model):
        Name = models.CharField(max_length=16)
        Mfgdate = models.CharField(max_length=4)
        Url = models.CharField(max_length=100)
        Graphic = models.ImageField(upload_to='cpu_images')
        Score = models.CharField(max_length=4)
        String = models.CharField(max_length=16)
        Fullstring = models.CharField(max_length=100)
        def __str__(self):
                return '{} - {}'.format(self.pk, self.name)

class Department(models.Model):
        Department = models.CharField(max_length=50)
        def __str__(self):
                return self.Department

class Manager(models.Model):
        Username = models.CharField(max_length=32)
        Department = models.ForeignKey('Department', on_delete=models.SET_NULL,blank=True,null=True)
        Email_enable = models.BooleanField(default=True)
        def __str__(self):
                return '{} - {}'.format(self.Username,self.Department)


class Employee(models.Model):
        Account = models.CharField(max_length=32)
        First_name = models.CharField(max_length=32)
        Last_name = models.CharField(max_length=32)
        Entry_date = models.DateTimeField(auto_now=True)
        Work_email = models.CharField(max_length=500)
        Personal_email = models.CharField(max_length=500)
        Work_phone = models.CharField(max_length=14)
        Extension = models.PositiveSmallIntegerField()
        Home_phone = models.CharField(max_length=14,default='unknown')
        Street = models.CharField(max_length=32)
        City = models.CharField(max_length=32)
        State = models.CharField(max_length=32,default='TX')
        Country = models.CharField(max_length=32, default='USA')
        Department = models.ForeignKey('Department', on_delete=models.SET_NULL,blank=True,null=True)
        Site = models.ForeignKey('Site', on_delete=models.SET_NULL,blank=True,null=True)
        Hire_date = models.DateTimeField()
        Timestamp = models.DateTimeField(auto_now=True)
        Picture = PrivateFileField("Picture", upload_to='employee_pictures',blank=True,null=True)
        Remote = models.BooleanField(default=True)
        Active = models.BooleanField(default=True)
        Pic_time_stamp = models.DateTimeField(blank=True,null=True)
        def __str__(self):
                return self.Account

class System(models.Model):
        Host_name = models.CharField(max_length=32)
        Uuid = models.UUIDField(db_index=True)
        Ip_address = models.CharField(max_length=15,blank=True,null=True)
        External_ipaddress= models.CharField(max_length=15,blank=True,null=True)
        Dns_address=models.CharField(max_length=50,blank=True,null=True)
        Ram = models.SmallIntegerField(blank=True,null=True)
        OS_info = models.CharField(max_length=100,blank=True,null=True)
        System_information = models.TextField(blank=True,null=True)
        Drive = models.TextField(blank=True,null=True)
        Monitor = models.TextField(blank=True,null=True)
        Isp = models.CharField(max_length=100,blank=True,null=True)
        Added = models.DateTimeField(auto_now_add=True)
        Cpu_id = models.ForeignKey('Cpu_table', on_delete=models.SET_NULL,blank=True,null=True)
        User_id = models.ForeignKey('Employee', on_delete=models.SET_NULL,blank=True,null=True)
        Site = models.ForeignKey('Site', on_delete=models.SET_NULL,blank=True,null=True)
        Check_in = models.DateTimeField(auto_now=True)
        Cpufullstring = models.CharField(max_length=100,blank=True,null=True)
        Laptop = models.BooleanField(blank=True,null=True)
        Local_admin_password = models.CharField(max_length=20,blank=True,null=True)
        Local_encryption_password_key = models.CharField(max_length=100,blank=True,null=True)
        Notes = models.TextField(blank=True,null=True)
        Vpn_key = models.CharField(max_length=20,blank=True,null=True)
        Handoff_date=models.DateTimeField(blank=True,null=True)
        System_update_status=models.BooleanField(default=False)
        Export_to_api=models.BooleanField(default=True)
        Export_to_windows_api=models.BooleanField(default=False)
        Enable_alerts=models.BooleanField(default=True)
        Encryption_password_enforcement=models.BooleanField(default=True)
        def __str__(self):
                return '{} - {}'.format(self.Host_name, self.Ip_address)

class Component_type(models.Model):
        Type = models.CharField(max_length=100)
        def __str__(self):
                return self.Type


class System_change_log(models.Model):
        System = models.ForeignKey('System', on_delete=models.SET_NULL,blank=True,null=True)
        Log = models.TextField()
        Added = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return '{} - {}'.format(str(self.System), self.Log)

class Component_log(models.Model):
        Component = models.ForeignKey('Component', on_delete=models.CASCADE)
        Old_system = models.ForeignKey('System', on_delete=models.SET_NULL,blank=True,null=True)
        New_system = models.ForeignKey('System', on_delete=models.SET_NULL,related_name='+',blank=True,null=True)
        Account = models.CharField(max_length=100,blank=True,null=True)
        Added = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return '{} - {} - {}'.format(self.Old_system, self.New_system, self.Component)


class Manufacturer(models.Model):
        Name = models.CharField(max_length=100)
        Information = models.TextField(blank=True,null=True)
        Added = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return self.Name

CAPACITY_TYPES = (
        ('KB', 'KB'),
        ('GB', 'GB'),
        ('MB', 'MB'),
        ('TB', 'TB'),
)


class Component_list(models.Model):
        Component_type = models.ForeignKey('Component_type', on_delete=models.CASCADE)
        Part_number = models.CharField(max_length=100, unique=True)
        Capacity = models.CharField(max_length=10,blank=True,null=True)
        Capacity_type = models.CharField(max_length=2, choices=CAPACITY_TYPES,blank=True)
#        Picture = PrivateFileField("Picture", upload_to='part_pics',blank=True,null=True)
        Manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
        Added = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return self.Part_number


class Component(models.Model):
        Serial_number = models.CharField(max_length=100,unique=True)
        Part_number = models.ForeignKey('Component_list', on_delete=models.SET_NULL,blank=True,null=True)
        Purchase = models.ForeignKey('Purchase', on_delete=models.SET_NULL, blank=True,null=True)
        System = models.ForeignKey('System', on_delete=models.SET_NULL,blank=True,null=True)
        Label = models.CharField(max_length=100,blank=True,null=True)
        Manual_assignment = models.BooleanField(default=False)
        Account = models.CharField(max_length=100,blank=True,null=True)
        Added = models.DateTimeField(auto_now_add=True)
        Rma = models.ForeignKey('Rma', on_delete=models.SET_NULL,blank=True,null=True)
        #parttype = myparttype(name='blah')
        def Part_type(self):
                data = Component_list.objects.get(Part_number=str(self.Part_number))
                return str(data.Component_type)
        def __str__(self):
                return '{} - {}'.format(self.Serial_number, self.Part_number)
        def save(self, *args, **kwargs):
                try:
                        MYPART = Component_list.objects.get(Serial_number=self.Serial_number)
                        if MYPART.System != self.System:
                                Component_logging.objects.create(Component=self, Old_system=MYPART.System, New_system=self.System, account=self.Account)
                except Exception:
                        blah = int()
                super().save(*args, **kwargs)



class Rma_reasons(models.Model):
        Reason = models.CharField(max_length=500)
        def __str__(self):
                return self.reason

class Rma_pictures(models.Model):
        Picture = models.ImageField(upload_to='rmas')
        Notes = models.CharField(max_length=1000)
        Rma = models.ForeignKey('Rma', on_delete=models.SET_NULL,blank=True,null=True)
        def __str__(self):
                return str(self.Rma)
class Rma_status(models.Model):
        Status = models.CharField(max_length=600)
        def __str__(self):
                return self.status

class Rma(models.Model):
        Vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL,blank=True,null=True)
        Reason = models.ForeignKey('Rma_reasons', on_delete=models.SET_NULL,blank=True,null=True)
        Status = models.ForeignKey('Rma_status', on_delete=models.SET_NULL,blank=True,null=True)
        Return_address_street = models.CharField(max_length=2000)
        Return_address_city_state_zip = models.CharField(max_length=2000)
        Documentation = models.TextField()
        Owner=models.CharField(max_length=15)
        Added = models.DateTimeField(auto_now_add=True)
        Shipped_to_vendor = models.BooleanField(default=False)
        Returned_from_vendor = models.BooleanField(default=False)
        def __str__(self):
                return '{} - {} - {}'.format(self.pk, self.Vendor,self.Status)


class Vendor(models.Model):
        Vendor_name = models.CharField(max_length=50)
        Vendor_link = models.CharField(max_length=200)
        Notes = models.TextField()
        Added = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return self.Vendor_name



class Purchase(models.Model):
        Vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
        Notes = models.TextField(blank=True,null=True)
        Box = models.ImageField(upload_to='purchases',blank=True,null=True)
        Reciept_picture = PrivateFileField("Reciept", upload_to='order_reciepts',blank=True,null=True)
        Box_picture = PrivateFileField("Box", upload_to='order_boxes',blank=True,null=True)
        Amount = models.PositiveSmallIntegerField()
        Entry_date = models.DateTimeField(auto_now_add=True,null=True)
        def __str__(self):
                return '{} - {}'.format(self.pk, str(self.Vendor))

class Site(models.Model):
        Site_name = models.CharField(max_length=200)
        Street = models.CharField(max_length=32)
        City = models.CharField(max_length=32)
        State = models.CharField(max_length=2,default='TX')
        Country = models.CharField(max_length=32, default='USA')


#class Setting(models.Model):
#        Name=models.CharField(max_length=100)
#        Default_component_assignment = models.ForeignKey('System', on_delete=models.SET_NULL,blank=True,null=True)
#        notes = models.TextField()



class Issue(models.Model):
        Issue=models.CharField(max_length=50)
        def __str__(self):
                return self.Issue

class Ticket_status(models.Model):
        Status=models.CharField(max_length=50)
        def __str__(self):
                return self.Status

class Ticket(models.Model):
        User=models.ForeignKey('Employee', on_delete=models.SET_NULL,blank=True,null=True)
        Issue=models.ForeignKey('Issue', on_delete=models.SET_NULL,blank=True,null=True)
        Ticket_status=models.ForeignKey('Ticket_status', on_delete=models.SET_NULL,blank=True,null=True)
        Sla = models.BooleanField(default=True)
        Problem=models.CharField(max_length=200)
        Email_user=models.BooleanField(default=False)
        Email_managers=models.BooleanField(default=False)
        Ticket_owner=models.CharField(max_length=15)
        Added = models.DateTimeField(auto_now_add=True)
        Minutes = models.IntegerField(default=0)
        def __str__(self):
                return '{} -- {} -- {}'.format(self.User, self.Problem,self.Added)


class Ticket_notes(models.Model):
        User=models.CharField(max_length=50)
        Start = models.DateTimeField(default=timezone.now)
        Text = models.TextField()
        Upload = PrivateFileField("file", upload_to='opentickets',blank=True,null=True)
        Hidden = models.BooleanField(default=False)
        Ticket = models.ForeignKey('Ticket', on_delete=models.SET_NULL,blank=True,null=True)
        Minutes = models.IntegerField(default=0)
        Added = models.DateTimeField(auto_now_add=True)
        def save(self, *args, **kwargs):
                seconds = (timezone.now() - self.start).total_seconds()
                minutes = seconds/60
                self.Minutes=int(minutes)
                myticket = Ticket.objects.get(pk=self.Ticket)
                myticket.minutes_spent = (myticket.Minutes + minutes)
                myticket.save()
                super().save(*args, **kwargs)

class Closed_ticket(models.Model):
        User=models.ForeignKey('Employee', on_delete=models.SET_NULL,blank=True,null=True)
        Old_id=models.CharField(max_length=50)
        Sla = models.BooleanField(default=True)
        Issue=models.ForeignKey('Issue', on_delete=models.SET_NULL,blank=True,null=True)
        Problem=models.CharField(max_length=200)
        Owner=models.CharField(max_length=15)
        Ticket_creation = models.DateTimeField()
        Closer = models.CharField(max_length=100)
        Closed = models.DateTimeField(auto_now_add=True)
        Minutes = models.IntegerField(default=0)
        Update_count = models.IntegerField(default=0)
        Minutes_open = models.IntegerField(default=0)
        def __str__(self):
                return '{} - {}'.format(self.pk,self.User)

class Closed_ticket_notes(models.Model):
        User=models.CharField(max_length=50)
        Added = models.DateTimeField(auto_now_add=True)
        Text = models.TextField()
        Upload = PrivateFileField("file", upload_to='opentickets',blank=True,null=True)
        Hidden = models.BooleanField(default=True)
        Ticket = models.ForeignKey('Closed_ticket', on_delete=models.SET_NULL,blank=True,null=True)
        Minutes = models.IntegerField(default=0)
        def __str__(self):
                return str(self.User)

class Decomissioned_component(models.Model):
        Serial_number = models.CharField(max_length=100)
        Part_number = models.ForeignKey('Component', on_delete=models.SET_NULL,blank=True,null=True)
        Purchase = models.ForeignKey('Purchase', on_delete=models.SET_NULL, blank=True,null=True)
        Account = models.CharField(max_length=100,blank=True,null=True)
        Added = models.DateTimeField(auto_now_add=True)
        Rma = models.ForeignKey('Rma', on_delete=models.SET_NULL,blank=True,null=True)

class Decomissioned_system(models.Model):
        Uuid = models.UUIDField(db_index=True)
        System_information = models.TextField(blank=True,null=True)
        Cpufullstring = models.CharField(max_length=100,blank=True,null=True)
        Account = models.CharField(max_length=100,blank=True,null=True)
        Decom_date = models.DateTimeField(auto_now_add=True)

class Asset(models.Model):
        Active=models.BooleanField(default=True)
        Serial_number = models.CharField(max_length=100,unique=True)
        User = models.ForeignKey('Employee', on_delete=models.SET_NULL,blank=True,null=True)
        Component = models.ForeignKey('Component_list', on_delete=models.SET_NULL,blank=False,null=True)
        Manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
        system = models.ForeignKey('System', on_delete=models.SET_NULL,blank=True,null=True)
        Purchase = models.ForeignKey('Purchase', on_delete=models.SET_NULL, blank=False,null=True)
        RMA = models.ForeignKey('Rma', on_delete=models.SET_NULL, blank=True,null=True)
        Extra_information = models.TextField(blank=True,null=True)
        Picture=PrivateFileField("assetpicture", upload_to='assetpictures',blank=True,null=True)
        Asset_type=models.ForeignKey('Asset_type', on_delete=models.SET_NULL, blank=True,null=True)
        def __str__(self):
                return '{} - {} - {}'.format(self.SerialNumber,self.user_id,self.PartNumber)

class Assetlog(models.Model):
        Asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
        Log = models.TextField()
        Time_stamp = models.DateTimeField(auto_now_add=True)
        User_stamp = models.TextField()

class Asset_type(models.Model):
        Asset = models.CharField(max_length=100,unique=True)
        Notes = models.TextField(blank=True,null=True)
        def __str__(self):
                return str(self.Asset)

