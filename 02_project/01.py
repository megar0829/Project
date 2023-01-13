import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key': '855cdae49d8da0101980231b1b06ce28',
        'languge': 'ko-KR',
        'region': 'KR'
    }
    response= requests.get(url, params=params).json()
    return len(response['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
