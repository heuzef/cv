# AIjusTeX
# Author : Heuzef.com
# Version : 2025-07
# Intelligent assistant designed to fine-tune LaTeX-crafted CVs with precision and ease. 
# AjustiCVTeX leverages advanced AI to adapt your existing CV to better fit specific job offers, 
# ensuring your application stands out without altering its core integrity.
# Licence : Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
# Requirement : pip install -U langchain-mistralai
# To use, install the requirements, and configure your environment.
# export MISTRAL_API_KEY=your-api-key

########################################################################################################################

import os
import re
from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI

chat = ChatMistralAI(model="mistral-large-latest")

def lechat_mistral(pre_prompt, cv_path, job_path):

    with open(cv_path, 'r') as file:
        code_content = file.read()

    with open(job_path, 'r') as file:
        job_content = file.read()

    messages = [HumanMessage(content=pre_prompt + job_content + "Voici le CV en LaTex à adapter : " + code_content)]

    return print(chat.invoke(messages).content)

pre_prompt = "En tant qu'assistant d'aide à la rédaction d'un Curriculum Vitae. Votre tâche est d'analyser le CV en LaTex fourni pour adapter son code à l'offre d'emploi suivante : "

lechat_mistral(pre_prompt, "fr/heuzef_cv.tex", "fr/job.txt")