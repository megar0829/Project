import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
l = list(movie.items())
# del l[0], l[1], l[2], l[3]
# del l[0], l[1]
movie_l = ["('id', 278)", "('title', '쇼생크 탈출')", "('vote_average', 8.7)", "('overview', '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...')", "('genre_ids', [18, 80])"]
movie_d = dict(movie_l)
print(movie_d)
# movie_t = tuple(movie_l)
# movie_d = {movie_t[0], movie_t[1], movie_t[2], movie_t[3], movie_t[4]}

# print(type(movie_d))
# pprint(movie_d)
# movie_list = dict(movie_l)
# # pprint(movie)
# pprint(l)
# pprint(movie_list)

