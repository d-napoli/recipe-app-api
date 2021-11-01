from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


# Create the default router
# it's going to be responsible for creating
# a lot of dynamic url's
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
