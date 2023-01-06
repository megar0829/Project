text = open('01.txt', 'w', encoding='utf-8')
text.write('Hello, Python! \n')
for i in range(1,6):
    text.write(f'{i}일차 파이썬 공부 중 \n')
text.close()