#!/usr/bin/env python
# encoding: utf-8
"""
Given an integer, output the Finnish word for that number.
"""
from __future__ import print_function, unicode_literals
import argparse

# https://fi.wikipedia.org/wiki/Suurten_lukujen_nimet

LESS_THAN_TEN = {
    0: "nolla",
    1: "yksi",
    2: "kaksi",
    3: "kolme",
    4: "neljä",
    5: "viisi",
    6: "kuusi",
    7: "seitsemän",
    8: "kahdeksan",
    9: "yhdeksän"
}
SINGULAR_TENS = {
    10: "kymmenen",
    100: "sata",
    1000: "tuhat",
    10**6: "miljoona",
    10**9: "miljardi",
    10**12: "biljoona",
    10**18: "triljoona",
    10**24: "kvadriljoona",
    10**30: "kvintiljoona",
    10**36: "sekstiljoona",
    10**42: "septiljoona",
    10**48: "oktiljoona",
    10**54: "noviljoona",
    10**60: "dekiljoona",
    10**66: "undekiljoona",
    10**72: "duodekiljoona",
    10**78: "tredekiljoona",
    10**84: "kvattuordekiljoona",
    10**90: "kvindekiljoona",
    10**96: "sedekiljoona",
    10**102: "septendekiljoona",
    10**108: "duodevigintiljoona",
    10**114: "undevigintiljoona",
    10**120: "vigintiljoona",
    10**126: "unvigintiljoona",
    10**180: "trigintiljoona",
    10**600: "sentiljoona",
}
# Just the few which don't have a simple -a partitive suffix
PLURAL_TENS = {
    10: "kymmentä",
    1000: "tuhatta",
}


def wordify(number, tens):
    if number == tens:
        return SINGULAR_TENS[tens]
    d, m = divmod(number, tens)
    if d > 1:
        if tens in PLURAL_TENS:
            plural = PLURAL_TENS[tens]
        else:
            plural = SINGULAR_TENS[tens] + "a"
        word = to_finnish(d) + plural
    else:
        word = SINGULAR_TENS[tens]
    if m > 0:
        word += to_finnish(m)
    return word


def find_tens_range(number):
    """
    Find where a number comes in the list of tens.
    Return the ten before (or equal to it), or None if out of range.
    """
    if number < 0:
        return None

    list_of_tens = sorted(SINGULAR_TENS.keys())

    import bisect
    n = bisect.bisect_left(list_of_tens, number)

    if list_of_tens[n:n+1] == [number]:
        return list_of_tens[n]
    else:
        return list_of_tens[n-1]


def to_finnish(number):
    if number >= 0 and number < 10:
        return LESS_THAN_TEN[number]
    elif number >= 11 and number <= 19:
        return LESS_THAN_TEN[number % 10] + "toista"
    elif number == 10 or number >= 20 and number <= 99:
        return wordify(number, 10)
    else:
        ten = find_tens_range(number)
        if ten:
            return wordify(number, ten)
        else:
            return "en tiedä"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Given an integer, "
                    "output the Finnish word for that number.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('number', type=int, help="An input integer")
    parser.add_argument(
        'end', nargs='?',  # type=int,
        help="An optional end integer. Prints all numbers from the first one "
             "up to this one. Use 'max' to keep going.")
    args = parser.parse_args()

    if not args.end:
        print(to_finnish(args.number))
    else:
        if args.end == "max":
            end = sorted(SINGULAR_TENS.keys())[-1]+1
        else:
            end = int(args.end)
        i = args.number
        while(i < end+1):
            print(i, to_finnish(i))
            i += 1

# End of file
