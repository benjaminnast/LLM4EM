import requests

def read_text_file(file_path):
    """Reads the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def call_openapi(text):
    """Sends a request to the OpenAPI API with the given text."""
    API_URL = "https://api.example.com/analyze"  # Replace with actual API URL
    API_KEY = "your_api_key"  # Replace with actual API key
    
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"input_text": text}
    
    response = requests.post(API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("result", "")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return ""

def main(txt_file):

    # DAS HIER ALLES ÜBERARBEITEN, SOWIE IN README BESCHRIEBEN @ALEX
    """Main function to read text, call API, and concatenate results."""
    file_content = read_text_file(txt_file)
    api_result = call_openapi(file_content)
    
    concatenated_result = file_content + "\n" + api_result
    
    print("Final Concatenated Output:")
    print(concatenated_result)
    
    return concatenated_result

if __name__ == "__main__":
    txt_file_path = "input.txt"  # Replace with actual file path
    main(txt_file_path)
