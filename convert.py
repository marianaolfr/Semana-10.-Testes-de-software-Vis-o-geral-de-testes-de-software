def roman_to_integer(roman_numeral):
    """Converts a Roman numeral to an integer.

    Args:
        roman_numeral: A Roman numeral string.

    Returns:
        int: The corresponding integer value.
    """

    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    prev_value = 0

    for char in reversed(roman_numeral):
        current_value = roman_to_int[char]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value

    return result
