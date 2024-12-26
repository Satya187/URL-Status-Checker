# URL Status Checker

**URL Status Checker** is a Python-based project that uses Selenium WebDriver to check the status of URLs by navigating to each URL, loading the webpage, and returning the status as either **Active** or **Inactive**. The results are then saved into an output CSV file for analysis.

## Features

- **Check URL status:** Validates whether a URL is active or not by loading the page in headless Chrome.
- **CSV Input/Output:** Reads a list of URLs from a CSV file and outputs the status of each URL to a new CSV file.
- **WebDriver Integration:** Uses Selenium WebDriver to automate browsing and check the page load status.
- **Handles Various Errors:** Catches errors such as invalid URLs, timeouts, or issues with the Chrome WebDriver.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.x
- Selenium
- Pandas
- ChromeDriver (to match your Chrome version)
  
You can install the required Python packages using the `requirements.txt` file.

### Install Dependencies

1. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Download ChromeDriver:**
   - Go to the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/) and download the version that matches your Chrome version.
   - Update the `service` path in the code with the location of the `chromedriver.exe`.

2. **Prepare the Input File:**
   - Create a CSV file (`input_urls.csv`) with the following structure:
     ```csv
     URL
     https://www.google.com
     https://www.github.com
     https://www.facebook.com
     ```

## Usage

1. **Run the script**:
   After setting up the environment and input file, you can run the script to check the URL statuses:

   ```bash
   python main.py
   ```

2. **Output**:
   - The results will be saved in an `output_status.csv` file, which will contain the URL and its status:
     ```csv
     URL,Status
     https://www.google.com,Active
     https://www.github.com,Active
     https://www.someinvalidurl.com,Inactive
     ```

## Project Structure

```
URL-Status-Checker/
│
├── .venv/              # Virtual environment folder
├── chromedriver/       # ChromeDriver executable
├── input_urls.csv      # Input CSV file with URLs
├── main.py             # Main Python script
├── requirements.txt    # List of Python dependencies
└── output_status.csv   # Output CSV file with URL status
```

## Contributing

1. Fork this repository.
2. Create a branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Create a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

### Notes:
- Replace `"MIT License"` with the appropriate license for your project if you're using a different one.
- You can add more specific instructions or details based on your project.

This `README.md` provides the essential information to run and understand your project, and will be helpful for others when contributing or using your repository!
