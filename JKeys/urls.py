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

    # Link to Home Page (Listview), called "home" in buttons
    # Pattern : url
    path('logins/', views.LoginHome.as_view(), name="loginhome"),

    # Link to Home Page (Listview), called "home" in buttons
    # Pattern : url
    path('idcards/', views.IDCardHomePage.as_view(), name="idcardhome"),

    # Link to Home Page (Listview), called "home" in buttons
    # Pattern : url
    path('creditcards/', views.CreditCardHome.as_view(), name="creditcardhome"),




    ############### IDs ###############

    # Link to Create Page (Createview), called "createelement" in buttons
    # Pattern : url/id/create
    path('logins/create', views.CreateLogin.as_view(), name="createlogin"),

    # Link to Details Page (Detailsview), called "element" in buttons
    # Pattern : url/id
    path('logins/<int:pk>', views.LoginPage.as_view(), name="loginpage"),

    # Link to Edit Page (Updateview), called "elementedit" in buttons
    # Pattern : url/id/edit
    path('logins/<int:pk>/edit', views.EditLogin.as_view(), name="editlogin"),

    # Link to Delete Page (Deleteview), called "elementdelete" in buttons
    # Pattern : url/id/delete
    path('logins/<int:pk>/delete', views.DeleteLogin.as_view(), name="deletelogin"),




    ############### IDCards ###############

    # Link to Create Page (Createview), called "createelement" in buttons
    # Pattern : url/id/create
    path('idcards/create', views.CreateIDCard.as_view(), name="createidcard"),

    # Link to Details Page (Detailsview), called "element" in buttons
    # Pattern : url/id
    path('idcards/<int:pk>', views.IDCardPage.as_view(), name="idcardpage"),

    # Link to Edit Page (Updateview), called "elementedit" in buttons
    # Pattern : url/id/edit
    path('idcards/<int:pk>/edit', views.EditIDCard.as_view(), name="editidcard"),

    # Link to Delete Page (Deleteview), called "elementdelete" in buttons
    # Pattern : url/id/delete
    path('idcards/<int:pk>/delete', views.DeleteIDCard.as_view(), name="deleteidcard"),




    ############### CreditCards ###############

    # Link to Create Page (Createview), called "createelement" in buttons
    # Pattern : url/id/create
    path('creditcards/create', views.CreateCreditCard.as_view(), name="createcreditcard"),

    # Link to Details Page (Detailsview), called "element" in buttons
    # Pattern : url/id
    path('creditcards/<int:pk>', views.CreditCardPage.as_view(), name="creditcardpage"),

    # Link to Edit Page (Updateview), called "elementedit" in buttons
    # Pattern : url/id/edit
    path('creditcards/<int:pk>/edit', views.EditCreditCard.as_view(), name="editcreditcard"),

    # Link to Delete Page (Deleteview), called "elementdelete" in buttons
    # Pattern : url/id/delete
    path('creditcards/<int:pk>/delete', views.DeleteCreditCard.as_view(), name="deletecreditcard"),




    ############### ACCOUNTS ###############

    # Link to Login Page
    # Pattern : url/login
    path("accounts/", include("account.urls")),

    # Link to Signup Page
    # Pattern : url/signup
    path("accounts/", include("django.contrib.auth.urls")),

    # Default admin page
    # Pattern : url/admin
    path('admin/', admin.site.urls),
]
