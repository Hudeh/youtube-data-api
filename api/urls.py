from django.urls import path
from .views import VideoDetailsView, VideoCommentsView

urlpatterns = [
    path('video/<str:video_id>/', VideoDetailsView.as_view(), name='video-details'),
    path('video/<str:video_id>/comments/', VideoCommentsView.as_view(), name='video-comments'),
]