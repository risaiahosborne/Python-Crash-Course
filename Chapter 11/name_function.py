def get_formatted_name(first, last, middle =''):
    """
    Generate a neatly formatted full name.

    Parameters:
        first (str): The first name.
        middle (str): The middle name (can be empty or None).
        last (str): The last name.

    Returns:
        str: The full name, neatly formatted.
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
