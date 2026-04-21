from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """
    Разрешение:
    - SAFE_METHODS (GET, HEAD, OPTIONS) - разрешены всем
    - Остальные методы (POST, PUT, PATCH, DELETE) - только автору поста
    """

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Изменение/удаление только автору
        return obj.author == request.user