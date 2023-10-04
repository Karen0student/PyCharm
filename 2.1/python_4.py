fruit_kg = 2.5
price_kg = 38
final_price = price_kg * fruit_kg
#print(type(final_price))
money = input()
money = int(money)
if money > final_price:
    change = money - final_price
    print(int(change))
else:
    print('not enough money')
