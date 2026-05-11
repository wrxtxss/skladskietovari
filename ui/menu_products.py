from models.product import Product, get_all_products

def menu_products():
    while True:
        print("\n=== Товары ===")
        print("1. Показать все")
        print("2. Добавить")
        print("3. Удалить")
        print("0. Назад")

        choice = input("Выбор: ")

        if choice == "1":
            products = get_all_products()
            for p in products:
                print(f"{p.id}. {p.name} | {p.price}")

        elif choice == "2":
            name = input("Название: ")
            article = input("Артикул: ")
            price = float(input("Цена: "))

            product = Product(name=name, article=article, price=price)
            product.save()

        elif choice == "3":
            id_ = int(input("ID: "))
            Product(id=id_).delete()

        elif choice == "0":
            break