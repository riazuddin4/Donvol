from django.contrib import admin
from .models import Donation, DonationArea, Donor, Gallery, Volunteer

# Register your models here.

admin.site.register(Donor)
admin.site.register(Volunteer)
admin.site.register(DonationArea)
admin.site.register(Donation)
admin.site.register(Gallery)



