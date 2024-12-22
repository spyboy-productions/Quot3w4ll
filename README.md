# Quot3w4ll - Random Quote Wallpaper Tool

Quot3w4ll is a simple tool that changes your desktop wallpaper to display a random quote on a black background with white text. Quotes are fetched from a `quote.txt` file hosted in a GitHub repository. This tool is designed for Windows systems.

## Requirements

- **Python**
- **Pillow (PIL)**

To install Pillow, run:
```bash
pip install pillow
```

## Usage

### Manual Wallpaper Change
To change the wallpaper manually, run:
```bash
Quot3w4ll.bat
```

### Automatic Wallpaper Change on Startup
To enable the tool to automatically change your wallpaper every time Windows starts:
1. Run:
   ```bash
   enable_startup.bat
   ```
2. This will set up the tool to execute at every startup.

## How It Works
1. A random quote is selected from the `quotes.csv` file in the GitHub repository.
2. The tool generates an image with a black background and white text displaying the selected quote.
3. The generated image is set as your desktop wallpaper.

## Notes
- Ensure Python is added to your system PATH.
- If the tool does not work as expected, check your internet connection and the configuration of the startup task.

Enjoy a new inspirational quote every time you start your computer!

