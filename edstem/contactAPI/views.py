from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework import generics, permissions, views, status, response, filters
from .permissions import IsOwner
# Create your views here.


class UserGroupManagement(views.APIView):
    group_name = None

    def get(self, request, *args, **kwargs):
        if not IsOwner().has_permission(request, self):
            return response.Response(status=status.HTTP_403_FORBIDDEN)
        
        if 'user_id' in kwargs:
            return self.delete(request, kwargs['user_id'])

        group = get_object_or_404(Group, name=self.group_name)
        users = group.user_set.all()
        user_data = [{'id': user.id, 'username': user.username}
                     for user in users]
        return response.Response(user_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if not IsOwner().has_permission(request, self):
            return response.Response(status=status.HTTP_403_FORBIDDEN)

        user_id = request.data.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        group = Group.objects.get_or_create(name=self.group_name)[0]
        group.user_set.add(user)
        return response.Response(status=status.HTTP_201_CREATED)

    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return response.Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        group = get_object_or_404(Group, name=self.group_name)
        group.user_set.remove(user)
        return response.Response(status=status.HTTP_200_OK)

