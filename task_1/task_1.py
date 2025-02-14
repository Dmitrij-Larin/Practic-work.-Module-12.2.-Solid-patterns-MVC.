import json
import os


class Pizza:
    def __init__(self, name, base_price, ingredients):
        self.name = name
        self.base_price = base_price
        self.ingredients = ingredients
        self.toppings = []
        self.new_price = None

    def get_price(self):
        return self.base_price

    def get_price_with_toppings(self):
        self.new_price = self.base_price + len(self.toppings) * 25
        return self.new_price

    def add_topping(self, topping):
        self.toppings.append(topping)


class StandardPizza(Pizza):

    def __init__(self, name, base_price, ingredients):
        super().__init__(name, base_price, ingredients)


class CustomPizza(Pizza):
    def __init__(self, name, base_price, ingredients, toppings=None):
        super().__init__(name, base_price, ingredients)
        self.toppings = toppings

    def get_price(self):
        return self.base_price


class OrderService:
    def __init__(self):
        self.orders = []
        self.sales_count = 0
        self.total_revenue = 0.0
        self.load_orders()

    def place_order(self, pizza):
        self.orders.append(pizza)

    def create_order(self, pizza):
        self.orders.append(pizza)
        self.sales_count += 1
        self.total_revenue += pizza.get_price_with_toppings()
        self.save_orders()
        return pizza

    def save_orders(self):
        with open("orders.json", "w", encoding='utf-8') as fh:
            json.dump([pizza.__dict__ for pizza in self.orders], fh, ensure_ascii=False, indent=4)

    def load_orders(self):
        if os.path.exists("orders.json"):
            with open("orders.json", "r", encoding='utf-8') as fh:
                orders_data = json.load(fh)
                self.orders = [Pizza(o['name'], o['base_price'], o['ingredients']) for o in orders_data]

    def get_report(self):
        return self.sales_count, self.total_revenue


class ReportService:
    def __init__(self, order_service):
        self.order_service = order_service

    def generate_report(self):
        sales_count, total_revenue = self.order_service.get_report()
        return f"Количество заказов: {sales_count}, общая сумма: {total_revenue} руб."


class Menu:
    def __init__(self, order_service):
        self.order_service = order_service
        self.standard_pizzas = [
            StandardPizza("Гавайская", 575.0,
                          ["ветчина", "куриное филе", "соус BBQ", "ананасы", "черри", "пармезан", "моцарелла"]),
            StandardPizza("Ветчина и грибы", 520.0, ["ветчина", "шампиньоны", "красный лук", "моцарелла"]),
            StandardPizza("Сырный цыплёнок", 650.0,
                          ["курица", "дор блю", "брынза", "пармезан", "моцарелла", "томаты", "красный лук",
                           "соус чеддер"]),
            StandardPizza("Пепперони", 520.0, ["колбаски пепперони", "моцарелла"]),
            StandardPizza("Морской коктейль", 725.0, ["креветки", "кальмары", "тобико", "красный лук", "моцарелла"]),
        ]

    def add_pizza(self, pizza):
        self.standard_pizzas.append(pizza)

    def display_menu(self):
        print("\nМеню пиццы:")
        for i, pizza in enumerate(self.standard_pizzas):
            print(f"{i + 1}. {pizza.name} - {pizza.get_price()} руб.")

    def create_custom_pizza(self):
        name = input("Введите название вашей кастомной пиццы: ")
        ingredients = input("Введите ингредиенты через запятую: ").split(", ")
        toppings = (input("Введите топпинги через запятую: ")).split(", ")
        base_price = 400 + len(ingredients) * 50 + len(toppings) * 25
        return CustomPizza(name, base_price, ingredients, toppings)

    def run(self):
        while True:
            self.display_menu()
            print("9. Создать кастомную пиццу.")
            print("0. Выход.")
            choice = input("Выберите опцию: ")
            if choice == '0':
                break
            elif choice in map(str, range(1, 10)):
                if choice == '9':
                    pizza = self.create_custom_pizza()
                else:
                    pizza = self.standard_pizzas[int(choice) - 1]

                    add_toppings = input("Хотите добавить топпинг в пиццу:\n"
                                     "да или нет? ")
                    if add_toppings == "да":
                        toppings = input("Введите топпинги через запятую: ").split(", ")
                        for topping in toppings:
                            pizza.add_topping(topping.strip())
                            pizza.get_price()
                    elif add_toppings == "нет":
                        pizza = self.standard_pizzas[int(choice) - 1]
                    else:
                        pass

                order = self.order_service.create_order(pizza)
                print(f"Заказ: {order.name} - {order.get_price_with_toppings()} руб.")


class AdminInterface:
    def __init__(self, order_service, report_service: ReportService, menu: Menu):
        self.order_service = order_service
        self.report_service = report_service
        self.menu = menu

    def add_new_pizza(self):
        name = input("\nВведите название новой пиццы: ")
        price = float(input("Введите базовую цену пиццы: "))
        ingredients = input("Введите ингредиенты через запятую: ").split(", ")
        new_pizza = Pizza(name, price, ingredients)
        self.menu.add_pizza(new_pizza)
        print(f"Пицца '{name}' добавлена в меню.")

    def run(self):
        while True:
            print("\nПанель Администратора.")
            print("1. Посмотреть отчёт о продажах.")
            print("2. Создать новую пиццу.")
            print("0. Выход.")
            choice = input("Выберите опцию: ")

            if choice == '0':
                break
            elif choice == '1':
                total_sales, total_revenue = self.order_service.get_report()
                print(f"Количество заказов: {total_sales}, общая сумма: {total_revenue} руб.")
            elif choice == '2':
                admin_interface.add_new_pizza()


if __name__ == "__main__":
    order_service = OrderService()
    menu = Menu(order_service)
    report_service = ReportService(order_service)
    admin_interface = AdminInterface(order_service, report_service, menu)

    while True:
        print("\n1. Пользовательский интерфейс.")
        print("2. Администраторский интерфейс.")
        print("0. Выход.")
        choice = input("Выберите опцию: ")

        if choice == '0':
            break
        elif choice == '1':
            menu.run()
        elif choice == '2':
            admin_interface.run()
