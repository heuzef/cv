# AIjusTeX
# Author : Heuzef.com
# Version : 2025-07
# Intelligent assistant designed to fine-tune LaTeX-crafted CVs with precision and ease. 
# AjustiCVTeX leverages advanced AI to adapt your existing CV to better fit specific job offers, 
# ensuring your application stands out without altering its core integrity.
# Licence : Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
# Requirement : pip install mistralai dotenv
########################################################################################################################

import os
import re
from mistralai import Mistral
from dotenv import load_dotenv
load_dotenv('.env')

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

def extract_latex(texte):
    pattern = r"```latex(.*?)```"
    match = re.search(pattern, texte, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return "No LaTeX code blocks found."

def lechat_mistral(pre_prompt, cv_path, job_path):
    client = Mistral(api_key=api_key)

    with open(cv_path, 'r') as file:
        code_content = file.read()

    with open(job_path, 'r') as file:
        job_content = file.read()

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": pre_prompt + job_content,
            },
            {
                "role": "user",
                "content": "Here is the LaTex CV to adapt: " + code_content,
            },
        ]
    )

    return extract_latex(chat_response.choices[0].message.content)

pre_prompt = "As a Curriculum Vitae assistant. Your task is to analyse the LaTex CV provided to adapt its code to the following job offer: "

response = lechat_mistral(pre_prompt, "en/heuzef_cv.tex", "en/job.txt")

print(response)