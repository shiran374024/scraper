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
    chunk_number = 0
    chunk_size = 1000
    for chunk in MetaDataReader(data_dir,chunk_size).read():
        for row in chunk:
            web_driver = fetcher.get_web_driver(row.file_rein)
            content = FindElement(web_driver).find_element_by_class_name("ntee-category")
            if content:
                print(f"Content fetched for {row.file_rein}")
                row.category = content
            else:
                print(f"Failed to fetch content for {row.file_rein}")
    
        formater = FormatMenager(f"output_data_{chunk_number}.json")
        formater.save_to_file(chunk)
        print(f"Data saved to output_data_{chunk_number}.json")
    print("Process completed")

if __name__ == "__main__":
    main()