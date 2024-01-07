#!/usr/bin/env python

def read_book(book_file_name):
    with open("books/" + book_file_name + ".txt") as f:
        file_contents = f.read()
    return file_contents


def number_of_words(string_to_count):
    words_list = string_to_count.split()
    return len(words_list)


def alpha_unique_count(string_to_count):
    results = {}

    for c in string_to_count.lower():
        if c not in results.keys() and c.isalpha():
            results[c] = 1
        elif c.isalpha():
            results[c] += 1
        else:
            next

    return results


def print_report(book_to_read, book_text):
    print(f"--- Begin report of books/{book_to_read}.txt ---")
    
    book_word_count = number_of_words(book_text)
    print(f"{book_word_count} words found in the document.")

    alpha_counts = alpha_unique_count(book_text)
    ordered_alpha_counts = sorted(alpha_counts.items(), key=lambda x: x[1], reverse=True)

    for letter in ordered_alpha_counts:
        print(f"The '{letter[0]}' character was found {letter[1]} times.")
    

def main():
    book_to_read = "frankenstein"
    book_text = read_book(book_to_read)
    
    print(book_text)
    print_report(book_to_read, book_text)


if __name__ == '__main__':
    main()
