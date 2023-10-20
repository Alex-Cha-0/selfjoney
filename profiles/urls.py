from django.urls import path
from .views import my_profile_view, update_my_profile_view

app_name = 'profiles'


urlpatterns = [
    path('myprofile/<int:profile_id>/', my_profile_view, name='my-profile-view'),
    path('update_my_profile/', update_my_profile_view, name='update-my-profile')
]

