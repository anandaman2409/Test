import multiprocessing
import requests
from bs4 import BeautifulSoup
import os


# Function to scrape data from a given URL
def scrape_data(url, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract some random data, e.g., all paragraph texts
        paragraphs = soup.find_all('p')
        data = "\n".join([para.get_text() for para in paragraphs])

        # Append the data to the file
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"Data from {url}:\n")
            file.write(data)
            file.write("\n\n")

    except requests.RequestException as e:
        print(f"Failed to scrape {url}: {e}")


if __name__ == "__main__":
    # List of websites to scrape
    urls = [
        'https://example.com',
        'https://httpbin.org',
        'https://en.wikipedia.org/wiki/Web_scraping',
        'https://openlibrary.org',
        'http://quotes.toscrape.com'
    ]

    # Output file name
    output_file = 'scraped_data.txt'

    # Ensure the file is empty before starting
    if os.path.exists(output_file):
        os.remove(output_file)

    # Create a pool of processes
    with multiprocessing.Pool(processes=5) as pool:
        pool.starmap(scrape_data, [(url, output_file) for url in urls])

    print(f"Data scraped and appended to {output_file}")