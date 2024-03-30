groceries = []
printed = []
while True:
    try:
        x = input("")
        groceries.append(x)
    except EOFError:
        print()
        groceries = sorted(groceries)
        for item in groceries:
            if item not in printed:
                printed.append(item)
                print(groceries.count(item), item.upper())

        break

