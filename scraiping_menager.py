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
    base_file_name = "output_data"
    formater = FormatMenager(base_file_name)
    chunk_number = 0
    
    for chunk in MetaDataReader(data_dir).read():
        output_file = f"{base_file_name}_{chunk_number}.json"
        if os.path.exists(output_file):
            print(f"File {output_file} already exists. Skipping this chunk.")
            chunk_number += 1
            continue
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