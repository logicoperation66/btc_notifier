from dotenv import load_dotenv
from statistics_func import price_calculate
from notofications import phone_notifier

load_dotenv()

def main():
    phone_notifier(btc_price=price_calculate())
    return 0


if __name__ == "__main__":
    main()
