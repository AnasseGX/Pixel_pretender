import unittest
from unittest.mock import patch
from io import StringIO
import pixel_pretender  # Import the module
from colorama import Fore
from rich.text import Text


class TestPixelPretender(unittest.TestCase):

    def tearDown(self):
        # Reset max_pixels after each test to avoid state leaking
        pixel_pretender.set_max_pixels(25)  # or set it to a default value

        # Reset _character_dict after each test
        pixel_pretender._change_symbol()

    def test_validate_input_valid_inputs(self):
        try:
            # Arrange: Define valid input scenarios
            text = "valid"
            number = 123
            list_input = [1, 2, 3]

            # Valid input with conditions
            valid_condition_input = "v"
            non_empty_condition_input = "valid"

            # Act: Call the _validate_input function with valid inputs
            pixel_pretender._validate_input(
                (text, str, None, None),  # Simple string
                (number, int, None, None),  # Simple integer
                (list_input, list, None, None),  # Simple list
                (valid_condition_input, str, lambda arg: arg == " ", "Input must not be a space character"),
                # Should pass
                (non_empty_condition_input, str, lambda arg: arg == "", "Input must not be empty")  # Should pass
            )

            # If no exceptions were raised, we can assert that the test passed
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Valid input test failed: {str(e)}")

    def test_validate_input_invalid_inputs(self):

        # Test for invalid types
        with self.assertRaises(TypeError):
            pixel_pretender._validate_input(
                ("invalid", int, None, None)  # Passing a string instead of an integer
            )

        with self.assertRaises(TypeError):
            pixel_pretender._validate_input(
                (50, str, None, None)  # Passing a string instead of an integer
            )

        with self.assertRaises(TypeError):
            pixel_pretender._validate_input(
                (list, str, None, None)  # Passing a string instead of an integer
            )

        # Test for input that violates the condition for non-empty strings
        with self.assertRaises(ValueError):
            pixel_pretender._validate_input(
                ("", str, lambda arg: arg == "", "Input must not be empty")  # Should raise for empty string
            )

        # Test for additional invalid conditions (space character)
        with self.assertRaises(ValueError):
            pixel_pretender._validate_input(
                (" ", str, lambda arg: arg == " ", "Input must not be a space character")
                # Should raise for space character
            )

    def test_change_symbol_valid_inputs(self):
        # Arrange: Set up initial state for the test
        character_dict_copy = pixel_pretender._character_dict.copy()  # Copy original dict
        original_symbol = "#"  # The symbol we want to change
        new_symbol = "*"  # The new symbol we want to use

        # Act: Call the __change_symbol function with the new symbol
        pixel_pretender._change_symbol(new_symbol)  # Call the function

        # Assert: Check that the original symbol is no longer present in any of the lists
        for rows in character_dict_copy.values():  # Only iterate over the values
            for row in rows:
                # Ensure the original symbol is no longer present
                self.assertNotIn(original_symbol, row)  # Check that original_symbol is not in the row
                # Ensure every symbol is now the new symbol or whitespace or empty string
                self.assertTrue(all(symbol == new_symbol or symbol == " " or symbol == "" for symbol in row))

    def test_change_symbol_invalid_inputs(self):
        # Test for empty string
        with self.assertRaises(ValueError):
            pixel_pretender._change_symbol("")

        # Test for whitespace
        with self.assertRaises(ValueError):
            pixel_pretender._change_symbol(" ")

        # Test for string with more than one character
        with self.assertRaises(ValueError):
            pixel_pretender._change_symbol("**")

    def test_edge_cases_change_symbol(self):
        # Test for non-printable characters
        with self.assertRaises(ValueError):
            pixel_pretender._change_symbol("\x00")  # Null character

        # Test for special characters
        new_symbol = "@"
        pixel_pretender._change_symbol(new_symbol)
        for rows in pixel_pretender._character_dict.values():
            for row in rows:
                self.assertTrue(all(symbol == new_symbol or symbol == " " or symbol == "" for symbol in row))

        # Test for too long strings
        with self.assertRaises(ValueError):
            pixel_pretender._change_symbol("long_string")

        # Test for integer input
        with self.assertRaises(TypeError):
            pixel_pretender._change_symbol(1)  # Integer input

        # Test for None input
        with self.assertRaises(TypeError):
            pixel_pretender._change_symbol(None)  # None input

    def test_wrap_text_at_space_valid_inputs(self):
        # Test 1
        pixel_pretender.set_max_pixels(25)  # Test case passes
        input_text = "This is a test string for wrapping."
        expected_first_line = "This is a test string for"
        expected_rest_lines = "wrapping."

        first_line, rest_lines = pixel_pretender._wrap_text_at_space(input_text)
        self.assertEqual(first_line, expected_first_line,
                         f"Expected first line: '{expected_first_line}', but got: '{first_line}'")
        self.assertEqual(rest_lines, expected_rest_lines,
                         f"Expected rest lines: '{expected_rest_lines}', but got: '{rest_lines}'")

        # Test 2
        pixel_pretender.set_max_pixels(50)  # This should now work consistently
        input_text = "This is a "
        expected_first_line = "This is a "
        expected_rest_lines = ""
        first_line, rest_lines = pixel_pretender._wrap_text_at_space(input_text)
        self.assertEqual(first_line, expected_first_line,
                         f"Expected first line: '{expected_first_line}', but got: '{first_line}'")
        self.assertEqual(rest_lines, expected_rest_lines,
                         f"Expected rest lines: '{expected_rest_lines}', but got: '{rest_lines}'")

        # Case 3: Text fits within the width
        pixel_pretender.set_max_pixels(40)  # Ensure max_width is set
        input_text = "Short text."
        expected_first_line = "Short text."  # Corrected expectation
        expected_rest_lines = ""

        first_line, rest_lines = pixel_pretender._wrap_text_at_space(input_text)

        self.assertEqual(first_line, expected_first_line,
                         f"?Expected first line: '{expected_first_line}', but got: '{first_line}'")
        self.assertEqual(rest_lines, expected_rest_lines,
                         f"?Expected rest lines: '{expected_rest_lines}', but got: '{rest_lines}'")

    def test_wrap_text_at_space_invalid_inputs(self):
        with self.assertRaises(TypeError):
            pixel_pretender._wrap_text_at_space(123)  # Integer input
        with self.assertRaises(TypeError):
            pixel_pretender._wrap_text_at_space(3.14)  # Float input
        with self.assertRaises(TypeError):
            pixel_pretender._wrap_text_at_space(None)  # None as input
        # test_invalid_input_empty_list
        with self.assertRaises(TypeError):  # Adjust this if necessary
            pixel_pretender._wrap_text_at_space([])
        with self.assertRaises(ValueError):  # Adjust this if necessary
            pixel_pretender._wrap_text_at_space("")  # Empty string input

        # test_invalid_input_non_string
        with self.assertRaises(TypeError):
            pixel_pretender._wrap_text_at_space([1, 2, 3])  # List of integers

        with self.assertRaises(TypeError):
            pixel_pretender._wrap_text_at_space(["valid", None])  # List with None

        # This is a valid string input, so no exception should be raised
        result = pixel_pretender._wrap_text_at_space("This is a valid string input.")
        self.assertIsInstance(result, tuple)  # Check if it returns a tuple

    def test_process_first_line_valid_input(self):
        # Test Case 1: Basic Case with "AB"
        line_to_process = "AB"
        var_to_store_pixel_segments = ""


        expected_output = ' # # #  # #   \n #   #  #   # \n # # #  # #   \n #   #  #   # \n #   #  # #   \n'

        result = pixel_pretender._process_first_line(line_to_process, var_to_store_pixel_segments)

        result = result
        expected_output = expected_output
        self.assertEqual(result, expected_output, msg=f'result :\n{result}\nexpected_output:\n{expected_output}')

        # Test Case 2: Empty string input
        line_to_process = ""
        var_to_store_pixel_segments = ""

        expected_output = ""  # Since there's no input, the result should be empty.

        result = pixel_pretender._process_first_line(line_to_process, var_to_store_pixel_segments)
        result = result
        expected_output = expected_output

        self.assertEqual(result, expected_output, msg=f'result :\n{result}\nexpected_output:\n{expected_output}')

        # Test Case 3: Longer input "BAA"
        line_to_process = "AILD"
        var_to_store_pixel_segments = ""

        expected_output = \
            (' # # #  # # #  #      # #   \n #   #    #    #      #   # \n # # #   '
             ' #    #      #   # \n #   #    #    #      #   # \n #   #  # # #  # # #  # #   \n')

        result = pixel_pretender._process_first_line(line_to_process, var_to_store_pixel_segments)
        result = result
        expected_output = expected_output
        # _____________________________________DEBUG________________________________________________
        #     print("Result with repr():")
        #     print(repr(result))
        #
        #     print("\nExpected output with repr():")
        #     print(repr(expected_output))
        #
        #     result_lines = result.splitlines()
        #     expected_lines = expected_output.splitlines()
        #
        #     for i, (res_line, exp_line) in enumerate(zip(result_lines, expected_lines), start=1):
        #         print(f"Line {i}:")
        #         print(f"Result:    {repr(res_line)}")
        #         print(f"Expected:  {repr(exp_line)}")
        #
        #     print(f"Trailing spaces in result: '{result[-1:]}'")  # Last character of result
        #     print(f"Trailing spaces in expected_output: '{expected_output[-1:]}'")  # Last character of expected_output
        #
        #     print(f"Length of result: {len(result)}")
        #     print(f"Length of expected output: {len(expected_output)}")
        # ___________________________________________________________________________________________

        self.assertEqual(result, expected_output, msg=f'result :\n{result}\nexpected_output:\n{expected_output}')

        # Additional tests covering the new functionality
        # 1. Test for Valid Filler Color

        # 2. Test for Empty String
        result_empty_string = pixel_pretender._process_first_line("", "")
        self.assertEqual(result_empty_string, "", "Empty string should result in no added pixel segments.")

        # 3. Test for Whitespace String
        result_whitespace_string = pixel_pretender._process_first_line("   ", "")
        self.assertEqual(result_whitespace_string, "", "Whitespace string should result in no added pixel segments.")

    def test_process_first_line_invalid_inputs(self):

        self.pixel_representation = ""  # Initialize an empty representation for tests


        # 1. Non-string input for line_to_process
        with self.assertRaises(TypeError):
            pixel_pretender._process_first_line(123, self.pixel_representation)

        # 2. Non-string input for var_to_store_pixel_segments
        with self.assertRaises(TypeError):
            pixel_pretender._process_first_line("AB", 456, False)

        # 3. NoneType input for var_to_store_pixel_segments
        with self.assertRaises(TypeError):
            pixel_pretender._process_first_line("AB", None)

        # 4. Empty string input
        result = pixel_pretender._process_first_line("", self.pixel_representation)
        self.assertEqual(result, self.pixel_representation)  # Should return unchanged representation

        # 5. Whitespace-only input
        result = pixel_pretender._process_first_line("       ", self.pixel_representation)
        self.assertEqual(result, self.pixel_representation)  # Should also return unchanged representation



    def test_digitise_additional_cases(self):
        """Test additional edge cases for the digitise function."""

        # Setup default parameters for reuse in the tests
        default_message = "AB"
        default_symbol = "#"
        default_max_pixels = 22  # Assuming this is the default max pixels value

        # Reset _max_pixels before the next test
        pixel_pretender.set_max_pixels(default_max_pixels)

        # Test if pixel_segment_list is created when the argument is None
        result = pixel_pretender.digitise(default_message, pixel_segment_list=None)
        self.assertIsInstance(result, list, "Expected a list to be created when pixel_segment_list is None.")
        self.assertGreater(len(result), 0, "Expected the list to contain pixel segments.")

        # Test if pixel_segment_list persists when the argument is a list
        existing_list = ["existing_segment"]
        result = pixel_pretender.digitise(default_message, pixel_segment_list=existing_list)
        self.assertEqual(result[0], "existing_segment", "Expected the list to persist its existing content.")
        self.assertGreater(len(result), 1, "Expected the list to have new pixel segments appended.")

        # Test when the message is shorter than _max_pixels
        pixel_pretender.set_max_pixels(10)  # Change max pixels for this test
        result = pixel_pretender.digitise("A", default_symbol)
        self.assertEqual(len(result), 1, "Expected a single line of pixel output for a short message.")

        # Test when the message is longer than _max_pixels
        pixel_pretender.set_max_pixels(2)  # Set a very small max pixel value to force wrapping
        result = pixel_pretender.digitise("ABCD", default_symbol)
        self.assertGreater(len(result), 1,
                           "Expected the message to be wrapped across multiple lines when longer than _max_pixels.")

        # Reset _max_pixels to the default after all tests
        pixel_pretender.set_max_pixels(default_max_pixels)

    def test_digitise_invalid_inputs(self):
        """Test invalid inputs for the digitise function."""

        # Test with non-string message input
        with self.assertRaises(TypeError, msg="Expected a TypeError when message is not a string."):
            pixel_pretender.digitise(123)  # Passing an integer instead of a string

        # Test with empty symbol (invalid input)
        with self.assertRaises(ValueError, msg="Expected a ValueError when symbol is an empty string."):
            pixel_pretender.digitise("AB", symbol="")

        # Test with whitespace symbol (invalid input)
        with self.assertRaises(ValueError, msg="Expected a ValueError when symbol is whitespace."):
            pixel_pretender.digitise("AB", symbol=" ")

        # Test with invalid pixel_segment_list type
        with self.assertRaises(TypeError, msg="Expected a TypeError when pixel_segment_list is not a list or None."):
            pixel_pretender.digitise("AB", pixel_segment_list="not_a_list")  # Passing a string instead of a list

        # Test with invalid max pixels scenario by setting it to a string (not allowed)
        with self.assertRaises(TypeError, msg="Expected a TypeError when max pixels is a string."):
            pixel_pretender.set_max_pixels("invalid_max_pixels")

        # Test with empty message string
        result = pixel_pretender.digitise("")
        self.assertEqual(result, [], "Expected an empty list when message is an empty string.")

    def test_digitise_edge_cases(self):
        # Set default values
        self.default_symbol = "#"
        self.default_max_pixels = 22
        pixel_pretender.set_max_pixels(self.default_max_pixels)

        # Very long message
        long_message = "A" * 100  # Message significantly longer than _max_pixels
        long_result = pixel_pretender.digitise(long_message, symbol=self.default_symbol)
        # each pixel is made up of 45 symbols and whitespaces
        self.assertTrue(all(len(line) // 45 <= self.default_max_pixels for line in long_result),
                        f"Long message did not wrap correctly en(long_result[0]): {len(long_result[0])}.")

        # Exact fit
        exact_fit_message = "A" * self.default_max_pixels  # Message that exactly fits
        exact_fit_result = pixel_pretender.digitise(exact_fit_message, symbol=self.default_symbol)
        self.assertEqual(len(exact_fit_result), 1, "Exact fit message produced multiple lines.")

        # Empty list passed for pixel_segment_list
        expected_output = [' # # #  # #   \n #   #  #   # \n # # #  # #   \n #   #  #   # \n #   #  # #   \n']
        empty_list_result = pixel_pretender.digitise("AB", symbol=self.default_symbol, pixel_segment_list=[])
        self.assertEqual(empty_list_result, expected_output, "Empty list did not populate correctly.")

        # Large symbol
        large_symbol = "##"  # More than one character
        with self.assertRaises(ValueError, msg="Expected ValueError when a symbol longer than one character is used."):
            pixel_pretender.digitise("AB", symbol=large_symbol)

        # All unsupported characters
        unsupported_message = "²&é"  # unsupported characters
        unsupported_result = pixel_pretender.digitise(unsupported_message, symbol=self.default_symbol)
        self.assertEqual(unsupported_result, [], "Message with all unsupported characters did not return empty list.")

        # Mixed supported and unsupported characters
        mixed_message = "A&B²X°YZ"
        expected_output = [
        ' # # #  # #    #   #  #   #  # # # \n #   #  #   #  #   #  #   #      # \n # # #  # #      #      #      #   \n #   #  #   #  #   #    #    #     \n #   #  # #    #   #    #    # # # \n']
        mixed_result = pixel_pretender.digitise(mixed_message, symbol=self.default_symbol)
        expected_mixed_result = expected_output  # Adjust based on your _character_dict
        self.assertEqual(mixed_result, expected_mixed_result,
                         "Mixed message did not filter unsupported characters correctly.")

    def test_max_display_capacity(self):

        # Capture the output of the function
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pixel_pretender.max_display_capacity()  # Call the function

            output = fake_out.getvalue().strip().split('\n')

            # Verify the last line contains guidance about adjusting pixel settings
            self.assertIn("You Should Adjust >> set_max_pixels()", output[-1],
                          "Guidance about adjusting pixels is missing.")

        # Test with default custom_width
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pixel_pretender.max_display_capacity()  # Default width of 50
            output = fake_out.getvalue().strip()
            self.assertIn("The Maximum Number Of Characters Your Display Can Properly Show", output)

        # Test with custom width
        custom_width = 100
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pixel_pretender.max_display_capacity(custom_width)
            output = fake_out.getvalue().strip()
            self.assertIn("The Maximum Number Of Characters Your Display Can Properly Show", output)

        # Test with a custom width that is smaller than the default
        custom_width_small = 20
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pixel_pretender.max_display_capacity(custom_width_small)
            output = fake_out.getvalue().strip()
            self.assertIn("The Maximum Number Of Characters Your Display Can Properly Show", output)

        # Test edge case with custom_width of 0
        with self.assertRaises(ValueError):
            pixel_pretender.max_display_capacity(0)

        # Test edge case with negative custom_width
        with self.assertRaises(ValueError):
            pixel_pretender.max_display_capacity(-10)

    def test_set_max_pixels_all_cases(self):
        # Save the original _max_pixels value to restore it later
        original_max_pixels = pixel_pretender._max_pixels

        # Test 1: Valid input - Update _max_pixels and check if the update occurs
        valid_value = 30
        pixel_pretender.set_max_pixels(valid_value)
        self.assertEqual(pixel_pretender._max_pixels, valid_value,
                         f"Expected _max_pixels to be {valid_value}, but got {pixel_pretender._max_pixels}")

        # Test 2: Invalid input - Negative integer (should raise ValueError)
        invalid_negative_value = -5
        with self.assertRaises(ValueError, msg="Expected ValueError for negative integer input."):
            pixel_pretender.set_max_pixels(invalid_negative_value)

        # Test 3: Invalid input - Zero (should raise ValueError)
        zero_value = 0
        with self.assertRaises(ValueError, msg="Expected ValueError for zero input."):
            pixel_pretender.set_max_pixels(zero_value)

        # Test 4: Invalid input - Non-integer type (should raise TypeError)
        non_integer_value = "fifty"
        with self.assertRaises(TypeError, msg="Expected TypeError for non-integer input."):
            pixel_pretender.set_max_pixels(non_integer_value)

        # Test 5: Invalid input - Float (should raise TypeError)
        float_value = 25.5
        with self.assertRaises(TypeError, msg="Expected TypeError for float input."):
            pixel_pretender.set_max_pixels(float_value)

        # Restore the original _max_pixels value
        pixel_pretender._max_pixels = original_max_pixels

    def test_try_all_pixels(self):
        # Key behaviors to test:
        # 1. Verifying that the function correctly validates input types and raises appropriate errors.
        # 2. Checking if the function properly handles try_all=True by iterating through all symbols in custom_pixel_list.
        # 3. Ensuring the pixel grid is printed with the expected color.
        # 4. Mocking input to simulate both "continue" and "quit" commands during the symbol display.

        # Mock _colors for testing and add common elements
        all_pixel_samples = ["#", "*", "@", "&"]
        test_phrase = "test - 1234567890"


        # 1. Valid inputs: checking basic functionality
        with patch('builtins.input', side_effect=["c", "q"]):
            pixel_pretender.try_all_pixels(test_phrase=test_phrase,  increment=2, try_all=False,
                           custom_pixel_list=all_pixel_samples)
            pixel_pretender.try_all_pixels(test_phrase=test_phrase,  increment=10, try_all=True)


        # 2. Handling try_all=True (check if it processes all symbols in custom_pixel_list)
        with patch('builtins.input', side_effect=["q"]):
            pixel_pretender.try_all_pixels(test_phrase=test_phrase,  increment=10, try_all=True)


        # 4. Mocking input to simulate both "continue" and "quit" commands during display
        with patch('builtins.input', side_effect=["c", "q"]):
            pixel_pretender.try_all_pixels(test_phrase=test_phrase,  increment=2, try_all=False,
                           custom_pixel_list=all_pixel_samples)

        # Invalid inputs

        # Invalid increment (negative)
        with self.assertRaises(ValueError, msg="Expected ValueError when increment is negative"):
            pixel_pretender.try_all_pixels(test_phrase=test_phrase,increment=-1, try_all=False)

        # Invalid increment (zero)
        with self.assertRaises(ValueError, msg="Expected ValueError when increment is zero"):
            pixel_pretender.try_all_pixels(test_phrase=test_phrase, increment=0, try_all=False)

        # Empty test_phrase
        with patch('builtins.input', side_effect=["q"]):
            pixel_pretender.try_all_pixels(test_phrase="",  increment=2, try_all=False,
                           custom_pixel_list=all_pixel_samples)

        # Empty custom_pixel_list
        with patch('builtins.input', side_effect=["q"]):
            pixel_pretender.try_all_pixels(test_phrase=test_phrase, increment=2, try_all=False, custom_pixel_list=[])
            print("arrived at empty")

    def test_apply_colorama_color(self):
        # Setup valid color in the _colors dictionary for testing purposes
        test_color = 'green'
        test_color_code = pixel_pretender._colors[test_color]

        # ==== Valid Input Cases ====
        # Test with a single line in pixel_list
        pixel_list_single = ["▉▉▉▉▉"]
        result_single = pixel_pretender.apply_colorama_color(pixel_list_single, test_color)
        self.assertEqual(result_single, [test_color_code + pixel_list_single[0] + Fore.RESET],
                         "Failed on single line pixel_list")

        # Test with multiple lines in pixel_list
        pixel_list_multi = ["▉▉▉▉", "▉▉▉", "▉▉"]
        result_multi = pixel_pretender.apply_colorama_color(pixel_list_multi, test_color)
        expected_multi = [
            test_color_code + pixel_list_multi[0],
            pixel_list_multi[1],
            pixel_list_multi[2] + Fore.RESET
        ]
        self.assertEqual(result_multi, expected_multi,
                         "Failed on multi-line pixel_list")

        # ==== Invalid Input Cases ====
        # Invalid pixel_list (not a list)
        with self.assertRaises(TypeError):
            pixel_pretender.apply_colorama_color("Not a list", test_color)

        # Invalid pixel_list (list but contains non-string elements)
        with self.assertRaises(ValueError):
            pixel_pretender.apply_colorama_color([123, "valid string"], test_color)

        # Invalid text_color (not in _colors)
        with self.assertRaises(ValueError):
            pixel_pretender.apply_colorama_color(["▉▉▉"], "invalid_color")

        # ==== Edge Cases ====
        # Empty pixel_list
        pixel_list_empty = []
        result_empty = pixel_pretender.apply_colorama_color(pixel_list_empty, test_color)
        self.assertEqual(result_empty, [],
                         "Failed on empty pixel_list")

        # Very large pixel_list
        pixel_list_large = ["▉" * 50] * 1000  # 1000 lines of 50 characters
        result_large = pixel_pretender.apply_colorama_color(pixel_list_large, test_color)
        self.assertEqual(len(result_large), 1000,
                         "Failed on very large pixel_list size")
        self.assertTrue(result_large[0].startswith(test_color_code)
                        and result_large[-1].endswith(Fore.RESET)
                        and all(line == pixel_list_large[i] for i, line in enumerate(result_large[1:-1])),
                        "Failed to colorize large pixel_list correctly")
        # Pixel_list with one empty string
        pixel_list_empty_str = [""]
        result_empty_str = pixel_pretender.apply_colorama_color(pixel_list_empty_str, test_color)
        self.assertEqual(result_empty_str, [test_color_code + "" + Fore.RESET],
                         "Failed on pixel_list with one empty string")

        # Pixel_list with spaces
        pixel_list_spaces = ["   ", "▉▉ ", " ▉▉"]
        result_spaces = pixel_pretender.apply_colorama_color(pixel_list_spaces, test_color)
        expected_spaces = [
            test_color_code + pixel_list_spaces[0],
            pixel_list_spaces[1],
            pixel_list_spaces[2] + Fore.RESET
        ]
        self.assertEqual(result_spaces, expected_spaces,
                         "Failed on pixel_list with spaces")

    def test_apply_rich_color(self):
        # Valid input cases

        # Case 1: Basic valid input, no background color
        pixel_list = ["▉▉▉", " ▉ ", "▉▉▉"]
        text_color = "green"
        result = pixel_pretender.apply_rich_color(pixel_list, text_color)
        self.assertEqual(len(result), len(pixel_list), "Incorrect number of Text objects returned.")
        self.assertTrue(all(isinstance(line, Text) for line in result), "Result should contain Text objects.")
        self.assertTrue(all(line.style == f"green" for line in result), "Text color not applied correctly.")


        # Case 2: Text color and background color specified
        background_color = "black"
        result_bg = pixel_pretender.apply_rich_color(pixel_list, text_color, background_color)
        self.assertTrue(all(line.style == f"green on black" for line in result_bg),
                        "Text color and background color not applied correctly.")

        # Invalid input cases

        # Case 3: Invalid pixel_list type (e.g., not a list of strings)
        with self.assertRaises(TypeError):
            pixel_pretender.apply_rich_color("not_a_list", text_color)

        # Case 4: Invalid text color
        invalid_text_color = "invalid_color"
        result_invalid_color = pixel_pretender.apply_rich_color(pixel_list, invalid_text_color)

        # Check that the text has not changed from its default appearance
        # Here, we're assuming a simple original text appearance without color
        for i, line in enumerate(result_invalid_color):
            self.assertEqual(line.plain, pixel_list[i],
                             f"Text was altered when using invalid color: {line.plain} != {pixel_list[i]}")

        # Edge cases

        # Case 5: Empty pixel_list
        result_empty = pixel_pretender.apply_rich_color([], text_color)
        self.assertEqual(result_empty, [], "Expected an empty list for an empty pixel_list input.")

        # Case 6: Single line in pixel_list
        single_line = ["▉▉▉"]
        result_single = pixel_pretender.apply_rich_color(single_line, text_color)
        self.assertEqual(len(result_single), 1, "Should return a single Text object for single-line input.")
        # self.assertTrue(result_single[0].stylize(text_color), "Text color not applied correctly on single line.")
        self.assertTrue(all(line.style == f"green" for line in result), "Text color not applied correctly on single line.")

    def test_display_pixels(self):
        # Valid input with strings
        pixel_list = ["▉▉▉", " ▉ ", "▉▉▉"]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pixel_pretender.display_pixels(pixel_list)
            self.assertEqual(mock_stdout.getvalue(), "▉▉▉\n ▉ \n▉▉▉\n")

        # Valid input with Text objects
        mock_text_list = [Text("▉▉▉"), Text(" ▉ "), Text("▉▉▉")]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pixel_pretender.display_pixels(mock_text_list)
            self.assertEqual(mock_stdout.getvalue(), "▉▉▉\n ▉ \n▉▉▉\n")

        # Empty list input
        pixel_list_empty = []
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pixel_pretender.display_pixels(pixel_list_empty)
            self.assertEqual(mock_stdout.getvalue(), "")

        # Invalid input type (not a list)
        with self.assertRaises(TypeError):
            pixel_pretender.display_pixels("Not a list")  # Pass a string instead of a list

        # Invalid list elements (non-string and non-Text)
        with self.assertRaises(ValueError):
            pixel_pretender.display_pixels([123, 456, 789])  # Pass integers instead of strings or Text objects




if __name__ == "__main__":
    unittest.main()  # Run the tests
