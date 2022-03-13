import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv
from pathlib import Path


def shorten_link(token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': f'Bearer {token}'}
    body = {"long_url": url}
    response = requests.post(bitly_url, headers=header, json=body)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, bitlink):
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    header = {'Authorization': f'Bearer {token}'}
    response = requests.get(bitly_url, headers=header)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, bitlink):
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    header = {'Authorization': f'Bearer {token}'}
    response = requests.get(bitly_url, headers=header)
    return response.ok


def remove_protocol(url):
    parsed_url = urlparse(url)
    return f'{parsed_url.netloc}{parsed_url.path}'


def url_from_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL для анализа')
    args = parser.parse_args()
    return args.url


if __name__ == '__main__':
    env_path = Path('.') / 'bit.env'
    load_dotenv(dotenv_path=env_path)
    token = os.environ['BITLY_TOKEN']
#   url = input('Input url: ')
    url = url_from_cmdline()
    try:
        if is_bitlink(token, remove_protocol(url)):
            print(url, 'is a correct bitlink')
            print('Total clicks:', count_clicks(token, remove_protocol(url)))
        else:
            print(url, 'may be complete URL')
            print('Bitlink:', shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print('Can not get answer from bit.ly. Check request url')
