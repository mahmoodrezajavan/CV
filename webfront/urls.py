from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Filelist/', views.Filelist, name='Filelist'),
    path('YaraEditor/<int:taskID>/', views.YaraEditor, name='YaraEditor'),
    path('Report/<int:taskID>/', views.Report, name='Report'),
    path('ProfileEditor/', views.ProfileEditor, name='ProfileEditor'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
    path('Logout/', views.Logout, name='Logout'),
    path('DeleteAccount/', views.DeleteAccount, name='DeleteAccount'),
    path('about/', views.about, name='about')
]