import requests
import os
import glob
from dotenv import load_dotenv
from datetime import datetime
import postprocess
from openai import OpenAI

# Load environment variables
load_dotenv()

# Constants
FILES_FOLDER_PATH = r".\files"
SCENARIOS_FOLDER = "./scenarios"
OUTPUT_FOLDER = "output"
PREPROMPT_FOLDER = os.path.join(OUTPUT_FOLDER, "preprompts")
GENERATED_MODEL_FOLDER = os.path.join(OUTPUT_FOLDER, "models")

# Ensure output directories exist
os.makedirs(PREPROMPT_FOLDER, exist_ok=True)
os.makedirs(GENERATED_MODEL_FOLDER, exist_ok=True)

# Utility Functions
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_text_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def call_api(client, model, messages):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

# Scenario Processing
def process_scenario(client, model, folder_path, scenario_content, scenario_file, iteration):
    scenario_file = scenario_file.replace(".txt", "")

    prompt_output_file = os.path.join(
        GENERATED_MODEL_FOLDER,
        f"{model}_{scenario_file}_{iteration}.adl"
    )

    if os.path.exists(prompt_output_file):
        print(f"File {prompt_output_file} already exists. Skipping.")
        return

    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if len(txt_files) != 2:
        print(f"Skipping {folder_path}, requires exactly 2 text files.")
        return

    preprompt = read_text_file(txt_files[0])
    prompt = read_text_file(txt_files[1])

    # Preprompt Stage
    combined_preprompt = preprompt + "\n" + scenario_content
    preprompt_result = call_api(client, model, [
        {"role": "system", "content": "You are an expert modeler."},
        {"role": "user", "content": combined_preprompt}
    ])

    preprompt_output_file = os.path.join(
        PREPROMPT_FOLDER,
        f"{scenario_file}_{iteration}_preprompt_result.txt"
    )
    save_text_file(preprompt_output_file, combined_preprompt + "\n" + preprompt_result)

    # Prompt Stage
    combined_prompt = prompt + "\n" + preprompt_result
    prompt_result = call_api(client, model, [
        {"role": "user", "content": combined_prompt}
    ])
    prompt_result = postprocess.clean_code_text(prompt_result)

    save_text_file(prompt_output_file, prompt_result)
    print(f"Results saved for {os.path.basename(folder_path)} under scenario.")

# Scenario Runner
def run_scenario(client, model, iteration):
    scenario_files = sorted(os.listdir(SCENARIOS_FOLDER))
    folder_paths = sorted(glob.glob(os.path.join(FILES_FOLDER_PATH, '*')))

    for scenario_file in scenario_files:
        scenario_content = read_text_file(os.path.join(SCENARIOS_FOLDER, scenario_file))

        for folder_path in folder_paths:
            folder_name = os.path.basename(folder_path)
            if folder_name in scenario_file:
                if os.path.isdir(folder_path):
                    process_scenario(client, model, folder_path, scenario_content, scenario_file, iteration)

    print("Processing complete.")

# Main Function
def main():
    api_type = "gemini"  # Change to "openrouter" for OpenRouter Gemini
    api_key = os.getenv("GOOGLE_API_KEY")
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

    model = "gemini-2.5-flash"  # Change model as needed

    client = OpenAI(api_key=api_key, base_url=base_url)

    for i in range(3):
        run_scenario(client, model, i)

if __name__ == "__main__":
    main()