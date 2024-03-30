from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    f = sys.argv[2]

    if sys.argv[1] == "--font":
        pass
    elif sys.argv[1] == "-f":
        pass
    else:
        sys.exit("Invalid Usage")
    f = sys.argv[2]

    if f not in fonts:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")



s = input()

figlet.setFont(font=f)

print(figlet.renderText(s))