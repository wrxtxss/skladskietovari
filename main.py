from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_products import menu_products
from ui.menu_warehouses import menu_warehouses

def main():
    initialize_db()

    while True:
        choice = show_main_menu()

        if choice == "1":
            menu_products()
        elif choice == "2":
            menu_warehouses()
        elif choice == "0":
            print("Выход...")
            break

if __name__ == "__main__":
    main()
