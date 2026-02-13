# LLM4EM

The LLM4EM Pipeline is a tool that processes textual scenario descriptions to automatically generate For Enterprise Modeling (4EM) models. 
The resulting models are exported in `ADL` file format, which can be directly imported into the [4EM Modeling Toolkit](https://www.omilab.org/activities/projects/details/?id=86). 



## 🚀 Installation

1. Clone the repository
2. Create .venv
3. Install Requirements in the venv

## 📝 Usage
> [!IMPORTANT]
> Adjust the `script.py` file as needed for the desired LLM/API

Use the example textual scenario files (.txt) or place your own into the `scenarios/` folder

Run the pipeline: python src/script.py

The generated `ADL` files will be saved in the `output/models/` folder

## 🧩 Input Format Example
Textual scenarios should refer to the selected perspective for accurate parsing.

Examples:

[Goal] Improve Customer Satisfaction  
[Problem] Dissatisfaction with the Service  
[Information Set] Customer Survey Data  
[Actor] Customer Support Team  
[Resource] Feedback Form  
[Process] Collect Customer Feedback

## 🤝 Currently Supported 4EM Perspectives/Model Types
- Goals Model (GM)
- Actors and Resources Model (ARM)
- Business Process Model (BPM)
- Technical Components and Requirements Model (TRM)
- Products and Services Model (PM)
- Concepts Model (CM)

## 📤 Output Format
The output `ADL` files conform to the 4EM Modeling Toolkit standard in XML Syntax.

## ⚙️ Process of Model Generation

![alt text](https://github.com/benjaminnast/LLM4EM/blob/main/files/Toolchain.png)

## 📊 Application and Evaluation
First experiments and results using the LLM4EM Toolchain can be found [here](https://link.springer.com/chapter/10.1007/978-3-031-77908-4_8).
The full dataset can be found [here](https://zenodo.org/records/17360226).
