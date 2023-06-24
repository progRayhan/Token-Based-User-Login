from django.urls import path

from user.views.user_registration import UserRegistrationView
from user.views.user_login import UserLoginView

urlpatterns = [
    path(
        route='user/register/',
        view=UserRegistrationView.as_view(),
        name='user_registration',
    ),

    path(
        route='user/login/',
        view=UserLoginView.as_view(),
        name='user_login',
    ),
]
