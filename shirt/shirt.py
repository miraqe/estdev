import sys
import os
from PIL import Image, ImageOps

# Ensure correct usage
if len(sys.argv) != 3:
    sys.exit("Too few command-line arguments")

# Ensure correct input and output file extensions
input_name, input_extension = os.path.splitext(sys.argv[1])
output_name, output_extension = os.path.splitext(sys.argv[2])
if input_extension.lower() not in ['.jpg', '.jpeg', '.png'] or output_extension.lower() not in ['.jpg', '.jpeg', '.png']:
    sys.exit("Invalid format")

# Ensure input and output have same extension
if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

# Ensure input file exists
if not os.path.isfile(sys.argv[1]):
    sys.exit("Input does not exist")

# Open input image
input_image = Image.open(sys.argv[1])

# Open shirt image
shirt_image = Image.open("shirt.png")

# Resize and crop input image to match size of shirt image
input_image = ImageOps.fit(input_image, shirt_image.size)

# Overlay shirt image on input image
input_image.paste(shirt_image, (0, 0), shirt_image)

# Save result as output image
input_image.save(sys.argv[2])
