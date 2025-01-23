
from django.urls import path
from .views import *
# from app import views

urlpatterns = [
    path("", index, name="index"),
    path("gallery/", gallery, name="gallery"),
    path("login-admin/", login_admin, name="login_admin"),
    path("login-donor/", login_donor, name="login_donor"),
    path("login-volunteer/", login_volunteer, name="login_volunteer"),
    path("signup-donor/", signup_donor, name="signup_donor"),
    path("signup-volunteer/", signup_volunteer, name="signup_volunteer"),
    path("index-admin/", index_admin, name="index_admin"),
    # admin dashboard
    path("pending-donation/", pending_donation, name="pending_donation"),
    path("accepted-donation/", accepted_donation, name="accepted_donation"),
    path("rejected-donation/", rejected_donation, name="rejected_donation"),
    path(
        "volunteerallocated-donation/",
        volunteerallocated_donation,
        name="volunteerallocated_donation",
    ),
    path("donationrec-admin/", donationrec_admin, name="donationrec_admin"),
    path(
        "donationnotrec-admin/", donationnotrec_admin, name="donationnotrec_admin"
    ),
    path(
        "donationdelivered-admin/",
        donationdelivered_admin,
        name="donationdelivered_admin",
    ),
    path("all-donations/", all_donations, name="all_donations"),
    path("manage-donor/", manage_donor, name="manage_donor"),
    path("new-volunteer/", new_volunteer, name="new_volunteer"),
    path("accepted-volunteer/", accepted_volunteer, name="accepted_volunteer"),
    path("rejected-volunteer/", rejected_volunteer, name="rejected_volunteer"),
    path("all-volunteer/", all_volunteer, name="all_volunteer"),
    path("add-area/", add_area, name="add_area"),
    path("edit-area/<int:pid>", edit_area, name="edit_area"),
    path("manage-area/", manage_area, name="manage_area"),
    path("changepwd-admin/", changepwd_admin, name="changepwd_admin"),
    path("logout/", logout_user, name="logout"),
    # view details
    path(
        "accepted-donationdetail/<int:pid>",
        accepted_donationdetail,
        name="accepted_donationdetail",
    ),
    path(
        "view-volunteerdetail/<int:pid>",
        view_volunteerdetail,
        name="view_volunteerdetail",
    ),
    path("view-donordetail/<int:pid>", view_donordetail, name="view_donordetail"),
    path(
        "view-donationdetail/<int:pid>",
        view_donationdetail,
        name="view_donationdetail",
    ),
    # donar dashboard
    path("index-donor/", index_donor, name="index_donor"),
    path("donate-now/", donate_now, name="donate_now"),
    path("donation-history/", donation_history, name="donation_history"),
    path("profile-donor/", profile_donor, name="profile_donor"),
    path("changepwd-donor/", changepwd_donor, name="changepwd_donor"),
    # volunteer dashboard
    path("index-volunteer/", index_volunteer, name="index_volunteer"),
    path("collection-req/", collection_req, name="collection_req"),
    path(
        "donationrec-volunteer/",
        donationrec_volunteer,
        name="donationrec_volunteer",
    ),
    path(
        "donationnotrec-volunteer/",
        donationnotrec_volunteer,
        name="donationnotrec_volunteer",
    ),
    path(
        "donationdelivered-volunteer/",
        donationdelivered_volunteer,
        name="donationdelivered_volunteer",
    ),
    path("profile-volunteer/", profile_volunteer, name="profile_volunteer"),
    path("changepwd-volunteer/", changepwd_volunteer, name="changepwd_volunteer"),
    # vew details
    path(
        "donationdetail-donor/<int:pid>",
        donationdetail_donor,
        name="donationdetail_donor",
    ),
    path(
        "donationrec-detail/<int:pid>",
        donationrec_detail,
        name="donationrec_detail",
    ),
    path(
        "donationcollection-detail/<int:pid>",
        donationcollection_detail,
        name="donationcollection_detail",
    ),
    path("delete_donation/<int:pid>/", delete_donation, name='delete_donation'),
    path("delete_volunteer/<int:pid>/", delete_volunteer, name='delete_volunteer'),
    path("delete_area/<int:pid>/", delete_area, name='delete_area'),
    path("delete_donor/<int:pid>/", delete_donor, name='delete_donor'),
    
    path("Forgetpassword/", Forgetpassword, name="Forget_password"),
    path("NewPasswordPage/<str:user>/", NewPasswordPage, name="New_Password"),
]
