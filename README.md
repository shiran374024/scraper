# Scraper Project

This project is a web scraping tool designed to fetch and process metadata from CSV files and web pages. The project uses Python and several libraries, including `pandas`, `selenium`, and `requests`.

## Requirements

- Python 3.7+
- `pandas`
- `selenium`
- `requests`


## Setup Instructions

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/scraper.git
    cd scraper
    ```

2. **Create a virtual environment and activate it:**
    - For Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the ChromeDriver and place it in your PATH.**  
   You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Usage

1. Place your CSV files in the `data` directory.

2. Run the main script:
    ```bash
    python scraiping_menager.py
    ```

    The script will read the CSV files, fetch the required web content, and save the processed data to `output_data.json`.

## Modules

- **meta_data.py**  
  Defines the `MetaData` class, which represents the metadata structure.

- **meta_data_reader.py**  
  Reads metadata from CSV files and creates `MetaData` objects.

- **fetch_content.py**  
  Fetches web content using Selenium WebDriver.

- **find_element.py**  
  Finds specific elements on a web page using Selenium.

- **format_menager.py**  
  Formats and saves the data to a JSON file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

