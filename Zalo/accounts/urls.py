from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterUserView


# app_name = 'user'

urlpatterns = [
    path('signup/', RegisterUserView.as_view(),
         name=''),
    path('login/', obtain_jwt_token,
         name='login'),

]