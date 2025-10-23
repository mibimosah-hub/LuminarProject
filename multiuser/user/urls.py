from django.urls import path
from user import views
app_name = 'user'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('userlogin/',views.UserLogin.as_view(),name='userlogin'),
    path('register',views.Register.as_view(),name='register'),
    # path('logout',views.Logout.as_view(),name='userlogout'),
    path('adminhome/',views.AdminHome.as_view(),name='adminhome'),
    path('studhome/',views.StudentHome.as_view(),name='studenthome'),
    path('teacherhome/',views.TeacherHome.as_view(),name='teacherhome'),

]