import os

from dotenv import load_dotenv
from binance.client import Client


def get_client():
    """
    Create and return a Binance client using API credentials
    stored in the .env file.
    """

    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
   

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )

    return client