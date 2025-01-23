from datetime import date
import random
from django.http import HttpResponse
from django.shortcuts import redirect, render

from donvol.settings import EMAIL_HOST_USER
from .models import Donation, DonationArea, Donor, Gallery, Volunteer
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


# Create your views here.
# @login_required(login_url='login_donor')
def index(request):
    return render(request, "index.html")


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, "gallery.html", {'gallery': gallery})


def login_admin(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        User = authenticate(username = username, password = password)
        print(User)
        if User:
            login(request, User)
            messages.success(request, "Logged in.")
            return redirect('index_admin')
        else:
            messages.error(request, "username or pass not matched.")
            # return redirect('signup_donor')
    return render(request, "login-admin.html")


def login_donor(request):
    
    # if request.user.is_authenticated:
    #     return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        User = authenticate(username = username, password = password)
        print(User)
        if User:
            login(request, User)
            messages.success(request, "Logged in.")
            return redirect('index_donor')
        else:
            messages.error(request, "username or pass not matched.")
            return redirect('signup_donor')
    

    return render(request, "login-donor.html")


def login_volunteer(request):

    # if request.user.is_authenticated:
    #     return redirect('index')
    
    if request.method == 'POST':
        # email = request.POST.get('name')
        username = request.POST.get('name')
        password = request.POST.get('pass')
        User = authenticate(username = username, password = password)
        print(User)
        if User:
            login(request, User)
            messages.success(request, "Logged in.")
            return redirect('index_volunteer')
        else:
            messages.error(request, "username or pass not matched.")
            return redirect('signup_volunteer')

    return render(request, "login-volunteer.html")


# def index_volunteer(request):
#     return render(request, "index-volunteer.html")


def signup_donor(request):
    if request.method == "POST":
        first_name =request.POST.get('firstname')
        last_name =request.POST.get('lastname')
        us =request.POST.get('username')
        email =request.POST.get('email')
        pic =request.FILES.get('userpic')
        contact =request.POST.get('contact')
        password =request.POST.get('pwd')
        password1 =request.POST.get('cpwd')
        address =request.POST.get('address')

        # if user.objects.filter(username = username).exists():
        #     messages.error(request,'This username is already been taken!')
        #     return redirect('reg')
        # elif User.objects.filter(email = email).exists():
        #     messages.error(request,'This email is already been taken!')
        #     return redirect('reg')
        
        if password == password1:
            if len(password) >= 6:
                ck = ['!','@','#','$','%','*']
                for i in ck:
                    if i not in password:
                        continue
                    elif i in password:
                        for j in [0,1,2,3,4,5,6,7,8,9]:
                            if str(j) not in password:
                                continue
                            elif str(j) in password:
                                user = User.objects.create(
                                    first_name = first_name,
                                    last_name = last_name,
                                    email = email,
                                    username = us,
                                    # username = first_name,
                                    # username = username,
                                )

                                user.set_password(password)
                                user.save()
                                donor = Donor(user=user, userpic=pic, contact=contact, address=address)
                                donor.save()
                            
                                messages.success(request, "User Created.")            
                                return redirect ('login_donor')
                        else:
                            messages.error(request, " No number found in password.")      
                            return redirect ('signup_donor')      
                else:
                    messages.error(request, "No Special charecter found in password.")
                    return redirect ('signup_donor')       
            else:
                messages.error(request, " password less then 8 charecter.")
                return redirect ('signup_donor') 
        else:
            messages.error(request, "password not matched with confirm password.")
            return redirect ('signup_donor') 
        

    return render(request, "signup_donor.html")


def signup_volunteer(request):
    if request.method == "POST":
        first_name =request.POST.get('firstname')
        last_name =request.POST.get('lastname')
        us =request.POST.get('username')
        email =request.POST.get('email')
        pic =request.FILES.get('userpic')
        contact =request.POST.get('contact')
        password =request.POST.get('pwd')
        password1 =request.POST.get('cpwd')
        address =request.POST.get('address')
        ipic = request.FILES.get('idpic')
        iaboutme =request.POST.get('aboutme')

        print(address,contact,pic,email,last_name,first_name, iaboutme,ipic,us),


        # if user.objects.filter(username = username).exists():
        #     messages.error(request,'This username is already been taken!')
        #     return redirect('reg')
        # elif User.objects.filter(email = email).exists():
        #     messages.error(request,'This email is already been taken!')
        #     return redirect('reg')
        
        if password == password1:
            if len(password) >= 6:
                ck = ['!','@','#','$','%','*']
                for i in ck:
                    if i not in password:
                        continue
                    elif i in password:
                        for j in [0,1,2,3,4,5,6,7,8,9]:
                            if str(j) not in password:
                                continue
                            elif str(j) in password:
                                user = User.objects.create(
                                    first_name = first_name,
                                    last_name = last_name,
                                    email = email,
                                    username = us,
                                )

                                user.set_password(password)
                                user.save()
                                volunteer = Volunteer(user=user, userpic=pic, contact=contact, address=address, idpiv=ipic, aboutme=iaboutme)
                                volunteer.save()
                            
                                messages.success(request, "User Created.")            
                                return redirect ('login_volunteer')
                        else:
                            messages.error(request, " No number found in password.")      
                            return redirect ('signup_volunteer')      
                else:
                    messages.error(request, "No Special charecter found in password.")
                    return redirect ('signup_volunteer')       
            else:
                messages.error(request, " password less then 8 charecter.")
                return redirect ('signup_volunteer') 
        else:
            messages.error(request, "password not matched with confirm password.")
            return redirect ('signup_volunteer')
    return render(request, "signup_volunteer.html")


def index_admin(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")

    totaldonations = Donation.objects.all().count()
    totaldonors = Donor.objects.all().count()
    totalvolunteers = Volunteer.objects.all().count()
    totalpendingdonations = Donation.objects.filter(status="Pending").count()
    totalaccepteddonations = Donation.objects.filter(status="Accepted").count()
    totaldelivereddonations = Donation.objects.filter(status="Donation Delivered Successfully").count()
    totaldinationareas = DonationArea.objects.all().count()

    return render(request, "index-admin.html", locals())


# admin dashboard
def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status='Pending')
    return render(request, "pending-donation.html", locals())


def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status="Accepted")
    return render(request, "accepted-donation.html", locals())


