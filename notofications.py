import pushbullet
from os import getenv


def phone_notifier(btc_price: float) -> bool:
    pb = pushbullet.PushBullet(getenv("pushbullet_token"))
    if isinstance(btc_price, float):
        pb.push_note("BTC_NOTIFIER", f"CENA BTC : {btc_price}zł")
        return True
    else:
        pb.push_note("BTC_NOTIFIER", f"Coś jest nie tak {btc_price}")
        return False
