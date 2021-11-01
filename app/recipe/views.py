from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag

from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)

    # garantee that the user is logged in
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        # References to the queryset on line 16
        # We can call the 'self.request.user'
        # Because we have informed on line 15 that is necessary
        # that the user is authenticated
        # if the user got this fat, it means that is okay
        return self.queryset.filter(user=self.request.user).order_by('-name')
