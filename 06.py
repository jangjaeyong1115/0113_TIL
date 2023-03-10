import requests
from pprint import pprint


def credits(title):
    pass
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

def search_movie(title):
    base_url = 'https://api.themoviedb.org/3'
    sort = '/search/movie'
    keywords = {
        'api_key': '5d9d597f46961a62aee90494173251b4',
        'language': 'ko-KR',
        'query' : title,
        'region': 'KR'
    }
    print(parse.quote(title))
    source = requests.get(base_url + sort, params= keywords).json()
    return source