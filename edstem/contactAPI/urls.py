from django.urls import path
from . import views

urlpatterns = [
    
    path('groups/owners/', views.UserGroupOwner.as_view(
        group_name='owner'), name='owner-group-management'),
]
