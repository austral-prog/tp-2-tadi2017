def change():
    expense = 23.75
    money = 100
    x = int(money - expense)
    y = float((money - expense)% 1)
    print("\nVuelto\n")
    print(f"Pesos:\n{x}")
    print(f"Centavos:\n{y}")
change()         
