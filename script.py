import requests
import sys
import glob
import os
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)
MODEL="gpt-4o-mini"


def read_text_file(file_path):
    """Reads the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def call_openapi(text):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"}, # <-- This is the system message that provides context to the model
            {"role": "user", "content": "Hello! Could you solve 2+2?"}  # <-- This is the user message for which the model will generate a response
        ]
    )
    print("Assistant: " + response.choices[0].message.content)
    

def main():
    # DAS HIER ALLES ÜBERARBEITEN, SOWIE IN README BESCHRIEBEN @ALEX
    """Main function to read text, call API, and concatenate results."""
    files_folder_path = r".\files"
    scenario_content = read_text_file("scenarios/Heat_pump-scenario_simple.txt")

    for file_path in glob.glob(os.path.join(files_folder_path, '**', '*.txt'), recursive=True):
        print(file_path)
        file_content = read_text_file(file_path)

        combined_content = scenario_content + "\n" + file_content
        api_result = call_openapi(combined_content)

        concatenated_result = combined_content + "\n" + api_result
        
        sys.exit()  # Beendet das Programm hier.



    sys.exit()  # Beendet das Programm hier.



    print("File Content:", file_content)
    sys.exit()  # Beendet das Programm hier.

    
    api_result = call_openapi(file_content)
    
    concatenated_result = file_content + "\n" + api_result
    
    print("Final Concatenated Output:")
    print(concatenated_result)
    
    return concatenated_result

if __name__ == "__main__":
    main()
