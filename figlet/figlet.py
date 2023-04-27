import sys
import random
from pyfiglet import Figlet

def print_usage():
    print("Usage: figlet.py [-f FONT] [TEXT]")
    sys.exit()

# Parse command-line arguments
if len(sys.argv) == 1:
    font_name = random.choice(Figlet().getFonts())
    text = input("Enter text: ")
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    font_name = sys.argv[2]
    text = input("Enter text: ")
else:
    print_usage()

# Check if font is valid
if font_name not in Figlet().getFonts():
    print("Invalid usage")
    sys.exit

# Print text in chosen font
figlet = Figlet(font=font_name)
print(figlet.renderText(text))