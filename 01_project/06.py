import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
movie_list = {}
title = ["id", "title", "poster_path", "vote_average", "overview", "genre_ids"]
movie = []

movie.append(movie_list)
print(movie,id(movie[0]))

for i in title:
    movie_list[i] = movies_list[0][i]

print(movie,id(movie[0]))

for i in title:
    movie_list[i] = movie_list[1][i]

print(movie,id(movie[0]))



# value_list = [
#     {"key1": "value1", "key2": "value2"},
#     {"key1": "value3", "key2": "value4"},
# ]
# key_list = ["key1", "key2"]
# dict_variable = {}
# dict_list = []

# dict_list.append(dict_variable)
# print(dict_list)

# for key in key_list:
#     dict_variable[key] = value_list[0][key]

# print(dict_list)

# for key in key_list:
#     dict_variable[key] = value_list[1][key]

# print(dict_list)