from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import AddPostView

router = DefaultRouter()
router.register('', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
    path('addpost', AddPostView.as_view())

]