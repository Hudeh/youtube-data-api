import requests
from django.conf import settings

class YouTubeService:
    BASE_URL = "https://www.googleapis.com/youtube/v3"

    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY

    def get_video_details(self, video_id):
        url = f"{self.BASE_URL}/videos"
        params = {
            'part': 'snippet,statistics',
            'id': video_id,
            'key': self.api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_video_comments(self, video_id, page_token=None):
        url = f"{self.BASE_URL}/commentThreads"
        params = {
            'part': 'snippet',
            'videoId': video_id,
            'key': self.api_key,
            'pageToken': page_token,
            'maxResults': 100,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()