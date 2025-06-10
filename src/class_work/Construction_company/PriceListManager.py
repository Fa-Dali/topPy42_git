import json

class PriceListManager:
    def __init__(self, filename="prices.json"):
        self.filename = filename
        self.load_prices()

    def load_prices(self):
        try:
            with open(self.filename, encoding="utf-8") as file:
                self.prices = json.load(file)
        except FileNotFoundError:
            print("Файл с ценами не найден. Будет использован пустой прайс.")
            self.prices = {}
        except json.JSONDecodeError:
            print("Ошибка разбора JSON-файла. Будут использованы дефолтные цены.")
            self.prices = {}

    def save_prices(self):
        with open(self.filename, mode="w", encoding="utf-8") as file:
            json.dump(self.prices, file, ensure_ascii=False, indent=4)

    def set_price(self, item, price):
        self.prices[item] = price
        self.save_prices()

    def get_price(self, item):
        return self.prices.get(item, None)