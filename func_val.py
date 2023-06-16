from pprint import pprint
import requests
from api_key import api_key


def get_exchangeRate(pul1: str = "USD", pul2: str = "UZS") -> float:
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{pul1.upper()}/{pul2.upper()}"
    response = requests.get(url).json()['conversion_rate']
    return response


if __name__ == '__main__':
    print(get_exchangeRate())
