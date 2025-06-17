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
load_dotenv('fr/.env')

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

def extract_latex(texte):
    pattern = r"```latex(.*?)```"
    match = re.search(pattern, texte, re.DOTALL)  # re.DOTALL permet de faire correspondre aussi les nouvelles lignes

    if match:
        # Retourner le contenu du bloc de code LaTeX
        return match.group(1).strip()
    else:
        return "Aucun bloc de code LaTeX trouvé."

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
                "content": "Voici le CV en LaTex à adapter : " + code_content,
            },
        ]
    )

    return extract_latex(chat_response.choices[0].message.content)

pre_prompt = "En tant qu'assistant d'aide à la rédaction d'un Curriculum Vitae. Votre tâche est d'analyser le CV en LaTex fourni pour adapter son code à l'offre d'emploi suivante : "

response = lechat_mistral(pre_prompt, "fr/heuzef_cv.tex", "fr/job.txt")

print(response)