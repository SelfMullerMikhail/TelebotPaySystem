import os

from apiaqsi import (ApiAqsiClasses, CashiersAqsi, ClientsAqsi, DeviceAqsi,
                     GoodsAqsi, GoodsCategoryAqsi, OrdersAqsi, ReceiptsAqsi,
                     ShiftsAqsi, ShopsAqsi, Slips)
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
aqsi = ApiAqsiClasses(STRIPE_SECRET_KEY)

shops: ShopsAqsi = aqsi.get_shops()
devices: DeviceAqsi = aqsi.get_devices()
cashiers: CashiersAqsi = aqsi.get_cashiers()
receipts: ReceiptsAqsi = aqsi.get_receipts()
slips: Slips = aqsi.get_slips()
shifts: ShiftsAqsi = aqsi.get_shifts()
goodsCategory: GoodsCategoryAqsi = aqsi.get_goodsCategory()
clietns: ClientsAqsi = aqsi.get_clietns()
orders: OrdersAqsi = aqsi.get_orders()
goods: GoodsAqsi = aqsi.get_goods()

if __name__ == "__main__":
    ...
