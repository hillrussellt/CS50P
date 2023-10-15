import sys
import inflect

p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: "))
    except Exception:
        print("Adieu, aduei, to ", end='' + p.join(names))
        sys.exit()
