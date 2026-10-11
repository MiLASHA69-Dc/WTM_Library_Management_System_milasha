from django.urls import path
from .views import registration_view,login_view,logout_view

app_name = 'accounts'
urlpatterns = [
    path("registration-page/",registration_view,name="register"),
    path("login-page/",login_view,name="login"),
    path("logout/",logout_view,name='logout'),
    
]