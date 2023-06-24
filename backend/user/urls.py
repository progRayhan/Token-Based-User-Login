from django.urls import path

from user.views.user_registration import UserRegistrationView

urlpatterns = [
    path(
        route='user/register/',
        view=UserRegistrationView.as_view(),
        name='user_registration',
    ),
]
