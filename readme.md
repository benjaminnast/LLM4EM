
The Grassroots Modeling Pipeline is a tool that processes textual scenarios to automatically generate 4EM (4-E Model) models. 
The resulting models are exported in `.adl` format, which can be directly imported into the 4EM modeling application.



## 🚀 Installation

1. Clone the repository:  
2. Create .venv
3. Install Requirements in the venv

📝 Usage
Place textual scenario files (.txt) into the scenarios/ folder.

Run the pipeline:

python src/script.py
The generated .adl files will be saved in the output/models/ folder.

🧩 Input Format Example
Textual scenarios should follow a structured format for accurate parsing:

Example:

[Goal] Improve customer satisfaction  
[Actor] Customer Support Team  
[Resource] Feedback Form  
[Task] Collect feedback after each service interaction  
[Dependency] Marketing Team provides survey templates 

📤 Output Format
The output .adl files conform to the 4EM modeling application standard in XML Syntax.
