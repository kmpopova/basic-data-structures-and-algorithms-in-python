import csv
import os

class Book:
    """
    Represents a book with its attributes.
    """

    def __init__(self, title: str, author: str, publication_year: str, genre: str):
        """
        Initializes a Book object.

        Args:
            title: The title of the book.
            author: The author of the book.
            publication_year: The year the book was published.
            genre: The genre of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Genre: {self.genre}"

def filter_books_by_author(csv_file_path: str, author_name: str):
    """
    Filters books in a given file by author.

    Args:
        csv_file_path: Path to the csv file.
        author_name: Author's name for filtering.

    Returns:
        A list of Book objects written by the specified author.
    """
    filtered_by_author = []
    try:
        with open(csv_file_path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if author_name.lower() == row['author'].lower():
                    book = Book(
                        title=row['title'],
                        author=row['author'],
                        publication_year=row['publication_year'],
                        genre=row['genre']
                    )
                    filtered_by_author.append(book)
    except FileNotFoundError:
        print("File does not exist.  Check the filename.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return filtered_by_author

def write_filtered_books_to_file(filtered_books: list, output_file_path: str):
    """
    Writes a list of Book objects to a file.

    Args:
        filtered_books: A list of Book objects.
        output_file_path: The path to the output file.
    """
        
    with open(output_file_path, 'w') as f:
        if filtered_books:
            for book in filtered_books:
                f.write(str(book) + "\n")
        else:
            print("There is no such author in the book list.")


if __name__ == "__main__":
    csv_file_path = "books.csv"
    author_name = input("Enter the author's name:") # e.g. J.R.R. Tolkien
    filtered_books = filter_books_by_author(csv_file_path, author_name)
    output_file_path = "books_by_author.txt"
    write_filtered_books_to_file(filtered_books, output_file_path)
    if os.path.exists(output_file_path) and os.path.getsize(output_file_path) != 0:
        print(f"The filtering is complete. You can find the information you requested in the file {output_file_path}.")