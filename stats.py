"""Module for text statistics."""


def count_words(text: str) -> int:
    """Count the number of words in a given text."""
    return len(text.split())


def count_characters(text: str) -> dict:
    """Count the number of characters in a given text."""
    text = text.lower()
    words = text.split()

    count = {}
    for word in words:
        letters = word.strip()
        for letter in letters:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
    return count


def sort_dictionary(dictionary: dict) -> list[dict]:
    """Sort a dictionary by its values in descending order and return a list of dictionaries."""
    new_list = []
    for key, value in dictionary.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def sort_on(items):
    """Sort function to sort items by the 'num' key in descending order."""
    return items["num"]
