from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeView.as_view(), name='password_change_form'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
