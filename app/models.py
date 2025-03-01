from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.ImageField(upload_to='donor', null=True, blank=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Volunteer(models.Model):
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.ImageField(upload_to='volunteer', null=True, blank=True)
    idpiv = models.ImageField(upload_to='volunteer', null=True, blank=True)
    aboutme = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_CHOICES, default='Pending')
    regdate =models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300, null=True)
    updationdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username
    
class DonationArea(models.Model):
    areaname = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname
    

DONATION_CHOICES=(
    ('Food Donation', 'Food Donation'),
    ('Cloth Donation', 'Cloth Donation'),
    ('Footwear Donation', 'Footwear Donation'),
    ('Books Donation', 'Books Donation'),
    ('Furniture Donation', 'Furniture Donation'),
    ('Vessel Donation', 'Vessel Donation'),
    ('Other', 'Other'),
)
    
class Donation(models.Model):
    choice  = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(choices=DONATION_CHOICES, max_length=100, null=True, blank=True)
    donationpic = models.ImageField(upload_to='donation', null=True, blank=True)
    collectionloc = models.CharField(max_length=300,null=True, blank=True)
    description = models.CharField(max_length=300,null=True, blank=True)
    status = models.CharField(max_length=20, choices=choice, null=True, blank=True, default='Pending')
    donationdate = models.DateField(null=True, blank=True)
    adminremark = models.CharField(max_length=200, null=True, blank=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE,null=True, blank=True)
    donationatea = models.ForeignKey(DonationArea, on_delete=models.CASCADE,null=True, blank=True)
    volunteerremark = models.CharField(max_length=200, null=True, blank=True)
    updationdate = models.DateField(null=True, blank=True, auto_now=True)
    def __str__(self):
        return self.donationname
    
class Gallery(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    deliverypiv = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donationn.donationname
    
