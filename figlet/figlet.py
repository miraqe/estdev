import sys

from pyfiglet import Figlet

figlet = Figlet()

# Parse command-line arguments
if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
   isRandomFont = False
else:
    sys.exit(1)

# Check if font is valid

figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(msg))
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
msg = input("Input: ")

print(f"Output: {figlet.renderText(msg)}")