object_weight = int(input())
object_price = int(input())
client_money = int(input())
final_money = object_price * object_weight
change = client_money - final_money
if change > 0:
    print(change)
else:
    print('not enough money')