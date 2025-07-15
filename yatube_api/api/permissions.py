from rest_framework import permissions


class IsAuthenticatedAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Разрешение, которое:
    - разрешает безопасные методы (GET, HEAD, OPTIONS) для всех,
    - для небезопасных требует аутентификацию,
    - а для операций с конкретным объектом проверяет, является ли пользователь
    автором.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
