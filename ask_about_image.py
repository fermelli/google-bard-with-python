import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BARD_TOKEN')
bard = Bard(token=token)

image = open('image.jpg', 'rb').read()
bard_answer = bard.ask_about_image("Que es esta imagen?", image=image)['content']
print(bard_answer)