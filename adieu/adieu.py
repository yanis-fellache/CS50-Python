import inflect

inf = inflect.engine()

namelst = []

while True:
    try:
        name = input("Name: ")
        namelst.append(name)
    except EOFError:
        break

print("Adieu, adieu, to", inf.join(namelst))

