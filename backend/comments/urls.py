from django.urls import path
from .views import CommentViewSet

urlpatterns = [
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
]
