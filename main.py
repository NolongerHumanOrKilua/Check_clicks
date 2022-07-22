from dotenv import load_dotenv
import os
import requests
from urllib.parse import urlparse
import argparse

def shorten_link(bitlink_token, input_url):
    headers =  {"Authorization": f"Bearer {bitlink_token}"}
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    long_url = {"long_url": input_url}
    response = requests.post(url, json=long_url, headers=headers)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(bitlink_token, input_url):
    headers = {"Authorization": f"Bearer {bitlink_token}"}
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{input_url}/clicks/summary"
    parameters = {"unit": "day", "units": "-1"}
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()    
    return response.json()["total_clicks"]


def is_bitlink(bitlink_token, input_url):
    headers =  {"Authorization": f"Bearer {bitlink_token}"}
    parsed_bitlink = urlparse(input_url)
    parsed_bitlink = f"{parsed_bitlink.netloc}{parsed_bitlink.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_bitlink}"
    response = requests.get(url, headers=headers)
    return response.ok



def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("input_url")
    args = parser.parse_args()
    bitlink_token = os.environ['BITLINK_TOKEN']

    try:
        if not is_bitlink(bitlink_token, args.input_url):
            bitlink = shorten_link(bitlink_token, args.input_url)
            return print("Битлинк:", bitlink)               
        else:
            clicks_count = count_clicks(bitlink_token, args.input_url)
            return print("Переходов по вашей ссылке:", clicks_count)
    except requests.exceptions.HTTPError:
        return print("error")

      
if __name__ == "__main__":
    main()
    
