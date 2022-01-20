from api.views import (CommentViewSet, FollowViewSet, PostViewSet,
                       ReadOnlyGroupViewSet)
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/groups', ReadOnlyGroupViewSet, basename='groups')
router.register(r'v1/follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
