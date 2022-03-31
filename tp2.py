per_cent={}
money=int(input("Введите сумму:"))
per_cent['ТКБ']=float(input("Введите ставку в банке ТБК:"))
per_cent['СКБ']=float(input("Введите ставку в банке СКБ:"))
per_cent['ВТБ']=float(input("Введите ставку в банке ВТБ:"))
per_cent['СБЕР']=float(input("Введите ставку в банке СБЕР:"))
tbk=round(money*(per_cent['ТКБ']/100))
skb=round(money*(per_cent['СКБ']/100))
vtb=round(money*(per_cent['ВТБ']/100))
sber=round(money*per_cent['СБЕР']/100)
deposit=[tbk,skb,vtb,sber]
max_i=max(deposit)
stavka=round(max_i/money*100,1)
list_key=list(per_cent.keys())
list_val=list(per_cent.values())
bank=list_key[list_val.index(stavka)]
print("Максимальная сумма, которую вы можете заработать — ",max_i, "в банке",bank)

