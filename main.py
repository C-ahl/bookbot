import sys

from stats import count_words, count_characters, sort_dictionary

if not len(sys.argv) > 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


def get_book_text(filepath: str) -> str:
    """Read the content of a book file and return it as a string."""
    with open(filepath) as f:
        file_content = f.read()
        return file_content


def main() -> None:
    """Main function to read a book and calculate occurence of letters."""
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    letter_count = count_characters(book_text)
    letter_count_sorted = sort_dictionary(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in letter_count_sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
