import requests
import os
from dotenv import load_dotenv
import argparse


load_dotenv()

BITLY_TOKEN = os.getenv('BITLY_TOKEN')

HEADERS = {
    'Authorization': f'Bearer {BITLY_TOKEN}'
    }

def is_bitlink(link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    res = requests.get(url, headers=HEADERS)
    return res.ok and 'long_url' in res.json()
        
def create_bitlink(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {
        'long_url': f'https://{link}',
        'domain': domain
        }
    res = requests.post(url, json=payload, headers=HEADERS)
    return res.json()['id']

def count_clicks(link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    res = requests.get(url, headers=HEADERS)
    return res.json()['total_clicks']
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='User can create bitlink or count clicks on an existing bitlink')
    parser.add_argument('link', help='Enter link to count clicks or create new bitlink ')
    parser.add_argument('--domain', help='Enter domain to create new bitlink')
    arguments = parser.parse_args()
    url, domain = arguments.link, arguments.domain
    
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.RequestException as err:
        print(err)
    else:
        _, reference = url.split('://')
        if is_bitlink(reference, BITLY_TOKEN):
            counter = count_clicks(reference, BITLY_TOKEN)
            print('Amount of clicks on user bitlink:', counter)
        else:
            print(create_bitlink(reference, BITLY_TOKEN))
