import requests
from pprint import pprint


def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'query': title,
        'api_key': '855cdae49d8da0101980231b1b06ce28',
        'languge': 'ko-KR',
        'region': 'KR'
    }
    response = requests.get(url, params=params).json()
    details = response.get('results', None)
    return details['id']
       

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
