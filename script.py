import requests
import sys
import glob
import os
from dotenv import load_dotenv
from openai import OpenAI 
from datetime import datetime


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
            {"role": "system", "content": "Du bist ein erfahrener Modellierungsexperte der schnell neue Techniken erlernt."}, # <-- This is the system message that provides context to the model
            {"role": "user", "content": text}  # <-- This is the user message for which the model will generate a response
        ]
    )
    result = response.choices[0].message.content
    return result

def save_text_file(file_path, content):
    """Saves the content to a text file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # DAS HIER ALLES ÜBERARBEITEN, SOWIE IN README BESCHRIEBEN @ALEX
    """Main function to read text, call API, and concatenate results."""
    files_folder_path = r".\files"
    scenario_content = read_text_file("scenarios/Heat_pump-scenario_simple.txt")

    for folder_path in glob.glob(os.path.join(files_folder_path, '*'), recursive=True):
        if os.path.isdir(folder_path):
            txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
            if len(txt_files) == 2:
                preprompt = read_text_file(txt_files[0])
                prompt = read_text_file(txt_files[1])
                current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

                combined_content = preprompt + "\n" + scenario_content

                preprompt_result = call_openapi(combined_content)
                
                output_file_path = os.path.join("output",f"{os.path.basename(folder_path)}_{current_time}_preprompt_result.txt")
                output_file_content = combined_content + "\n" + preprompt_result
                save_text_file(output_file_path, output_file_content)
                
                combined_content = prompt + "\n" + preprompt_result
                
                prompt_result = call_openapi(combined_content)

                output_file_path = os.path.join("output",f"{os.path.basename(folder_path)}_{current_time}_prompt_result.txt")
                output_file_content = combined_content + "\n" + prompt_result
                save_text_file(output_file_path, output_file_content)

        
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
