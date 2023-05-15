import os
import threading
from dotenv import load_dotenv
from apiaqsi import ApiAqsiClasses
from apiaqsi.aqsi_types.aqsi_types import *
from apiaqsi import ShopsAqsi
from apiaqsi import DeviceAqsi
from apiaqsi import CashiersAqsi
from apiaqsi import ReceiptsAqsi
from apiaqsi import Slips
from apiaqsi import ShiftsAqsi
from apiaqsi import GoodsAqsi
from apiaqsi import GoodsCategoryAqsi
from apiaqsi import ClientsAqsi
from apiaqsi import OrdersAqsi

from tg_chat import TgChat
from mailing.mailing_1 import Mailing1

dotenv_path = os.path.join(os.path.dirname(__file__), '', 'env_file.env')
load_dotenv(dotenv_path=dotenv_path)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
aqsi = ApiAqsiClasses(STRIPE_SECRET_KEY)

shops:ShopsAqsi = aqsi.get_shops()
devices:DeviceAqsi = aqsi.get_devices()
cashiers:CashiersAqsi = aqsi.get_cashiers()
receipts:ReceiptsAqsi = aqsi.get_receipts()
slips:Slips = aqsi.get_slips()
shifts:ShiftsAqsi = aqsi.get_shifts()
goodsCategory :GoodsCategoryAqsi= aqsi.get_goodsCategory()
clietns:ClientsAqsi = aqsi.get_clietns()
orders:OrdersAqsi = aqsi.get_orders()
goods:GoodsAqsi = aqsi.get_goods()

if __name__=="__main__":
    bot = TgChat(TELEGRAM_TOKEN)
    mailing = Mailing1()
    
    malling = threading.Thread(target=mailing.example_func, args=())
    tg_bot = threading.Thread(target=bot.start, args=())
    malling.start()
    tg_bot.start()