text = open('03.txt', 'w', encoding='utf-8')
cnt = 0
f_list = []
with open('data/fruits.txt', 'r', encoding = 'utf-8') as f:
    fruit = f.readlines()
fruit = [line.rstrip('\n') for line in fruit]
for i in fruit:
    if i.endswith('berry') == True:
        f_list.append(i)
f_list_1 = []
for i in f_list:
    if i not in  f_list_1:
        f_list_1.append(i)
        cnt += 1
    else:
        continue
           
text.write(f'{str(cnt)} \n')
for i in f_list_1:
    text.write(f'{i} \n')
text.close()