def rejected_donation(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status="Rejected")
    return render(request, "rejected-donation.html", locals())


def volunteerallocated_donation(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status="Volunteer Allocated")
    return render(request, "volunteerallocated-donation.html", locals())


def donationrec_admin(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status="Donation Recevired")
    return render(request, "donationrec-admin.html", locals())


def donationnotrec_admin(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status="Donation NotRecevired")
    return render(request, "donationnotrec-admin.html", locals())


def donationdelivered_admin(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.filter(status="Donation Delivered Successfully")
    return render(request, "donationdelivered-admin.html", locals())


def all_donations(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.all()
    return render(request, "all-donations.html", locals())


def delete_donation(request,pid):
    donation = Donation.objects.get(id=pid)
    donation.delete()
    return redirect('all_donations')



def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donor = Donor.objects.all()
    return render(request, "manage-donor.html", locals())


def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    volunteer = Volunteer.objects.filter(status='Pending')
    return render(request, "new-volunteer.html", locals())


def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    volunteer = Volunteer.objects.filter(status="Accepted")
    return render(request, "accepted-volunteer.html", locals())


def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    volunteer = Volunteer.objects.filter(status='Rejected')
    return render(request, "rejected-volunteer.html", locals())


def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    volunteer = Volunteer.objects.all()
    return render(request, "all-volunteer.html", locals())

def delete_volunteer(request,pid):
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('all_volunteer')


def add_area(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    if request.method == "GET":
        areaName = request.GET.get("areaname")
        description = request.GET.get("description")
        try:
            DonationArea.objects.create(areaname=areaName,description=description)
            messages.success(request,'Area Added Successfully')
        except:
            messages.warning(request,'add-area Not added')

    return render(request, "add-area.html", locals())

def edit_area(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    
    area = DonationArea.objects.get(id=pid)

    if request.method == "GET":
        return render(request, "edit-area.html", locals())
    elif request.method == "POST":
        areaName = request.GET.get("areaname")
        description = request.GET.get("description")

        area.areaname = areaName
        area.description = description
        # print(area.areaname,area.description)
        try:
            area.save()
            messages.success(request,'Area Updated Successfully')
            return redirect('manage_area')
        except:
            messages.warning(request,'add-area Not Updated')
        return render(request, "edit-area.html", locals())


def manage_area(request):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    area = DonationArea.objects.all()
    
    return render(request, "manage-area.html", locals())

def delete_area(request,pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    area = DonationArea.objects.get(id=pid)
    area.delete()
    return redirect('manage_area')


def changepwd_admin(request):
    if request.method == "POST":
        oldpass = request.POST.get('currentpassword')
        newpass = request.POST.get('newpassword')
        comfpass = request.POST.get('confirmpassword')

        # print(newpass, comfpass)
        try:
            if newpass == comfpass:
                user = User.objects.get(id=request.user.id)
                if user.check_password(oldpass):
                    user.set_password(newpass)
                    user.save()
                    messages.success(request, 'change password Successfully')
                else:
                    messages.warning(request, 'old password ont matched')
            else:
                messages.warning(request, 'old password and New password are different')
        except:
            messages.warning(request, 'Faild to change password ')
    return render(request, "changepwd-admin.html")


def logout_user(request):
    logout(request)
    return redirect("index")

# admin view details
def accepted_donationdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")

    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    # volunteer = Volunteer.objects.filter(status='Accepted')
    volunteer = Volunteer.objects.all()

    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        adminremark = request.POST['adminremark']
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)

        try:
            donation.donationatea = da
            donation.volunteer = v
            donation.adminremark = adminremark
            donation.status = "Volunteer Allocated"
            donation.volunteerremark = "Not Updated Yet"
            donation.updationdate = timezone.now()
            donation.save()
            messages.success(request,'Volunteer Allocated Successfully')
        except:
            messages.warning(request,'Failld to Allocate Volunteer')
    return render(request, "accepted-donationdetail.html", {'donation': donation, 'donationarea': donationarea, 'volunteer': volunteer})


def view_volunteerdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    volunteer = Volunteer.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']
        try:
            volunteer.adminremark = adminremark
            volunteer.status = status
            volunteer.updationdate = timezone.now()
            volunteer.save()
            messages.success(request, 'Volunteer updated Successfully')
        except:
            messages.warning(request, 'Volunteer Not updated Successfully')
    return render(request, "view-volunteerdetail.html", locals())


def view_donordetail(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donor = Donor.objects.get(id=pid)

    return render(request, "view-donordetail.html", locals())

def view_donationdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    
    if request.method == "GET":
        donation = Donation.objects.get(id=pid)
        return render(request, "view-donationdetail.html", {'donation': donation})
    
    if request.method == "POST":
        status = request.POST["status"]
        adminremark = request.POST["adminremark"]

        try:
            donation = Donation.objects.get(id=pid)
            donation.status = status
            donation.adminremark = adminremark
            donation.updationdate = timezone.now()
            donation.save()
            
            messages.success(request, 'Status & Remark Updated Successfully')
        except Donation.DoesNotExist:
            messages.warning(request, 'Donation not found')
        except Exception as e:
            messages.warning(request, f'Failed to Update status & Remark: {str(e)}')
        
        return render(request, "view-donationdetail.html", {'donation': donation})

def delete_donor(request,pid):
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('manage_donor')

# donor dashboard
def index_donor(request):
    if not request.user.is_authenticated:
        return redirect("login_donor")

    user = request.user
    donor = Donor.objects.get(user=user)
    donationcount = Donation.objects.filter(donor=donor).count()
    acceptedcount = Donation.objects.filter(donor=donor, status="Accept").count()
    rejectedcount = Donation.objects.filter(donor=donor, status="Reject").count()
    pendingcount = Donation.objects.filter(donor=donor, status="Pending").count()
    deliveredcount = Donation.objects.filter(donor=donor, status="Donation Delivered Successfully").count()
    return render(request, "index-donor.html", locals())


def donate_now(request):
    if request.method == "POST":
        
        user = User.objects.filter(username=request.user).first()
        donor = Donor.objects.get(user=user)
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        
        try:
            Donation.objects.create(donor=donor, donationname=donationname, donationpic=donationpic, 
            collectionloc=collectionloc, description=description, donationdate=date.today())
            messages.success(request,"Donation save Successfully")
        except Exception as e:
            messages.warning(request,'Failed to Donation')

    return render(request, "donate-now.html", locals())


def donation_history(request):
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, "donation-history.html", locals())


def profile_donor(request):
    user = request.user
    donor = Donor.objects.get(user=user)

    if request.method == "POST":
        first_name =request.POST.get('firstname')
        last_name =request.POST.get('lastname')
        # us =request.POST.get('username')
        # email =request.POST.get('email')
        # pic =request.FILES.get('userpic')
        contact =request.POST.get('contact')
        address =request.POST.get('address')

        donor.user.first_name = first_name
        donor.user.last_name = last_name
        donor.user.contact = contact
        donor.user.address= address

        try:
            userpic = request.FILES['userpic']
            donor.userpic = userpic
            donor.save()
            donor.user.save()
            messages.success(request, 'profile updated successfully')
        except Exception as e:
            messages.warning(request, 'profile updated failed'+e)
        

    return render(request, "profile-donor.html", {"donor":donor})


def changepwd_donor(request):
    if request.method == "POST":
        oldpass = request.POST.get('currentpassword')
        newpass = request.POST.get('newpassword')
        comfpass = request.POST.get('confirmpassword')

        # print(newpass, comfpass)
        try:
            if newpass == comfpass:
                user = User.objects.get(id=request.user.id)
                if user.check_password(oldpass):
                    user.set_password(newpass)
                    user.save()
                    messages.success(request, 'change password Successfully')
                else:
                    messages.warning(request, 'old password ont matched')
            else:
                messages.warning(request, 'old password and New password are different')
        except:
            messages.warning(request, 'Faild to change password ')

    return render(request, "changepwd-donor.html")


# volunteer dashboard
def index_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_volunteer")

    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    totalCollectionReg = Donation.objects.filter(volunteer=volunteer, status="Volunteer Allocated").count()
    totalRecDonation = Donation.objects.filter(volunteer=volunteer, status="Donation Received").count()
    totalNotRecDonation = Donation.objects.filter(volunteer=volunteer, status="Donation NotReceived").count()
    totalDonationDelivered = Donation.objects.filter(volunteer=volunteer, status="Donation Delivered Successfully").count()
    return render(request, "index-volunteer.html", locals())


def collection_req(request):
    if not request.user.is_authenticated:
        return redirect("login_volunteer")

    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Volunteer Allocated")
    return render(request, "collection-req.html", locals())


def donationrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_volunteer")

    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Donation Received")
    return render(request, "donationrec-volunteer.html", locals())


def donationnotrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_volunteer")

    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Donation NotReceived")
    return render(request, "donationnotrec-volunteer.html")


def donationdelivered_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("login_volunteer")

    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Donation Delivered Successfully")
    return render(request, "donationdelivered-volunteer.html", locals())


def profile_volunteer(request):
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    
    if request.method == "POST":
        first_name =request.POST.get('firstname')
        last_name =request.POST.get('lastname')
        # us =request.POST.get('username')
        # email =request.POST.get('email')
        # pic =request.FILES.get('userpic')
        contact =request.POST.get('contact')
        address =request.POST.get('address')

        volunteer.user.first_name = first_name
        volunteer.user.last_name = last_name
        volunteer.user.contact = contact
        volunteer.user.address= address

        try:
            userpic = request.FILES['userpic']
            volunteer.userpic = userpic
            idpiv =request.FILES['idpiv']
            volunteer.idpiv = idpiv
            volunteer.save()
            volunteer.user.save()
            messages.success(request, 'profile updated successfully')
        except Exception as e:
            messages.warning(request, 'profile updated failed'+e)
    return render(request, "profile-volunteer.html", locals())


def changepwd_volunteer(request):
    if request.method == "POST":
        oldpass = request.POST.get('currentpassword')
        newpass = request.POST.get('newpassword')
        comfpass = request.POST.get('confirmpassword')

        # print(newpass, comfpass)
        try:
            if newpass == comfpass:
                user = User.objects.get(id=request.user.id)
                if user.check_password(oldpass):
                    user.set_password(newpass)
                    user.save()
                    messages.success(request, 'change password Successfully')
                else:
                    messages.warning(request, 'old password ont matched')
            else:
                messages.warning(request, 'old password and New password are different')
        except:
            messages.warning(request, 'Faild to change password ')
    return render(request, "changepwd-volunteer.html")


# view details
def donationdetail_donor(request, pid):
    
    donation = Donation.objects.get(id=pid)
    return render(request, "donationdetail-donor.html", {'donation':donation})


def donationcollection_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    
    donation = Donation.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        volunteerremark = request.POST['volunteerremark']

        try:
            donation.status = status
            donation.volunteerremark = volunteerremark
            donation.updationdate = timezone.now()
            donation.save()
            messages.success(request, 'Volunteer Status & Remark updated Succefully')
        except:
            messages.success(request, 'Failed to update Volunteer Status & Remark ')

    
    return render(request, "donationcollection-detail.html", locals())


def donationrec_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_admin")
    donation = Donation.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

        try:
            donation.status = status
            donation.updationdate = timezone.now()
            donation.save()
            Gallery.objects.create(donation=donation, deliverypiv=deliverypic)
            # Gallery(donation=donation, deliverypic=deliverypic).save()
            messages.success(request, 'Donation Delivered Successfull')
        except:
            messages.warning(request, 'Donation Delivery Failed')
    return render(request, "donationrec-detail.html", locals())


def Forgetpassword(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print("User Exists")
            # otp = random.randint(1111, 9999)
            send_mail("Reset Your Password:", f"Hey user: {user}! TO reset Password, click on the given link \n http://127.0.0.1:8000/NewPasswordPage/{user}/", EMAIL_HOST_USER, {email}, fail_silently=True)
            return HttpResponse('password reset Link  sent your email')
            

    return render(request, "Forget_password.html")

def NewPasswordPage(request, user):
    userid = User.objects.get(username=user)
    print(userid)
    if request.method == "POST":
        pass1 = request.POST.get('newpassword')
        pass2 = request.POST.get('confirmpassword')

        print('pass1 and pass2:', pass1, pass2)
        if pass1 == pass2:
            userid.set_password(pass1)
            userid.save()
            return HttpResponse('password reset')


    return render(request, "donor_New_password.html")
