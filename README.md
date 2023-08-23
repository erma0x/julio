
# Julio 🌶️

### Scraping Public Data from Websites

This is a Python program that scrapes information from medical professional related websites and saves it to a CSV file.

## Addictions

The program uses the following Python libraries:

- `csv`: For handling CSV files.
- `requests`: To make HTTP requests.
- `beautifulsoup4`: For parsing HTML.
- `collections`: To count the elements in a list.
- `re`: To execute regular expressions.
- `os`: For system operations such as checking for file existence.
- `subprocess`: To execute system commands like ping.
- `time`: For adding delays.

## Main Features

- `fetch_city_names()`: Fetch the city names from the provided url and return a list of names.
- `most_repeating_item(list)`: Find the most common item in a list using `Counter`.
- `get_links(url)`: Extract all links from a web page.
- `get_username(url)`: Extracts the username from a web page.
- `find_phone_number(url)`: Find phone numbers using regular expressions.
- `remove_duplicates_csv(input_file, output_file)`: Removes duplicates from a CSV file.
- `list_without_repeating(list)`: Returns a list with no duplicate elements.
- `is_id_present(file_path, id_value)`: Check if an ID is present in a CSV file.
- `add_datapoint_to_csv(file_path, datapoint)`: Add a datapoint to a CSV file.
- `create_empty_csv(file_path)`: Create an empty CSV file if it doesn't exist.
- `check_website_exists(link)`: Check if a website exists using ping.
- Main rationale for scraping information from websites.

## Usage

1. Make sure the listed dependencies are installed.
2. Run the Python `app.py` file.
3. The program will download information from various websites, filtering by medical professionals and specific cities, and save it in a CSV file.

Be sure to comply with local laws and website terms of use when scraping information.
