from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Load the image
image_path = r"filepath and name.png"
image = Image.open(image_path)

# Extract EXIF data
exif_data = image._getexif()

# Function to get EXIF data in human-readable form
def get_exif_data(exif):
    exif_table = {}
    for tag, value in exif.items():
        tag_name = TAGS.get(tag, tag)
        exif_table[tag_name] = value
    return exif_table

# Extract and display the EXIF data
exif_table = get_exif_data(exif_data) if exif_data else "No EXIF data found"
exif_table
