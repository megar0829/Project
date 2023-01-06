import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
import collections
from collections import OrderedDict
od = collections.OrderedDict()
od = movie
l = list(od.items())
movie_l = [l[3], l[10], l[12], l[6], l[2]]
movie_list = dict(movie_l)
pprint(movie_l)
pprint(movie)
pprint(movie_list)