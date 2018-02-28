from django.http import HttpResponse
from pip._vendor import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from utils.file import *

User = get_user_model()


class YoutubeBackend:
    ACCESS_TOKEN = settings.YOUTUBE_API_KEY
    URL_SEARCH = 'https://www.googleapis.com/youtube/v3/search'

    def get_search_list(self, request, keyword):
        """
        User access token을 사용해서
        GraphAPI의 'User'항목을 리턴
            (엔드포인트 'me'를 사용해서 access_token에 해당하는 사용자의 정보를 가져옴)
        :param user_access_token: 정보를 가져올 Facebook User access token
        :return: User정보 (dict)
        """
        params = {
            'key': self.ACCESS_TOKEN,
            'q': keyword
        }
        response = requests.get(self.URL_SEARCH, params)
        response_dict = response.json()
        return HttpResponse(str(response_dict))