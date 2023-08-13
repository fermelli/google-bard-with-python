from datetime import datetime
import os
from bardapi import Bard
from dotenv import load_dotenv
import requests

load_dotenv()

token = os.getenv('BARD_TOKEN')
session = requests.Session()
session.headers = {
    'Host': 'bard.google.com',
    'X-Same-Domain': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://bard.google.com',
    'Referer': 'https://bard.google.com/',
}
session.cookies.set('__Secure-1PSID', token)

bard = Bard(token=token, session=session)

try:
    if not os.path.exists('conversations'):
        os.makedirs('conversations')

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = f'conversations/{timestamp}_conversation.txt'

    while True:
        print('Enter prompt (press Enter twice to finish):')
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)

        prompt = '\n'.join(lines)

        response = bard.get_answer(prompt)['content']
        print(response)

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(str(datetime.now()) + '\n')
            file.write(prompt + '\n')
            file.write(response + '\n')
            file.write('\n')

except Exception as e:
    print(e)
    print('Something went wrong. Please try again.')
