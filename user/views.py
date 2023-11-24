from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import User

def create_user(request):
    data = request.POST
    user = User.objects.create(**data)
    return JsonResponse({"user_id": user.id})

def update_user(request, user_id):
    data = request.POST
    user = get_object_or_404(User, pk=user_id)
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    return JsonResponse({"message": "User updated successfully"})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return JsonResponse({"message": "User deleted successfully"})
