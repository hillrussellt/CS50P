import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
random.seed()

if len(sys.argv) >= 4:
    sys.exit("Only accepts two arguments")


elif len(sys.argv) == 2:
    sys.exit("Please provide two arguments")


elif len(sys.argv) == 1:
    input = input("Give me a text string to convert, please! ")
    fonts = figlet.getFonts()
    random_font_value = random.randrange(0, len(fonts))
    try:
        figlet.setFont(font=fonts[random_font_value])
    except Exception:
        print("Invalid Usage")
        sys.exit()
    print(figlet.renderText(input))


elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    input = input("Give me a text string to convert, please! ")
    selected_font = sys.argv[2]
    try:
        figlet.setFont(font=selected_font)
    except Exception:
        print("Invalid Usage")
        sys.exit()
    print(figlet.renderText(input))


else:
    print("Invalid Usage")
