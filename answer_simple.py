import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BARD_TOKEN')
bard = Bard(token=token)
response = bard.get_answer("Que es el procesamiento de lenguaje natural?")['content']
print(response)