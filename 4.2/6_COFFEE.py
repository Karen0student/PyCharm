in_stock = {"coffee": 1, "milk": 2, "cream": 3}


def order(*menu):
    recipes = {
        "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
        "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
        "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
        "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
    }
    for coffee in menu:
        if (
            in_stock["coffee"] >= recipes[coffee]["coffee"]
            and in_stock["milk"] >= recipes[coffee]["milk"]
            and in_stock["cream"] >= recipes[coffee]["cream"]
        ):
            in_stock["coffee"] -= recipes[coffee]["coffee"]
            in_stock["milk"] -= recipes[coffee]["milk"]
            in_stock["cream"] -= recipes[coffee]["cream"]
            return coffee

    return "К сожалению, не можем предложить Вам напиток"


print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
