from colorama import init, Fore
from rich.text import Text
from rich.console import Console

_console = Console(width=200)

init()

_character_dict = {

    "0": [["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"]],
    "1": [[" ", "#", " "], [" ", "#", " "], [" ", "#", " "], [" ", "#", " "], [" ", "#", " "]],
    "2": [["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"]],
    "3": [["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]],
    "4": [["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], [" ", " ", "#"]],
    "5": [["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]],
    "6": [["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"]],
    "7": [["#", "#", "#"], [" ", " ", "#"], [" ", "#", "#"], [" ", " ", "#"], [" ", " ", "#"]],
    "8": [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"]],
    "9": [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]],

    "A": [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"]],
    "B": [["#", "#", " "], ["#", " ", "#"], ["#", "#", " "], ["#", " ", "#"], ["#", "#", " "]],
    "C": [["#", "#", "#"], ["#", " ", " "], ["#", " ", " "], ["#", " ", " "], ["#", "#", "#"]],
    "D": [["#", "#", " "], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", " "]],
    "E": [["#", "#", "#"], ["#", " ", " "], ["#", "#", " "], ["#", " ", " "], ["#", "#", "#"]],
    "F": [["#", "#", "#"], ["#", " ", " "], ["#", "#", " "], ["#", " ", " "], ["#", " ", " "]],
    "G": [["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"]],
    "H": [["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"]],
    "I": [["#", "#", "#"], [" ", "#", " "], [" ", "#", " "], [" ", "#", " "], ["#", "#", "#"]],
    "J": [[" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], ["#", " ", "#"], ["#", "#", "#"]],

    "K": [["#", " ", "#"], ["#", "#", " "], ["#", " ", " "], ["#", "#", " "], ["#", " ", "#"]],
    "L": [["#", " ", " "], ["#", " ", " "], ["#", " ", " "], ["#", " ", " "], ["#", "#", "#"]],
    "M": [["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"]],
    "N": [["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"]],
    "O": [["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"]],
    "P": [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", " "], ["#", " ", " "]],
    "Q": [["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", "#", " "]],
    "R": [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", "#", " "], ["#", " ", "#"]],
    "S": [["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]],
    "T": [["#", "#", "#"], [" ", "#", " "], [" ", "#", " "], [" ", "#", " "], [" ", "#", " "]],

    "U": [["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"]],
    "V": [["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], [" ", "#", " "]],
    "W": [["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"]],
    "X": [["#", " ", "#"], ["#", " ", "#"], [" ", "#", " "], ["#", " ", "#"], ["#", " ", "#"]],
    "Y": [["#", " ", "#"], ["#", " ", "#"], [" ", "#", " "], [" ", "#", " "], [" ", "#", " "]],
    "Z": [["#", "#", "#"], [" ", " ", "#"], [" ", "#", " "], ["#", " ", " "], ["#", "#", "#"]],

    ".": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", "#", " "]],
    "-": [[" ", " ", " "], [" ", " ", " "], ["#", "#", "#"], [" ", " ", " "], [" ", " ", " "]],
    "_": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],

    " ": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
    ":": [[" ", " ", " "], [" ", "#", " "], [" ", " ", " "], [" ", "#", " "], [" ", " ", " "]],
    "\n": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
    ",": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", "#", "#"], [" ", " ", "#"]],
    "}": [["#", "#", " "], [" ", "#", " "], [" ", " ", "#"], [" ", "#", " "], ["#", "#", " "]],
    "{": [[" ", "#", "#"], [" ", "#", " "], ["#", " ", " "], [" ", "#", " "], [" ", "#", "#"]],
    "!": [[" ", "#", " "], [" ", "#", " "], [" ", "#", " "], [" ", " ", " "], [" ", "#", " "]],
    '"': [[" ", "#", "#"], [" ", "#", "#"], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
    "'": [[" ", "#", " "], [" ", "#", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],

    "(": [[" ", "#", " "], ["#", " ", " "], ["#", " ", " "], ["#", " ", " "], [" ", "#", " "]],
    ")": [[" ", "#", " "], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", "#", " "]],
    "+": [[" ", " ", " "], [" ", "#", " "], ["#", "#", "#"], [" ", "#", " "], [" ", " ", " "]],
    "=": [[" ", " ", " "], ["#", "#", "#"], [" ", " ", " "], ["#", "#", "#"], [" ", " ", " "]],
    ">": [["#", " ", " "], [" ", "#", " "], [" ", " ", "#"], [" ", "#", " "], ["#", " ", " "]],
    "<": [[" ", " ", "#"], [" ", "#", " "], ["#", " ", " "], [" ", "#", " "], [" ", " ", "#"]],
    "[": [["#", "#", " "], ["#", " ", " "], ["#", " ", " "], ["#", " ", " "], ["#", "#", " "]],
    "]": [[" ", "#", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", "#", "#"]],

}

_colors = {
    "red": Fore.RED,
    "yellow": Fore.YELLOW,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "black": Fore.BLACK,
    "white": Fore.WHITE,

    "light red": Fore.LIGHTRED_EX,
    "light yellow": Fore.LIGHTYELLOW_EX,
    "light green": Fore.LIGHTGREEN_EX,
    "light blue": Fore.LIGHTBLUE_EX,
    "light cyan": Fore.LIGHTCYAN_EX,
    "light magenta": Fore.LIGHTMAGENTA_EX,
    "light black": Fore.LIGHTBLACK_EX,
    "light white": Fore.LIGHTWHITE_EX,
}

_max_pixels = 20

_all_pixel_string = (
    "┞┬α▄Ζτ┘●○┟Θά◫┅¶╘►╂Δ⌷₽Ρ━◶μ▛█Η┛╣Κ┺Ω▚┋▂┌₫ή┎╄▁Ϋο▪₮┍┨θß◎▉└Σ┤╦╱╴◀┯╛╬ΒΞ╋ρ╳▝╒┉π┗╃╢╧▌╮@╯▔╇┻┪▞◯┴┼Π╤┝├╊▜╔Γ┥ς╶▃▅◆"
    "║Ν◪┽β╆╩╫φ▋┊◇┵╀┹₹╾┢◕Τ╺χ▶╪╅υ╗╡╲┰╈ΰ▎╙╨╥▆┸┇┆◧┒ν┚┶╠◄╌┑▙κ┖ψ▒┠◉┦╻■Ψσ₸╰ε╏┐▓┄δ┫┓┱Ϊ▘#╵Υζ•┙┲═Μ€Φ╁▼╓┈╜▊έ◊╿╕╎░λ╚"
    "┕▍∩╷ΧΟω┾╟─┮╼╖┧╸╽§▏Ε▐Λ◨┿ξ┩Ι┡▲▇▀╍┏ί╉□γ◩₺┃╝╞┭┷ηι╹▕│▟┳┣╭Α")

_cool_pixel_string = "ιοχ┇┆┅━┃│┍┑┠┣┳╂╍╝╛╙╳╲╱╮╵▄▅▆▇█▉▝▚▖▔▓▒░▐□▪■▟◆◇◉○◎●◕◧◪◯◶•▀0"

# A list of Unicode symbols that can be used as pixel characters, ensuring compatibility across various terminals.
pixel_samples = list(_all_pixel_string)  # this variable uses an immutable string to keep original state

# A curated list of Unicode symbols that are visually appealing and work well as pixel characters.
cool_pixel_samples = list(_cool_pixel_string)  # this variable uses an immutable string to keep original state

# An error message if the user enters an invalid color.
_color_error_message = (f"!!! ▷▷▷ERROR--THE COLOR YOU ENTERED IS NOT ON THE LIST◁◁◁ !!!"
                        f"!!!\n\t\t ▽▽▽ HERE ARE THE AVAILABLE COLOR NAMES ▽▽▽\n{list(_colors.keys())}\n")


def _validate_input(*args):  # NEEDS DOCSTRINGS
    """
    Validates the input values against expected types and conditions.

    Parameters:
    *args:
        - input_value: The value to be validated.
        - expected_type: The type(s) that input_value is expected to be.
        - condition: A callable (function) that returns True for invalid input; can be None.
        - error_message: The error message to be raised if validation fails.

    Raises:
    TypeError: If input_value is not of the expected_type.
    ValueError: If the condition is met, indicating the input is invalid.
    """

    for input_value, expected_type, condition, error_message in args:
        # Check if the input is of the expected type
        if not isinstance(input_value, expected_type):
            raise TypeError(
                f"Input must be of type ▷{expected_type if isinstance(expected_type, tuple) else expected_type.__name__}◁  got: ▷{type(input_value).__name__}◁.".title())

        # If there's an additional condition, check it
        if condition and condition(input_value):
            raise ValueError(f"{error_message}")


def _change_symbol(symbol="#"):
    """
    Change the default symbol in the pixel grid representation.

    Args:
        symbol (str): The symbol used to represent the pixels, default >'#'.
            Must not be an empty string or whitespace

    Raises:
        ValueError: If the provided symbol is an empty string or whitespace.

    Notes:
        This function is intended for internal use and modifies the global
        variable `__character_dict`, which contains pixel grid representations.
    """

    error_message = "\n\t!!! ▷▷▷--ERROR: ▷ SYMBOL ◁ MUST BE A SINGLE CHARACTER AND MUST NOT BE AN EMPTY STRING, OR A WHITESPACE .--◁◁◁ !!!"

    # Check if the provided symbol is invalid (empty space or empty string or len() != 1)
    _validate_input((symbol,
                     str,
                     lambda arg: len(arg) != 1 or arg in ("", " ") or not arg.isprintable(),
                     error_message))

    # Iterate through all pixel grid lists and update symbols
    for pixel_grid_list in _character_dict.values():
        for sub_list in pixel_grid_list:
            for item_index in range(3):

                if sub_list[item_index] != " ":
                    sub_list[item_index] = symbol


def _wrap_text_at_space(text_to_process):
    """
        Wraps text contained in a list at the nearest space within a specified maximum pixel width.

        Args:
            text_to_process (str): The string to be wrapped.

        Returns:
            tuple: A tuple containing two elements:
                - first_line (str): The portion of the text that fits within the specified width.
                - rest_of_lines (str): The remaining portion of the text after the wrap point.

        Notes:
            Wrapping occurs at the last space found within the specified width. If no space is
            found, it wraps at the maximum pixel width, even if that breaks a word.
        """

    _validate_input((text_to_process, str, lambda arg: len(arg) == 0, "argument can't be empty"))

    text = text_to_process

    index = text[:_max_pixels].rfind(" ")
    slice_at_max_pixels = text[:_max_pixels + 1]  # plus 1 to account for a complete word

    # If the text is shorter than _max_pixels, return it as it will fit.
    if len(text) <= _max_pixels:
        first_line = text
        rest_of_the_lines = ""
        return first_line, rest_of_the_lines

    # if there is a trailing space at the max allowable width or if there is no space present at all split the word at _max_pixels
    if slice_at_max_pixels[-1].isspace() or index == -1:

        first_line = text[:_max_pixels]
        rest_of_lines = text[_max_pixels:].strip()

    else:
        first_line = text[:index]
        rest_of_lines = text[index:].strip()

    return first_line, rest_of_lines


def _process_first_line(line_to_process, var_to_store_pixel_segments, ):
    """

    Processes a string representing a line of characters into a pixelated representation.

    Args:
        line_to_process (str): The string of characters to be converted into pixel representation.
        var_to_store_pixel_segments (str): The accumulated pixel representation to which the new line will be added.
        this functionality  is used by another function "pixel_background"


    Returns:
        str: The updated pixel segment containing the pixel representation of the input line.

    """

    _validate_input(
        (line_to_process, str, None, None),
        (var_to_store_pixel_segments, str, None, None),
    )

    for row in range(5):
        # if line is empty there is no need to append 5 new lines to the output \n\n\n\n\n same for whitespaces
        if len(line_to_process) == 0 or line_to_process.isspace():
            break

        # Iterate through each of the 5 rows of the pixel representation.
        for number_of_letters in range(len(line_to_process)):
            # Process each character in the line to generate its pixel representation.
            var_to_store_pixel_segments += " "
            var_to_store_pixel_segments += " ".join(
                _character_dict[line_to_process[number_of_letters]][row]) + " "
            """
            __character_dict[line_to_process[number_of_letters]][row]:
                Accesses the pixel representation for a specific character in the input line.

                - line_to_process[number_of_letters]: Retrieves the character at the current index,
                  which serves as a key in the __character_dict.

                - __character_dict[line_to_process[number_of_letters]]: Fetches the corresponding
                  pixel pattern, which is a list of 5 sublists representing each row of the pixel grid.

                - [row]: Accesses the current row (0 to 4) from the character's pixel pattern.

            """

        # new line after each row.
        var_to_store_pixel_segments += "\n"

    return var_to_store_pixel_segments


def digitise(text, symbol="#", negative_image=False, pixel_segment_list=None):
    """
    Converts a given message into pixel segments based on a character dictionary,
    wrapping the text if it exceeds the maximum pixel width.

    Args:
        text (str): The message to be converted into pixel segments.
        symbol (str): The symbol used to represent the pixels
                  -- can be All ASCII and Some* Unicode characters (view notes).
                  -- Must not be an empty string or whitespace !
        negative_image (bool): If True, reverses the symbol with whitespace to create a negative image.
        pixel_segment_list (list, optional): A list to store the pixel segments If None, a new list is created.

    Returns:
         Returns:
        - list of str: The processed pixel strings, with or without negative representation.
            with each entry representing a line of pixel text.

    Notes:
        - The text is converted to uppercase to match the dictionary keys.
        - If the test length exceeds the maximum pixel width, the text is wrapped at spaces.
        - Symbols not found in the character dictionary are ignored.
        - If `_max_pixels` exceeds your screen width, the program may not space the characters correctly,
          leading to distorted output. You can adjust this value to fit your screen by running the
          `max_display_capacity()` function and modifying the value of `_max_pixels` by using `set_max_pixels(int)`function .

        - Some*: Some Unicode symbols may not display correctly due to varying spacing compared to ASCII letters,
          the ones that display correctly can be found in `pixel_samples` list.
    """

    _validate_input(
        (text, str, None, None),
        (symbol, str, None, None),
        (pixel_segment_list, (list, type(None)), None, None)
    )

    # Return an empty list if max pixel width is zero or the input message is empty.
    if _max_pixels == 0 or len(text) == 0:
        return []

    if pixel_segment_list is None:
        # Create a new list if none is provided
        pixel_segment_list = []

    # Change the pixel symbol based on the user input.
    _change_symbol(symbol)

    # Initialize a string to store the pixel representations.
    pixel_segments = ""

    # Convert the message to uppercase to match dictionary keys.
    text = text.upper()

    # Filter out characters not present in the character dictionary, creating a valid input list.
    user_input = "".join(
        list(filter(lambda letter: "" if _character_dict.get(letter) is None else letter, list(text))))
    word_length = len(user_input)  # Get the length of the filtered user input.

    # if user_input is empty after filtering unsupported characters return an empty list
    if not user_input:
        return []

    # Process the input if it exceeds the maximum pixel width.
    if word_length >= _max_pixels:

        # Wrap text at spaces for proper formatting.
        first_line, rest_of_the_lines = _wrap_text_at_space(user_input)

        while rest_of_the_lines:
            # Processing the first line, and returning the constructed str representing the whole line.
            pixel_segments = _process_first_line(first_line, pixel_segments, )

            # Add the constructed pixel segments to the list.
            pixel_segment_list.append(pixel_segments)

            # Resetting the variable that stores the pixel segments for the next line
            pixel_segments = ""
            first_line, rest_of_the_lines = _wrap_text_at_space(rest_of_the_lines)

        else:
            # Processing the last part of the message sins the while loop ignores it
            pixel_segment_list.append(_process_first_line(first_line, pixel_segments, ))

    # Process the input if it is within the maximum pixel width.
    elif word_length < _max_pixels:

        # Processing the user_input, and returning the constructed str representing the whole line.
        pixel_segments = _process_first_line(user_input, pixel_segments, )

        # Add the constructed pixel segments to the list.
        pixel_segment_list.append(pixel_segments)

    # Check if negative image processing is enabled
    if negative_image:  # Check if negative image processing is enabled
        reversed_list = []  # Initialize a list to store the processed lines

        # Create a translation table to swap whitespace with the symbol
        translation_table = str.maketrans({
            ' ': symbol,  # Replace space with the provided symbol
            symbol: ' '  # Replace the provided symbol with space
        })

        # Iterate over each line in the pixel_segment_list
        for line in pixel_segment_list:
            line_length = line.find("\n")  # Find the index of the newline character
            padding = symbol * line_length  # Create padding of symbols equal to the line length
            negative_pixels = line.translate(translation_table)  # Translate the line using the translation table

            # Combine padding, negative pixels, and padding again
            add_padding = padding + "\n" + negative_pixels + padding
            reversed_list.append(add_padding)  # Append the modified line to the reversed_list

        pixel_segment_list = reversed_list  # Update the original list with the processed lines

    return pixel_segment_list  # Return the list of pixel segments.


def apply_colorama_color(pixel_list, color):
    """
    Applies a specified text color to a list of pixel strings using Colorama.

    Parameters:
    - pixel_list (list of str): A list of pixel strings to color.
    - color (str): A color name that specifies the text color to be applied. (e.g., "red", "blue", "light green").
          - A tuple containing all available color names from the colorama library is stored in colorama_colors.

    Returns:
    - list of str: A new list of pixel strings with the specified text color applied to the first
                   line and a reset applied to the last line.

    Raises:
    - TypeError: If pixel_list is not a list of strings or if color is not a string.
    - ValueError: If color is not in colorama_colors.
    """

    # Validate the input types and conditions
    _validate_input(
        (pixel_list, list,
         lambda arg: not isinstance(arg[0], str) if arg else None,
         "pixel_list must be list of strings list[str]".upper()),
        (color, str, None, None),
    )

    color = color.strip()
    # Check if the specified color is valid
    if color not in _colors.keys():
        raise ValueError(_color_error_message)

    if pixel_list:  # Proceed if pixel_list is not empty
        if len(pixel_list) == 1:  # If there's only one line in the list
            # Apply color to the line and reset after
            colored_list = [_colors[color] + pixel_list[0] + Fore.RESET]
        else:  # If there are multiple lines
            # Apply color to the first line and reset after the last line
            add_color = _colors[color] + pixel_list[0]
            add_reset = pixel_list[-1] + Fore.RESET
            colored_list = [add_color] + pixel_list[1: len(pixel_list) - 1] + [add_reset]

        return colored_list  # Return the list with colors applied

    else:  # If pixel_list is empty, return an empty list
        return []


def apply_rich_color(pixel_list, text_color, background_color=None):
    """
    Applies colors to a list of pixel strings and returns a list of Text objects.

    Parameters:
    - pixel_list (list of str): The list of pixel strings to color.
    - text_color (str): The color to apply to the text.
                     - color can be : "red" "green" "yellow" "blue" "magenta" "cyan" "white" "black"
                     - or a hexadecimal value : "#00E6BD"
                     - or a rgb value : "rgb(175,0,255)"
                     - or the color’s number (between 0 and 255) with the syntax "color(number)"
    - background_color (str, optional): The color to apply as a background.

    Returns:
    - List[Text]: A list of Text objects with applied styles.

    Notes:
        - You can apply any available color from the Rich library to the output. For more details, refer to the Rich library documentation.
        - You can also perform any operations on the `Text` objects returned in the list by this function, as supported by the Rich library.
        - PyCharm users should enable the “Emulate terminal in output console” option in the run/debug configuration, or run the program in the terminal to view the styled output.
    """
    # Validate the input parameters for type and conditions
    _validate_input(
        (pixel_list, list,
         lambda arg: not isinstance(arg[0], str) if arg else None
         , "pixel_list must be list of strings list[str]"),  # Ensure pixel_list is a list of strings
        (text_color, str, None, None),  # Ensure text_color is a string
        (background_color, (str, type(None)), None, None),  # Ensure background_color is either a string or None
    )

    # Initialize the style with the specified text color
    style = text_color
    # If a background color is provided, append it to the style
    if background_color:
        style += f" on {background_color}"

    # Create a list of Text objects, applying the style to each line in pixel_list
    colored_lines = [Text(line, style=style) for line in pixel_list]

    return colored_lines  # Return the list of styled Text objects


def display_pixels(pixel_list):
    """
    Displays a list of pixel strings or Text objects to the console.

    Parameters:
    - pixel_list (list of [Text] or [str]): A list containing pixel representations as strings or Text objects (from the rich library).


    If the list is empty, the function returns None.
    """
    # Validate the input to ensure pixel_list is a list
    _validate_input(
        (
            pixel_list,
            list,
            lambda arg: not isinstance(arg[0], str) and not isinstance(arg[0], Text) if arg else None,
            "pixel_list must be list of strings list[str] or list[Text]"
        )
    )
    # Check if the pixel_list is not empty
    if pixel_list:
        # If the first element is a string, print each line directly
        if isinstance(pixel_list[0], str):
            for line in pixel_list:
                print(line)  # Print each string line to the console

        # If the first element is a Text object, use the console to print each line
        elif isinstance(pixel_list[0], Text):
            for line in pixel_list:
                _console.print(line)  # Print each Text object to the console
    else:
        pass  # No operation for an empty list


def max_display_capacity(custom_value=50):
    """
    Tests the maximum number of characters that can be displayed on the user's screen.

    This function tests the maximum number of characters your screen can display.
    The default maximum pixel value is 20, but you can adjust this based on your screen size.
    Use this function to find the highest number of pixels your display can handle,
    and then set that value with `set_max_pixels(int)` for a better experience.

    Returns:
        None: This function does not return a value. It prints the number of characters
        displayed and informs the user about the maximum capacity of their display.

    Notes:
        - If shapes appear distorted or incorrect, the user should adjust the maximum pixel
          setting using the `set_max_pixels()` function to match the indicated number.
    """
    error_message = f"!!! ▷▷▷ERROR-- CUSTOM_VALUE:▷{custom_value}◁MUST BE LARGER THAN 0 ◁◁◁ !!!"

    _validate_input((custom_value, int, lambda arg: arg <= 0, error_message))

    test_string = "8"  # String to be used for testing display capacity.
    old_max_pixels_value = _max_pixels  # Store the current maximum pixel value.
    set_max_pixels(custom_value)  # Temporarily set the maximum pixel limit to 50.

    for number in range(1, custom_value + 1):
        # Display the test string.
        display_pixels(digitise(test_string * number, "#"))

        # Print the current count of characters displayed.
        print(number)

    print(Fore.LIGHTGREEN_EX +
          f"\n____| The Maximum Number Of Characters Your Display Can Properly Show\n"
          f"    | Is Indicated Under The Last Line That Displays Correctly \n"
          f"\t-> You Should Adjust >> set_max_pixels() << To Match That Number."
           + Fore.RESET)

    # Restore the original maximum pixel value.
    set_max_pixels(old_max_pixels_value)


def set_max_pixels(user_max_pixels):
    """
    Sets the maximum number of pixels that can be displayed.

    This function updates the global `__max_pixels` variable to the value provided by the user.
    It must be a positive integer; otherwise, an error message is displayed,
    and the previous value of `__max_pixels` is restored.

    Args:
        user_max_pixels (int): The desired maximum number of pixels to display, Must be larger than 0

    Raises:
        TypeError: If `user_max_pixels` is not of type `int`.
    """
    global _max_pixels

    error_message = "\n\t\t!!! ▷▷▷--ERROR: ▷max_pixels()◁ MUST BE LARGER THAN 0 AND OF TYPE (int)--◁◁◁ !!!"

    _validate_input((user_max_pixels, int, lambda arg: arg <= 0, error_message))

    # Update the maximum pixels to user-defined value
    _max_pixels = user_max_pixels


def try_pixel_samples(test_phrase="test - 1234567890", increment=10, try_all=False,
                      custom_pixel_list=pixel_samples):
    """
    Display a series of pixel representations of a given test phrase using various symbols.

    Args:
        test_phrase (str): The phrase to be represented in pixels. Default is "test - 1234567890".
        increment (int): Number of symbols to display before prompting for user input. Default is 10.
        try_all (bool): If True, uses the entire custom_pixel_list instead of the default increments. Default is False.
        custom_pixel_list (list): A custom list of symbols to be used for pixel representation. Default is pixel_samples.

    Returns:
        None: This function does not return a value.

    Notes:
        The function displays pixel representations in increments, allowing the user to pause
        and continue or quit the display process.
    """

    _validate_input(
        (test_phrase, str, None, None),
        (increment, int, lambda arg: arg <= 0, "▷▷▷--ERROR:increment Must be larger than 0--◁◁◁ !!!".upper()),
        (try_all, bool, None, None)
    )

    if _max_pixels <= 0:
        return print(
            "!!! (_max_pixels) variable is less than or equal to 0\n\tno pixels can be displayed !\n\t\t>please set (_max_pixels) to a valuer larger than 0".upper())

    if try_all is True:
        # Set increments to the length of the custom pixel list.
        increment = len(custom_pixel_list)

    # Initialize the count for displayed symbols which serves as an index for that particular symbol.
    count = 0
    for pixel_symbol in custom_pixel_list:

        # Display the pixel representation of the test phrase using the current symbol.
        display_pixels(digitise(test_phrase, pixel_symbol))
        # Print the current symbol and its index.

        print(f"-----^------\n-Symbol: {pixel_symbol}\n-Index : {count}\n------------\n")

        # Prompt the user after displaying the specified number of symbols.
        if count % increment == 0 and count != 0:

            user_input = input('\t\t>>> : Enter "C" to continue or "Q" to quit: '.upper())
            if user_input.lower() == "q":
                # Exit the loop if the user chooses to quit.
                break
            else:
                pass
        # Increment the count of displayed symbols.
        count += 1


def try_cool_pixels(test_phrase="test_cool - 1234567890", increment=10, try_all=False,
                    custom_pixel_list=cool_pixel_samples):
    """
       Display a series of pixel representations of a given test phrase using various symbols.

       Args:
           test_phrase (str): The phrase to be represented in pixels. Default is "test - 1234567890".
           increment (int): Number of symbols to display before prompting for user input. Default is 10.
           try_all (bool): If True, uses the entire custom_pixel_list instead of the default increments. Default is False.
           custom_pixel_list (list): A custom list of symbols to be used for pixel representation. Default is pixel_samples.

       Returns:
           None: This function does not return a value.

       Notes:
           The function displays pixel representations in increments, allowing the user to pause
           and continue or quit the display process.
       """
    # input validation happens in try_pixel_samples

    try_pixel_samples(test_phrase, increment, try_all, custom_pixel_list)


def try_rich_colors(test_phrase="test - 1234567890", increment=10, try_all=False):
    """
    Display 255 of rich colors

    Args:
        test_phrase (str): The phrase to be represented in rich colors. Default is "test - 1234567890".
        increment (int): Number of colors to display before prompting for user input. Default is 10.
        try_all (bool): If True, displays all colors  instead of the default increments. Default is False.

    Returns:
        None: This function does not return a value.

    Notes:
        -The function displays rich colors in increments, allowing the user to pause
            and continue or quit the display process.
        -The rich library offers more than 255 colors, for more details, refer to the Rich library documentation.
        - PyCharm users should run the program in the terminal to view the styled output
            for more details, refer to the Rich library documentation.

    """

    _validate_input(
        (test_phrase, str, None, None),
        (increment, int, lambda arg: arg <= 0, "▷▷▷--ERROR:increment Must be larger than 0--◁◁◁ !!!".upper()),
        (try_all, bool, None, None)
    )
    test_phrase = digitise(test_phrase)
    if _max_pixels <= 0:
        return print(
            "!!! (_max_pixels) variable is less than or equal to 0\n\tno pixels can be displayed !\n\t\t>please set (_max_pixels) to a valuer larger than 0".upper())

    if try_all is True:
        # Set increments to the total number of colors.
        increment = 255

    # Initialize the count for color number which serves as an index for that particular color.
    count = 0
    for color_number in range(0, 255):

        # Display the color representation of the test phrase using "color(color_number)".
        color_test = apply_rich_color(test_phrase, f"color({color_number})")
        # Display the color
        display_pixels(color_test)
        # Print the color number
        print(f'------------------\n Color number: {color_number}\n------------------\n')

        # Prompt the user after displaying the specified number of colors.
        if count % increment == 0 and count != 0:

            user_input = input('\t\t>>> : Enter "C" to continue or "Q" to quit: '.upper())
            if user_input.lower() == "q":
                # Exit the loop if the user chooses to quit.
                break
            else:
                pass
        # Increment the count of displayed colors.
        count += 1


# A tuple of all color names available in Colorama, allowing you to easily apply colors to your pixel text.
colorama_colors = tuple(_colors.keys())
# A tuple containing 16 color names available in the Rich library for quick access and application to your pixel text.
rich_colors = (
"red", "green", "yellow", "blue", "magenta", "cyan", "white", "black", " bright_green", "bright_yellow", "bright_blue",
"bright_magenta", "'bright_cyan'," "bright_white", "bright_black")