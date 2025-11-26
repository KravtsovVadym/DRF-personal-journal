from rest_framework import viewsets, permissions, filters 
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Tag, Entry
from .serializers import TagSerializer, EntrySerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
