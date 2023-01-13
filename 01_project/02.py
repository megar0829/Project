text = open('02.txt', 'w', encoding='utf-8')
cnt = 0
with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    for i in f:
        cnt += 1
    text.write(str(cnt))
text.close()