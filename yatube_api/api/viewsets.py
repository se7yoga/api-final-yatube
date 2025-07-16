from rest_framework import mixins, viewsets


class ListCreateViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """Базовый кастомный вьюсет: только GET (list) и POST (create)."""
    pass
