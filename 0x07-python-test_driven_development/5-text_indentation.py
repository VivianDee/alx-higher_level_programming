#!/usr/bin/python3
"""
   text_indentation function
"""



def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print()
            print()
        else:
            if text[i] == ' ' and text[(i -1)] in ['.', '?', ':']:
                pass
            else:
                print(text[i], end="")
