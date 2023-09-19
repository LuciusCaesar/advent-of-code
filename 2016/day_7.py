"""Day 7 Of the AoC 2016"""
import doctest
import re
from itertools import chain

with open("2016/day_7_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def return_outside_brackets(string: str) -> str:
    """Return a string where all between brackets have been removed"""
    s = string.replace("[", " ").replace("]", " ").split()
    return s[::2]


def return_inside_brackets(string: str) -> str:
    """
    >>> return_inside_brackets("abc[def]ghi")
    ['def']

    >>> return_inside_brackets("abc[def]ghi[jkl]mno")
    ['def', 'jkl']
    """
    s = string.replace("[", " ").replace("]", " ").split()
    return s[1::2]


def is_abba_pattern(s: str) -> bool:
    """
    >>> is_abba_pattern("abba")
    True

    >>> is_abba_pattern("aba")
    False

    >>> is_abba_pattern("aaabba")
    True
    """
    match = re.search(r"(.)(.)\2(?<!\1)(\1)", s)

    return match is not None


def is_abba_pattern_in_list(l: list) -> bool:
    """
    >>> is_abba_pattern_in_list(["abba", "abs"])
    True

    >>> is_abba_pattern_in_list(["def", "abs"])
    False

    >>> is_abba_pattern_in_list(["def", "qdmkoffoqsdoi"])
    True
    """
    result = [is_abba_pattern(string) for string in l]

    return True in result


def is_tls_supported_ip(ip: str) -> bool:
    """
    >>> is_tls_supported_ip("abba[abc]def")
    True

    >>> is_tls_supported_ip("abc[abba]def")
    False

    >>> is_tls_supported_ip("abc[def]abba")
    True

    >>> is_tls_supported_ip("abc[def]ghi[abba]xyz")
    False

    >>> is_tls_supported_ip("abc[def]ghi[xyz]abba")
    True



    >>> is_tls_supported_ip("abba[mnop]qrst")
    True

    >>> is_tls_supported_ip("abcd[bddb]xyyx")
    False

    >>> is_tls_supported_ip("aaaa[qwer]tyui")
    False

    >>> is_tls_supported_ip("ioxxoj[asdfgh]zxcvbn")
    True
    """
    return is_abba_pattern_in_list(
        return_outside_brackets(ip)
    ) and not is_abba_pattern_in_list(return_inside_brackets(ip))


def is_ssl_supported_ip(ip: str) -> bool:
    """
    >>> is_ssl_supported_ip("aba[bab]xyz")
    True

    >>> is_ssl_supported_ip("xyx[xyx]xyx")
    False

    >>> is_ssl_supported_ip("aaa[kek]eke")
    True

    >>> is_ssl_supported_ip("zazbz[bzb]cdb")
    True
    """
    match = re.search(r"(\w)(?=((\w)\1)\w*(\[|\])(.+\4)?\w*(\2\3))", ip)

    return match is not None


tls_supported_ips = [
    (line, is_tls_supported_ip(line))
    for line in lines
    if is_tls_supported_ip(line) is True
]

ssl_supported_ips = [
    (line, is_ssl_supported_ip(line)) for line in lines if is_ssl_supported_ip(line)
]

print(ssl_supported_ips)
print(len(ssl_supported_ips))
