from django.urls import path
from .views import create_user, update_user, delete_user

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('update/<int:user_id>/', update_user, name='update_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
