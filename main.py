import pandas as pd
import os
import requests

def check_url_status(url):
    # Check if the URL is well-formed
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        return "Invalid URL format"

    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        # Check if the response is OK (200-299)
        if response.status_code == 200:
            return "OK"
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"  # Return the error message from the exception

def main(input_file, output_file):
    try:
        # Check if input file exists
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"The input file '{input_file}' does not exist.")

        # Read URLs from the input CSV file
        urls_data = pd.read_csv(input_file)

        # Check for the 'URL' column in the DataFrame
        if 'URL' not in urls_data.columns:
            raise KeyError("The input CSV file must contain a 'URL' column.")

        urls = urls_data['URL'].dropna().tolist()  # Drop NaN values and convert to list

        # Check if the URL list is empty
        if not urls:
            print("No URLs to check.")
            return

        results = []
        for url in urls:
            print(f"Checking: {url}")
            status = check_url_status(url)  # Check the URL status
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
    input_file = 'input_urls.csv'  # specify your input file name
    output_file = 'output_status.csv'  # specify your output file name
    main(input_file, output_file)
