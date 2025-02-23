import os
from dotenv import load_dotenv
from meta_data_reader import MetaDataReader
from fetcher_factory import FetcherFactory
from format_menager import FormatMenager

# Load environment variables from .env file
load_dotenv()

def handle_content(content: str, file_rein: str) -> str|None:
    if content:
        print(f"Content fetched for {file_rein}")
        return content
    else:
        print(f"Failed to fetch content for {file_rein}")
        return None
    
def init():
    print("Starting the process")
    use_fetcher = os.getenv("FATCHER_NAME")
    print(f"Using fetcher: {use_fetcher}")
    fetcher = FetcherFactory().get_fatcher(
        use_fetcher,os.getenv("BASE_URL"))
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, "data")
    base_file_name =os.path.join("resultes","output_data ")
    formater = FormatMenager(base_file_name)
    chunk_size = int(os.getenv("BULK_SIZE"))
    chunk_number = 0
    return fetcher, data_dir, formater, chunk_size, chunk_number,base_file_name

 
def main():
    fetcher, data_dir, formater, chunk_size, chunk_number,base_file_name = init()
    for chunk in MetaDataReader(data_dir,chunk_size).read():
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
    fetcher.close()

if __name__ == "__main__":
    main()