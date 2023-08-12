import os
from bardapi import Bard
from dotenv import load_dotenv


load_dotenv()

token = os.environ['BARD_TOKEN']
bard = Bard(token=token)

prompt='''
What is a LLM?
The answer format should be the following.

answer: {
[
  id: 1,
  content: draft1
],
 id: 2,
  content: draft2
]
}
'''
response = bard.get_answer(prompt)['content']
print(response)