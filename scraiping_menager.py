import os
from meta_data_reader import MetaDataReader
from fetch_content import PlaywrightFetchContent, SeleniumFetchContent
from format_menager import FormatMenager


def handle_content(content: str, file_rein: str) -> str|None:
    if content:
        print(f"Content fetched for {file_rein}")
        return content
    else:
        print(f"Failed to fetch content for {file_rein}")
        return None

def main():
    print("Starting the process")
    use_playwright = True
    fetcher = None
    if use_playwright:
        fetcher = PlaywrightFetchContent("https://projects.propublica.org/nonprofits/organizations/")
    else:
        fetcher = SeleniumFetchContent("https://projects.propublica.org/nonprofits/organizations/")
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, "data")
    base_file_name =os.path.join("resultes","output_data")
    formater = FormatMenager(base_file_name)
    chunk_number = 0
    
    for chunk in MetaDataReader(data_dir).read():
        output_file = f"{base_file_name}_{chunk_number}.json"
        if os.path.exists(output_file):
            print(f"File {output_file} already exists. Skipping this chunk.")
            chunk_number += 1
            continue
        for row in chunk:
            content = fetcher.find_element(row.file_rein)
            handle_content(content, row.file_rein)
            row.category = content
        
        formater.save_to_file(chunk, chunk_number)
        chunk_number += 1
    
    print("Process completed")     
    
    # Close the WebDriver when done 
    fetcher.close_web_driver()

if __name__ == "__main__":
    main()