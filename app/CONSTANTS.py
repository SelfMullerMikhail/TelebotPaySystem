BUTTON_SHOPS = "🏠 Кофейни ..."
BUTTON_CONTACT_INFO = "☎️ Контактная информация ..."
BUTTON_SETTINGS = "⚙️ Настройки аккаунта ..."
BUTTON_STOCK = '📈 Акции ...'
BUTON_MENU = '📖 Menu'
BUTTON_BASKET = "🧺 Корзина ..."
CONTROLL_PANEL = "Панель управления"
APPROVE_TEXT = '❌ Approve ...'
DONE_TEXT = "✅ Done ..."

BOT_COMMANDS = [
    ("/start", "🫡 Старт"),
    ("/order", "📝 Заказ"),
    ("/previous", "🧷 Предыдущий заказ ..."),
    ("/basket", "🧺 Корзина ..."),
    ("/history", "📖 История заказов ...")]


def get_order_info(discount, discount_money, summ, city, address):
    info = f"""
    {city}
    {address}
    Скидка: {discount}%: {discount_money} ₽
    К оплате: {summ} ₽"""
    return info
