import os
from meta_data_reader import MetaDataReader
from fetch_content import FetchContent
from find_element import FindElement
from format_menager import FormatMenager

def main():
    fetcher = FetchContent("https://projects.propublica.org/nonprofits/organizations/")
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, "data")
    row_data = MetaDataReader(data_dir).get_data()
    for row in row_data:
        web_driver = fetcher.get_web_driver(row.file_rein)
        content = FindElement(web_driver).find_element_by_class_name("ntee-category")
        if  content:
            print(f"Content fetched for {row.file_rein}")
            row.category = content
        else:
            print(f"Failed to fetch content for {row.file_rein}")

    formater = FormatMenager("output_data.json")
    formater.save_to_file(row_data)
    print("Data saved to output_data.json")

if __name__ == "__main__":
    main()