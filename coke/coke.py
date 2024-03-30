amountDue = 50
while amountDue > 0:
    print("Amount Due:", amountDue)
    money = int(input("Insert Coin: "))
    if money == 25 or money == 10 or money == 5:
        amountDue = amountDue - money
if amountDue <= 0:
    change = amountDue * -1
    print("Change Owed:", change)