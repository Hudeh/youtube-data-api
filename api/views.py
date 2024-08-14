import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .youtube_service import YouTubeService

class VideoDetailsView(APIView):
    def get(self, request, video_id):
        youtube_service = YouTubeService()
        try:
            data = youtube_service.get_video_details(video_id)
            if not data['items']:
                raise NotFound("Video not found")
            video_details = data['items'][0]['snippet']
            statistics = data['items'][0]['statistics']
            response_data = {
                'title': video_details['title'],
                'description': video_details['description'],
                'view_count': statistics.get('viewCount'),
                'like_count': statistics.get('likeCount'),
            }
            return Response(response_data)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=500)

class VideoCommentsView(APIView):
    def get(self, request, video_id):
        youtube_service = YouTubeService()
        comments = []
        page_token = request.query_params.get('pageToken')
        try:
            while True:
                data = youtube_service.get_video_comments(video_id, page_token)
                for item in data['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    comments.append(comment)
                page_token = data.get('nextPageToken')
                if not page_token:
                    break
            return Response({'comments': comments})
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=500)
