# Pixel Pretender

**A Python package for rendering pixelated text in the console, with customizable ASCII and Unicode\* symbols and optional color formatting.**

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Support Functions](#support-functions) 
- [Help](#need-help-with-a-specific-function)
- [Notes](#notes)
- [Contributing](#contributing)
- [Author](#author)
- [Licenses](#licenses)
- [Acknowledgements](#acknowledgements)

## Features
- **Transform** text into pixelated representations using customizable symbols.
- Enhance color customization with **rich and colorama libraries**.
- **Simple functions for rendering and displaying pixel text with style.**
- **User friendly API**

## Installation

- To install the latest version of `pixel_pretender`, run:

```bash
pip install pixel-pretender
```

## Usage
- - adjust maximum number of pixel characters to display to your screen 

```python
import pixel_pretender as pxp 

# Determine the maximum number of pixel characters your screen can display.
pxp.max_display_capacity()

# Set the maximum number of pixel characters to display per line.
pxp.set_max_pixels(20)
```

- - using `pxp.digitise()` function to Transform text into its pixelated form.
```python
import pixel_pretender as pxp 
# Text to be pixelated
text = "hello world"

# Convert text to pixels.
pixels = pxp.digitise(text, symbol='█')

# Display the pixelated text.
pxp.display_pixels(pixels)
```

![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/92335f57a2a4d14473159a71421f93b9102ec665/Docs/digitise_output.png)

- - Use the `pxp.digitise()` function with the `negative_image=True` option to invert the image, swapping whitespace with the symbol.
```python
import pixel_pretender as pxp 

# Text to be pixelated
text = "hello world"
# Generate a negative image of the pixelated text.
pixels = pxp.digitise(text, symbol='█', negative_image=True)

# Display the negative image.
pxp.display_pixels(pixels)
```

**Pixelated text output with** `negative_image=True`

![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/92335f57a2a4d14473159a71421f93b9102ec665/Docs/digitise_negative_True.png)


### Colorama Color Function:
**Apply 16 standard colors to your pixel characters using colorama.**

The following colors are available:

+ *'red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'black', 'white'*
+ *'light red', 'light yellow', 'light green', 'light blue', 'light cyan', 'light magenta', 'light black', 'light white'*

```python
import pixel_pretender as pxp 

# Transform text into its pixelated form
pixels = pxp.digitise("> python 3.8 <", symbol='▄')

# Apply a color to the pixel characters using colorama (16 available colors).
colorama_pixels = pxp.apply_colorama_color(pixels, "yellow")

# Display the colorized pixel text.
pxp.display_pixels(colorama_pixels)
```
![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/apply_colorama_color.png)


### Applying Colorama Colors in a Loop:

**Apply multiple colors to the same pixel text in sequence.**

```python
import pixel_pretender as pxp

# Transform text into its pixelated form
pixels = pxp.digitise("21:30", symbol='┇')

# Tuple containing all available colorama color names.
colors = pxp.colorama_colors

# Loop through colors and apply each to the pixel text.
for color in colors:
    # Apply the current color to the pixel characters.
    colorama_pixels = pxp.apply_colorama_color(pixels, color)
    
    # Display the pixel text with the applied color.
    pxp.display_pixels(colorama_pixels)
```
![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/colorama_normal_colors.png
)
![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/colorama_light_colors.png
)

### Rich Color Function

**The Rich color library provides advanced coloring options that you can apply to customize your pixel characters.**

- **Without Background**

```python
import pixel_pretender as pxp 

# Generate pixel list 
pixels = pxp.digitise("pixel pretender", symbol='▓')

# Apply Rich color: True Color, 256 Colors, Basic Colors
rich_pixels = pxp.apply_rich_color(pixels, text_color="#ffff87")  # Note: PyCharm users should run their script in the terminal to view Rich colors

# Display the result 
pxp.display_pixels(rich_pixels)
```
![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/apply_rich_color.png)

- **With Background**
```python
import pixel_pretender as pxp 

# Generate pixel list 
pixels = pxp.digitise("pixel pretender", symbol='▓')

# Apply Rich color with background: True Color, 256 Colors, Basic Colors
rich_pixels = pxp.apply_rich_color(pixels, text_color="#ffff87", background_color="color(4)")  # Note: PyCharm users should run their script in the terminal to view Rich colors

# Display the result 
pxp.display_pixels(rich_pixels)
```
![Example Output](https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/rich_color_with_background.png)

## Support Functions

<details>
    <summary><b><code> max_display_capacity() </code></b></summary>

<i>Determines the maximum number of pixel characters your screen can display and helps you optimize the display settings for your pixelated text.
</i>

```python
import pixel_pretender as pxp 

# Check the maximum display capacity for your screen.
pxp.max_display_capacity()
```
</details>

<details> 
    <summary><b><code> set_max_pixels() </code></b></summary> 
<i><br>Allows you to customize the number of pixel characters displayed per line by setting a positive integer value. This ensures your pixelated text fits your screen perfectly.
</i>

```python
import pixel_pretender as pxp 

# Define the maximum number of pixels per line based on your screen capacity.
user_max_pixels = 27

# Set the maximum pixel limit for display.
pxp.set_max_pixels(user_max_pixels)
```
</details>

<details>
    <summary><b><code> try_pixel_samples() </code></b></summary> 
<i><br>
Displays a test phrase in pixelated form using various symbols. The function shows the symbols in customizable increments, allowing you to experiment with different styles interactively.

</i>

```python
import pixel_pretender as pxp

# Display the test phrase using a series of different pixel symbols.
pxp.try_pixel_samples(test_phrase="test - 1234567890", increment=10, try_all=False)
```

<li><code>test_phrase:</code><b> The phrase to be represented in pixels. &nbsp; &nbsp;> <em>Default is "test - 1234567890"</em>.</b></li>
<li><code>increment (int):</code><b> Number of symbols to display before prompting for user input. &nbsp; &nbsp;> <em>Default is 10.</em></b></li>
<li><code>try_all (bool):</code><b> If True, uses the entire custom_pixel_list instead of the default increments. &nbsp; &nbsp;> <em>Default is False.</em></b></li>
<li><code>custom_pixel_list (list):</code><b> A custom list of symbols to be used for pixel representation.  &nbsp; &nbsp;> <em>Default is pixel_samples.</em></b></li><br>
<img src="https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/try_some_pixels.png" alt="">
</details>

<details>
    <summary><b><code> try_rich_colors() </code></b></summary> 
<i><br>
Showcases a test phrase using 255 rich color styles, letting users explore and preview color customization options.
</i>


```python
import pixel_pretender as pxp 

# Display the test phrase using 255 Rich colors for a full range of color effects.
pxp.try_rich_colors(test_phrase="test - 1234567890", increment=10, try_all=False)
```

<li><code>test_phrase:</code><b> The phrase to be represented in rich colors. &nbsp;<em> > Default is "test - 1234567890"</em>.</b></li>
<li><code>increment (int):</code><b> Number of colors to display before prompting for user input.   &nbsp;&nbsp;> <em>Default is 10.</em></b></li>
<li><code>try_all (bool):</code><b>  If True, displays all colors  instead of the default increments  &nbsp; &nbsp;><em> Default is False.</em></b></li>
<br>
<img src="https://raw.githubusercontent.com/AnasseGX/Pixel_pretender/refs/heads/master/Docs/try_rich_colors.png" alt=>
</details>

## Available Features for Users



<details>
    <summary><b><code> colorama_colors </code></b></summary>
<i><br>A tuple of all color names available in Colorama, allowing you to easily apply colors to your pixel text.</i>

```python
import pixel_pretender as pxp 

# Display all available Colorama color names.
print(pxp.colorama_colors)
```
- ***result:***
`('red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'black', 'white', 'light red', 'light yellow', 'light green', 'light blue', 'light cyan', 'light magenta', 'light black', 'light white')`

</details>

<details>
    <summary><b><code> rich_colors </code></b></summary> 
<i><br> A tuple containing 16 color names available in the Rich library for quick access and application to your pixel text.</i>

```python
import pixel_pretender as pxp 

# Display the 16 basic color names available in Rich.
print(pxp.rich_colors)
```
- ***result:***
`('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white', 'bright_black')`
</details>

<details>
    <summary><b><code> pixel_samples </code></b></summary>
<i><br>A list of  Unicode symbols that can be used as pixel characters,
ensuring compatibility across various terminals.</i>

```python
import pixel_pretender as pxp

# Display all compatible Unicode symbols for pixel representation.
print(pxp.pixel_samples)
```
- ***result:***
`['┞', '┬', 'α', '▄', 'Ζ', 'τ', '┘', 'ß', '●', '○', '┟', 'Θ', 'ά', '◫', '┅', '¶', '╘', '►', '╂', 'Δ', '⌷', '₽', 'Ρ', '━', '◶', 'μ', '▛', '█', ...]`

</details>

<details>
    <summary><b><code> cool_pixel_samples </code></b></summary> 
<i><br> A curated list of Unicode symbols that are visually appealing and work well as pixel characters.</i>

```python

import pixel_pretender as pxp 

# Display a selection of recommended symbols for pixelated text.
print(pxp.cool_pixel_samples)
```
- ***result:***
`['╳', '╲', '╱', '╮', '╵', '▄', '▅', '▆', '▇', '█', '▉', '▝', '▚', '▖', '▓', '▒', '░', '▐', '□', '▪', '■', '▟','◆', '◇', '◉', '○', '◎', '●', ...]`
</details> 

## Need Help with a Specific Function?

- **To get detailed information on any function, use Python's built-in `help()` function on the function name.**
   - **For example:**

```python
import pixel_pretender as pxp

help(pxp.apply_colorama_color)
```
- - **result:**
```
Help on function apply_colorama_color in module pixel_pretender:

apply_colorama_color(pixel_list, color)
    Applies a specified text color to a list of pixel strings using Colorama.
    
    Parameters:
    - pixel_list (list of str): A list of pixel strings to color.
    - color (str): A color name that specifies the text color to be applied. (e.g., "red", "blue", "light green").
          - A tuple containing all available color names from the colorama library is stored in colorama_colors
    
    Returns:
    - list of str: A new list of pixel strings with the specified text color applied to the first
                   line and a reset applied to the last line.
    
    Raises:
    - TypeError: If pixel_list is not a list of strings or if color is not a string.
    - ValueError: If color is not in colorama_colors.

```

## Notes
- Unicode* :
     - **Some Unicode symbols may not display correctly due to varying spacing compared to ASCII letters**
- Rich Library :
     - **PyCharm users should enable the “Emulate terminal in output console” option in the run/debug configuration, or run the program in the terminal to view the styled output.**

## Contributing

**This project is maintained as time and resources permit, However, the community is encouraged to contribute, fork, and modify the code freely. Contributions are always welcome and appreciated.**

***You are encouraged to:***
- Submit pull requests for bug fixes or feature enhancements.  
- Fork the repository and adapt it to suit your needs.  

There are no strict guidelines or requirements for contributing,
this project is now a collaborative effort for the benefit of the community. ***However, please note that approving pull requests may take some time.***

### Publishing to PyPI
This project is published on PyPI as `pixel_pretender`. If you contribute a significant feature and would like to publish it, please request to be added as a maintainer on PyPI by opening an issue. Alternatively, feel free to fork this project and publish your version independently.

## Author
Created by [Anasse Gassab](https://github.com/AnasseGX).

## Licenses
- **Pixel_Pretender** is licensed under the MIT License - see the [LICENSE](https://github.com/AnasseGX/Pixel_pretender/blob/master/LICENSE%20.txt) file for details.


- **Colorama** is licensed under the BSD license. See [Colorama License](https://github.com/tartley/colorama/blob/master/LICENSE.txt) for details.
- **Rich** is licensed under the MIT license. See [Rich License](https://github.com/Textualize/rich/blob/master/LICENSE) for details.

## Acknowledgements
- This project uses the [Colorama](https://pypi.org/project/colorama/) library for basic terminal color support.
- This project uses the [Rich](https://pypi.org/project/rich/) library for advanced text formatting and styling in the terminal.

- ***Thanks to the Python community for the awesome libraries like `colorama` and `rich`.***
- Inspired by Seven Segment Displays, ASCII art and creative console designs.