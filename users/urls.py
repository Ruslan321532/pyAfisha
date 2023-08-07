from . import views
from django.urls import path

urlpatterns = [
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('registration/', views.RegistrationAPIView.as_view()),
    path('confirm/', views.UserConfirmationAPIView.as_view(), name='user_confirmation'),
]

# urlpatterns = [
#     path('authorization/', views.authorization_api_view),
#     path('registration/', views.registration_api_view),
#     path('confirm/', views.user_confirmation_api_view, name='user_confirmation'),
# ]