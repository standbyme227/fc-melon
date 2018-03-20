from django.urls import path, re_path
from . import views

app_name='send'
urlpatterns = [
    path('sms/', views.send_sms, name='send-sms'),
    path('email/', views.send_email, name='send-email'),
]