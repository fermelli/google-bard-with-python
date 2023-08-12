import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BARD_TOKEN')
bard = Bard(token=token)

audio = bard.speech("Hello world, my name is Bard")

with open("bard.ogg", "wb") as f:
    f.write(bytes(audio['audio']))
