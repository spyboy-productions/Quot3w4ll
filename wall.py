import os
import random
import csv
from PIL import Image, ImageDraw, ImageFont
import ctypes

# Configuration
LOCAL_QUOTE_FILE = "quotes.csv"  # Local quotes file
WALLPAPER_PATH = os.path.expanduser("~\\AppData\\Local\\Temp\\wallpaper.bmp")
FONT_PATH = "Helvetica.ttf" 

QUOTE_FONT_SIZE = 40
AUTHOR_FONT_SIZE = 24
MARGIN = 50

def fetch_random_quote():
    # Load quotes from the local CSV file
    with open(LOCAL_QUOTE_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        quotes = list(reader)
    return random.choice(quotes)

def get_screen_resolution():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def create_wallpaper(quote, author):
    global QUOTE_FONT_SIZE
    
    width, height = get_screen_resolution()

    img = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(img)

    
    quote_font = ImageFont.truetype(FONT_PATH, QUOTE_FONT_SIZE)
    author_font = ImageFont.truetype(FONT_PATH, AUTHOR_FONT_SIZE)

    quote_text = f'"{quote}"'
    author_text = f"— {author}"

    quote_width, quote_height = draw.textbbox((0, 0), quote_text, font=quote_font)[2:]
    author_width, author_height = draw.textbbox((0, 0), author_text, font=author_font)[2:]

    # Adjust quote width if it exceeds screen width
    if quote_width + 2 * MARGIN > width:
        # Reduce font size until it fits
        while quote_width + 2 * MARGIN > width:
            QUOTE_FONT_SIZE -= 2
            quote_font = ImageFont.truetype(FONT_PATH, QUOTE_FONT_SIZE)
            quote_width, quote_height = draw.textbbox((0, 0), quote_text, font=quote_font)[2:]

    # centered positions with margins
    quote_position = ((width - quote_width) // 2, (height - quote_height) // 2)
    author_position = ((width - author_width) // 2, quote_position[1] + quote_height + MARGIN)

    # Draw text
    draw.text(quote_position, quote_text, font=quote_font, fill="white")
    draw.text(author_position, author_text, font=author_font, fill="grey")

    # Save wallpaper
    img.save(WALLPAPER_PATH)

def set_wallpaper():
    # Updating registry key for wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

if __name__ == "__main__":
    random_quote = fetch_random_quote()
    create_wallpaper(random_quote["Quote"], random_quote["Author"])
    set_wallpaper()
