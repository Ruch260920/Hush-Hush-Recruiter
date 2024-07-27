import openai
import json
#import sqlite3
from dotenv import load_dotenv
import os

def chatgpt(question, solution):
    load_dotenv()
   
    api_key = os.getenv('API_KEY')
 
    PROMPT = f"""
    Question: {question}
   
    The code solution is below and delimited by triple backticks:
    ```python
    {solution}
    ```
   
    YOUR RESPONSE SHOULD STRICTLY BE A JSON AND SHOULD FOLLOW THE FORMAT BELOW:
    {{"time_complexity": "O(n)", "space_complexity": "O(1)", "feedback": "The code is correct and efficient."}}
    """
 
    client = openai.Client(api_key=api_key)
 
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI code evaluator. You will be provided with a Question and a code snippet. You need to check the provided question and code snippet. And provide time & space complexity and also the feedback if any syntax errors and logical errors are found."},
            {"role": "user", "content": PROMPT}
        ]
    )
 
    # Extracting data from the response
    time_complexity = json.loads(completion.choices[0].message.content)['time_complexity']
    space_complexity = json.loads(completion.choices[0].message.content)['space_complexity']
    feedback = json.loads(completion.choices[0].message.content)['feedback']
   
    return time_complexity, space_complexity, feedback