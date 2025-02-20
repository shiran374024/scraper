import os
from meta_data_reader import MetaDataReader
from fetch_content import FetchContent
from find_element import FindElement
from format_menager import FormatMenager

def main():
    print("Starting the process")
    fetcher = FetchContent("https://projects.propublica.org/nonprofits/organizations/")
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, "data")
    formater = FormatMenager("output_data")
    chunk_number = 0
    
    for chunk in MetaDataReader(data_dir).read():
        for row in chunk:
            web_driver = fetcher.get_web_driver(row.file_rein)
            content = FindElement(web_driver).find_element_by_class_name("ntee-category")
            if content:
                print(f"Content fetched for {row.file_rein}")
                row.category = content
            else:
                print(f"Failed to fetch content for {row.file_rein}")
        
        formater.save_to_file(chunk, chunk_number)
        chunk_number += 1
    
    print("Process completed")
    
    # Close the WebDriver when done
    fetcher.close_web_driver()

if __name__ == "__main__":
    main()