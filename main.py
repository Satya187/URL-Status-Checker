"""
Script to check the HTTP status of URLs from an input CSV file and save the results to an output CSV file.

This script reads a CSV file containing URLs, validates their format, and performs an HTTP HEAD request
on each URL to determine its status. The results are saved in another CSV file.

Dependencies:
    - pandas: For reading and writing CSV files.
    - requests: For performing HTTP requests.
    - os: For file system operations.

Functions:
    - check_url_status(url): Validates the URL format and checks its HTTP status.
    - main(input_file, output_file): Handles file reading, status checking, and results saving.

Usage:
    1. Prepare an input CSV file named 'input_urls.csv' with a column named 'URL' containing URLs to check.
    2. Run the script.
    3. The output will be saved in 'output_status.csv'.

Error Handling:
    - Ensures the input file exists.
    - Validates the presence of a 'URL' column in the input file.
    - Handles invalid URLs and network issues gracefully.
"""

import pandas as pd
import os
import requests

def check_url_status(url):
    """
    Validates a URL and checks its HTTP status.

    Args:
        url (str): The URL to check.

    Returns:
        str: The status of the URL (e.g., 'OK' or an error message).
    """
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        return "Invalid URL format"
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            return "OK"
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main(input_file, output_file):
    """
    Reads a CSV file containing URLs, checks their statuses, and writes the results to another CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        KeyError: If the input file does not contain a 'URL' column.
        pd.errors.EmptyDataError: If the input file is empty.
    """
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"The input file '{input_file}' does not exist.")

        # Read the input CSV file
        urls_data = pd.read_csv(input_file)

        # Check if 'URL' column exists
        if 'URL' not in urls_data.columns:
            raise KeyError("The input CSV file must contain a 'URL' column.")

        # Extract URLs and ensure they are not empty
        urls = urls_data['URL'].dropna().tolist()
        if not urls:
            print("No URLs to check.")
            return

        # Check the status of each URL
        results = []
        for url in urls:
            print(f"Checking: {url}")
            status = check_url_status(url)
            results.append({'URL': url, 'Status': status})

        # Save results to the output CSV file
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_file, index=False)
        print(f"Results saved to '{output_file}'")

    except (FileNotFoundError, KeyError, pd.errors.EmptyDataError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define input and output file paths
    input_file = 'input_urls.csv'
    output_file = 'output_status.csv'

    # Execute the main function
    main(input_file, output_file)
