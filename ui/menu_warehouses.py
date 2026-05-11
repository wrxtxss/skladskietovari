from models.warehouse import Warehouse, get_all_warehouses

def menu_warehouses():
    while True:
        print("\n=== Склады ===")
        print("1. Показать все")
        print("2. Добавить")
        print("0. Назад")

        choice = input("Выбор: ")

        if choice == "1":
            warehouses = get_all_warehouses()
            for w in warehouses:
                print(f"{w.id}. {w.name} | {w.address}")

        elif choice == "2":
            name = input("Название склада: ")
            address = input("Адрес: ")

            warehouse = Warehouse(name=name, address=address)
            warehouse.save()

            print("✅ Склад добавлен")

        elif choice == "0":
            break

        else:
            print("❌ Неверный ввод")