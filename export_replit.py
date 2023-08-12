import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BARD_TOKEN')
bard = Bard(token=token)

bard_answer = bard.get_answer("Give me python code to conect to a database")
url = bard.export_replit(bard_answer['content'], bard_answer['program_lang'])
print(url)