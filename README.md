This Python script utilizes the requests library to make an HTTP request to a webpage related to travel books, and BeautifulSoup to parse the HTML and extract relevant information. The target website is Books to Scrape.

Script Features:
HTML Elements and Page Structure:

Demonstrates the use of BeautifulSoup to find and print specific HTML elements like ul, div, and title.
Prints the prettified HTML structure of the webpage.
Result Counts and Site Title:

Extracts and prints the result counts and site title from the webpage.
Book Prices:

Scrapes and prints the prices of the books from the webpage.
Book Links and Names:

Extracts and prints both book links and names using different HTML tags.
Writing Book Names to File:

Utilizes a with statement to open a file named "books.txt" in write mode.
Writes each book name to a new line in the file using UTF-8 encoding.
