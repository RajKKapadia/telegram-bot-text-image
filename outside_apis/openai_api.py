import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_image(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='1024x1024'
        )
        return {
            'status': 1,
            'url': response['data'][0]['url']
        }
    except:
        return {
            'status': 0,
            'url': ''
        }
        