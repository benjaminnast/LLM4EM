
The LLM4EM Pipeline is a tool that processes textual scenario descriptions to automatically generate For Enterprise Modeling (4EM) models. 
The resulting models are exported in `.adl` format, which can be directly imported into the 4EM Modeling Toolkit.
https://www.omilab.org/activities/projects/details/?id=86 



## 🚀 Installation

1. Clone the repository
2. Create .venv
3. Install Requirements in the venv

## 📝 Usage
Use the example textual scenario files (.txt) or place your own into the scenarios/ folder.

Run the pipeline: python src/script.py

The generated .adl files will be saved in the output/models/ folder.

## 🧩 Input Format Example
Textual scenarios should refer to the selected perspective for accurate parsing.

Examples:

[Goal] Improve Customer Satisfaction
[Problem] Dissatisfaction with the Service
[Information Set] Customer Survey Data
[Actor] Customer Support Team
[Resource] Feedback Form
[Process] Collect Customer Feedback

## 🤝 Currently Supported 4EM Perspectives/Model Types:
- Goals Model (GM)
- Actors and Resources Model (ARM)
- Process Model (PM)
- Technical Components Model (TC)
- Products and Services Model (PS)
- Concepts Model (CM)

## 📤 Output Format
The output .adl files conform to the 4EM Modeling Toolkit standard in XML Syntax.

## ⚙️ Process of Model Generation

![alt text](https://github.com/benjaminnast/LLM4EM/blob/main/files/Toolchain.png)
