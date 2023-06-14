#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or roman_string == "":
        return None
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    s_case = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}
    decimal = sum(roman[character] for character in roman_string)
    length = len(roman_string)
    for i in range(length - 1):
        if roman[roman_string[i]] < roman[roman_string[i + 1]]:
            decimal += s_case.get(roman_string[i:i + 2], 0)
    return decimal
