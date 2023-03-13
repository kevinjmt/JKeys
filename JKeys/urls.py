"""JKeys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = 'JKeys'

urlpatterns = [

    ############### HOME PAGES ###############

    # Link to Home Page (Listview), called "home" in buttons
    # Pattern : url
    path('', views.WebSite.as_view(), name="home"),

    # Link to Logins Home Page (Listview), called "loginhome" in buttons
    # Pattern : url/logins
    path('logins/', views.LoginHome.as_view(), name="loginhome"),

    # Link to IDCards Home Page (Listview), called "idcardhome" in buttons
    # Pattern : url/idcards
    path('idcards/', views.IDCardHomePage.as_view(), name="idcardhome"),

    # Link to CreditCards Home Page (Listview), called "creditcardhome" in buttons
    # Pattern : url/creditcards
    path('creditcards/', views.CreditCardHome.as_view(), name="creditcardhome"),




    ############### IDs ###############

    # Link to Logins Create Page (FormView), called "createlogin" in buttons
    # Pattern : url/logins/id/create
    path('logins/create', views.CreateLogin.as_view(), name="createlogin"),

    # Link to Logins Details Page (Detailsview), called "loginpage" in buttons
    # Pattern : url/logins/id
    path('logins/<int:pk>', views.LoginPage.as_view(), name="loginpage"),

    # Link to Logins Edit Page (FormView), called "editlogin" in buttons
    # Pattern : url/logins/id/edit
    path('logins/<int:pk>/edit', views.EditLogin.as_view(), name="editlogin"),

    # Link to Logins Delete Page (Deleteview), called "deletelogin" in buttons
    # Pattern : url/logins/id/delete
    path('logins/<int:pk>/delete', views.DeleteLogin.as_view(), name="deletelogin"),




    ############### IDCards ###############

    # Link to IDCards Create Page (FormView), called "createidcard" in buttons
    # Pattern : url/idcards/id/create
    path('idcards/create', views.CreateIDCard.as_view(), name="createidcard"),

    # Link to IDCards Details Page (Detailsview), called "idcardpage" in buttons
    # Pattern : url/idcards/id
    path('idcards/<int:pk>', views.IDCardPage.as_view(), name="idcardpage"),

    # Link to IDCards Edit Page (FormView), called "editidcard" in buttons
    # Pattern : url/idcards/id/edit
    path('idcards/<int:pk>/edit', views.EditIDCard.as_view(), name="editidcard"),

    # Link to IDCards Delete Page (Deleteview), called "deleteidcard" in buttons
    # Pattern : url/idcards/id/delete
    path('idcards/<int:pk>/delete', views.DeleteIDCard.as_view(), name="deleteidcard"),




    ############### CreditCards ###############

    # Link to CreditCards Create Page (FormView), called "createcreditcard" in buttons
    # Pattern : url/creditcards/id/create
    path('creditcards/create', views.CreateCreditCard.as_view(), name="createcreditcard"),

    # Link to CreditCards Details Page (Detailsview), called "creditcardpage" in buttons
    # Pattern : url/creditcards/id
    path('creditcards/<int:pk>', views.CreditCardPage.as_view(), name="creditcardpage"),

    # Link to CreditCards Edit Page (FormView), called "editcreditcard" in buttons
    # Pattern : url/creditcards/id/edit
    path('creditcards/<int:pk>/edit', views.EditCreditCard.as_view(), name="editcreditcard"),

    # Link to CreditCards Delete Page (Deleteview), called "deletecreditcard" in buttons
    # Pattern : url/creditcards/id/delete
    path('creditcards/<int:pk>/delete', views.DeleteCreditCard.as_view(), name="deletecreditcard"),




    ############### ACCOUNTS ###############

    # Link to Login Page
    # Pattern : url/accounts/login
    path("accounts/", include("account.urls")),

    # Link to Signup Page
    # Pattern : url/accounts/signup
    path("accounts/", include("django.contrib.auth.urls")),

    # Default admin page
    # Pattern : url/admin
    path('admin/', admin.site.urls),
]
