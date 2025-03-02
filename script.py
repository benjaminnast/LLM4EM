
import requests
import sys
import glob
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
import postprocess as postprocess
from env import OPENAI_API_KEY

# Load environment variables
load_dotenv(".env")

API_KEY = OPENAI_API_KEY
MODEL = "gpt-4o"
FILES_FOLDER_PATH = r".\files"
SCENARIOS_FOLDER = "./scenarios"
OUTPUT_FOLDER = "output"
PREPROMPT_FOLDER = os.path.join(OUTPUT_FOLDER, "preprompts")
GENERATED_MODEL_FOLDER = os.path.join(OUTPUT_FOLDER, "models")

# Ensure output directories exist
os.makedirs(PREPROMPT_FOLDER, exist_ok=True)
os.makedirs(GENERATED_MODEL_FOLDER, exist_ok=True)

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)


def read_text_file(file_path):
    """Reads the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_text_file(file_path, content):
    """Saves the content to a text file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def call_openapi(text):
    """Calls the OpenAI API with the provided text."""
    messages=[
        [
            {
            "role": "assistant",
            "content": [
                {
                "type": "text",
                "text": "Du bist ein erfahrener Modellierungsexperte der schnell neue Techniken erlernt."
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": text
                }
            ]
            }
        ],
        [           
            {"role": "system", "content": "Du bist ein erfahrener Modellierungsexperte der schnell neue Techniken erlernt."},
            {"role": "user", "content": text}
        ]
    ]
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages[1]
    )
    return response.choices[0].message.content


def process_scenario(folder_path, scenario_content, scenario_file, iteration):
    """Processes a scenario with preprompt and prompt, saves results in appropriate folders."""
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if len(txt_files) != 2:
        print(f"Skipping {folder_path}, requires exactly 2 text files.")
        return

    preprompt = read_text_file(txt_files[0])
    prompt = read_text_file(txt_files[1])

    # --- Preprompt Stage ---
    combined_preprompt = preprompt + "\n" + scenario_content
    preprompt_result = call_openapi(combined_preprompt)

    preprompt_output_file = os.path.join(
        PREPROMPT_FOLDER,
        f"{scenario_file}_{iteration}_preprompt_result.txt"
    )
    save_text_file(preprompt_output_file, combined_preprompt + "\n" + preprompt_result)

    # --- Prompt Stage ---
    combined_prompt = prompt + "\n" + preprompt_result
    prompt_result = call_openapi(combined_prompt)
    prompt_result = postprocess.clean_code_text(prompt_result)

    scenario_file = scenario_file.replace(".txt", "")

    prompt_output_file = os.path.join(
        GENERATED_MODEL_FOLDER,
        f"{MODEL}_{scenario_file}_{iteration}.adl"
        # FIXME: ZEIT KANN GEGEN NUMMERIERUNG AUSGETAUSCHT WERDEN!
    )

    save_text_file(prompt_output_file, prompt_result)

    print(f"Results saved for {os.path.basename(folder_path)} under scenario.")

def run_scenario(iteration):
    """Main function to read scenarios, process files, and save outputs."""
    scenario_files = sorted(os.listdir(SCENARIOS_FOLDER))
    folder_paths = sorted(glob.glob(os.path.join(FILES_FOLDER_PATH, '*')))
    
    for scenario_file in scenario_files:
        scenario_content = read_text_file(os.path.join(SCENARIOS_FOLDER, scenario_file))

        for folder_path in folder_paths:
            folder_name = os.path.basename(folder_path)
            if folder_name in scenario_file:
                if os.path.isdir(folder_path):
                    process_scenario(folder_path, scenario_content, scenario_file, iteration)

    print("Processing complete.")

def main():
    for i in range(3):
        run_scenario(i)

if __name__ == "__main__":
    main()