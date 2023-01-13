text = open('04.txt', 'w', encoding='utf-8')
dict_fruit = {}
fruit = []
with open('data/fruits.txt', 'r', encoding='utf-8') as f:
    fruit = f.readlines()
fruit = [line.rstrip('\n') for line in fruit]
for i in fruit:
    if i not in dict_fruit:
        dict_fruit[i] = 1
    else:
        dict_fruit[i] += 1
for key, value in dict_fruit.items():
    text.write(f'{key} {value} \n')
text.close()