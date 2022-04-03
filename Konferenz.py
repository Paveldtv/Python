ticked=abs(int(input('Введите количество билетов - ')))
print('----------------------------------')
age=[]
sum=0
for i in range(0,ticked):
    age.append(abs(int(input(f'Введите возраст {i+1} билета - '))))
    if 18<=age[i]<25:
        sum+=990
    elif age[i]>=25:
        sum+=1390
print('----------------------------------')
if sum==0:
    print(f'Для Вас проход бесплатный.')
else:
    if ticked>3:
        sum*=0.9
        sale=round(sum-(sum*0.9),2)
        print(f'Вы купили {ticked} билета(ов), общая стоимость билетов-{sum} руб., cкидка составила-{sale} руб.')
    else:
        print(f'Вы купили билетов {ticked}, общая стоимость билетов-{sum} руб.')