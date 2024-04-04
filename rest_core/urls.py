from django.urls import include, path
from . import views

urlpatterns = [
    path('getFilelist/', views.getFilelist, name='getFilelist'),
    path('CreateTask/', views.CreateTask, name='CreateTask'),
    path('Report/<int:taskID>/', views.Report, name='Report'),
    path('Status/<int:taskID>/', views.Status, name='Status'),
    path('Delete/<int:taskID>/', views.Delete, name='Delete'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
    path('Logout/', views.Logout, name='Logout'),
    path('DeleteAccount/', views.DeleteAccount, name='DeleteAccount'),
    path('YaraMatch/<int:taskID>/', views.YaraMatch, name='YaraMatch'),
    path('EmailChange/', views.EmailChange, name='EmailChange'),
    path('PasswordChange/', views.PasswordChange, name='PasswordChange'),
    path('getProfile/', views.getProfile, name='getProfile')
]