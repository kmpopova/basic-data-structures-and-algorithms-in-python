"""
Define a function filter_books_by_author(csv_file_path, author_name):
This function should:
Take the path to the CSV file (csv_file_path) and an author's name (author_name) as input.
Open and read the books.csv file.
Iterate through the rows of the CSV file.
Filter the books to find books written by the specified author.
Return a list of dictionaries, where each dictionary represents a book and contains the keys title, 
author, publication_year, and genre.
"""
import csv
import os

def filter_books_by_author(csv_file_path: str, author_name: str):

    """
    Filters books in a given file by author.

    *args:
        csv_file_path: a string. Path to the csv file containing a list of books.
        author_name: a string. Name of the author for filtering. Case sensitive, 
        author's name and surname must be capitalized and separated by a space.

    Returns a list of dictionaries, each dictionary containing title, author name, publication year, genre.
    """

    filtered_by_author = []
    try:
        with open(csv_file_path) as f:
            for item in csv.reader(f):
                if author_name in item:
                    book = {'title': item[0], 'author': item[1], 'publication_year': item[2], 'genre': item[3]}
                    filtered_by_author.append(book)

    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print("File does not exist. Are you sure the file name you entered is correct?")
        else:
            print(f"Something went wrong: {e}")
    return filtered_by_author


def write_filtered_books_to_file(filtered_books: list, output_file_path: str):

    """
    Writes to file the list of books filtered by author's name.

    *args:
        filtered_books: a list of dictionaries, would be an output of the function filter_books_by_author
        output_file_path: name / path to the file to store the information from filtered_books

    Each dictionary is processed in a way that key-value pairs are modified for readability
    and then written into the output file. This way we don't need to know the dictionary
    structure in advance. 
    """
    if filtered_books:
        with open(output_file_path, 'w') as f:
            for item in filtered_books:
                for k, v in item.items():
                    f.write(f"{str(k).capitalize().replace('_', ' ')}: {v}. ")
                f.write("\n")
    else:
        print("There is no such author in the book list.")

if __name__ == "__main__":
    
    csv_file_path = "books.csv"
    author_name = input("Enter the author's name:")
    filtered_books = filter_books_by_author(csv_file_path, author_name) # e.g. J.R.R. Tolkien
    output_file_path = "books_by_author.txt"
    write_filtered_books_to_file(filtered_books, output_file_path)
    if os.path.getsize(output_file_path) != 0:
        print(f"The filtering is complete. You can find the information you requested in the file {output_file_path}.")