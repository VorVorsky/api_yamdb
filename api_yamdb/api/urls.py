from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (register_or_confirm_code, get_token,
                    UserEditViewSet, ReviewViewSet, CommentsViewSet,
                    CategoryViewSet, GenreViewSet, TitleViewSet)


router_v1 = DefaultRouter()
router_v1.register(r'users', UserEditViewSet, basename='users')
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router_v1.urls), name='review-api'),
    path('v1/auth/signup/', register_or_confirm_code, name='register_or_code'),
    path('v1/auth/token/', get_token, name='get_token'),
]
