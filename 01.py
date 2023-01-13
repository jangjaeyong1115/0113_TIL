import requests


def popular_count():
    pass 
    URL = 'https://developers.themoviedb.org/3/movies/get-popular-movies'
    path = '/movie/popular' 
    params = { # 그 문서에서 필요한 params 정의
    'api_key' : '5d9d597f46961a62aee90494173251b4',
    'language' : 'ko-KR',
    'region' : 'KR',
    }

    response = requests.get(URL+path,params=params).json()
    print(response)
    print(response.get('results')[0])

    
    # 여기에 코드를 작성합니다.  



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
