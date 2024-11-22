# pixel_pretender/__init__.py

# Metadata about the package
__version__ = "1.0.0"
__author__ = "Anasse Gassab"

#  ____ Importing key public functions from submodules ____  #

# Importing functions for pixel management
from .pixel_pretender import max_display_capacity, set_max_pixels

# Importing functions for text transformation and display 
from .pixel_pretender import digitise, display_pixels

# Importing functions for color application
from .pixel_pretender import apply_colorama_color, apply_rich_color

# Importing functions for user experiments and samples
from .pixel_pretender import try_pixel_samples, try_cool_pixels, try_rich_colors

# Importing constants
from .pixel_pretender import colorama_colors, rich_colors, pixel_samples, cool_pixel_samples

# Defining the public API
__all__ = [
    "max_display_capacity",  # Determine the maximum number of pixel characters your screen can display.
    "set_max_pixels",        # Sets the maximum number of pixel characters to display per line.

    "digitise",              # function to Transform text into its pixelated form
    "display_pixels",        # Displays the pixelated output in the terminal

    "apply_colorama_color",  # Applies color formatting using the `colorama` library.
    "apply_rich_color",      # Applies color formatting using the `rich` library for enhanced terminal output.

    "try_pixel_samples",     # Displays a message in a variety of pixel samples for users to explore.
    "try_cool_pixels",       # Displays a message in a variety of cool pixel samples for users to explore.
    "try_rich_colors",       # Displays a message in 255 different colors using the `rich` library.

    "colorama_colors", # A tuple of all color names available in Colorama, allowing you to easily apply colors to your pixel text.
    "rich_colors", # A tuple containing 16 color names available in the Rich library for quick access and application to your pixel text.
    "pixel_samples",  # A list of Unicode symbols that can be used as pixel characters, ensuring compatibility across various terminals.
    "cool_pixel_samples", # A curated list of Unicode symbols that are visually appealing and work well as pixel characters.
]

# ENJOY :)