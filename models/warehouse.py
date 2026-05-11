from database.db_manager import get_connection

class Warehouse:
    def __init__(self, id=None, name=None, address=None):
        self.id = id
        self.name = name
        self.address = address

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute("INSERT INTO warehouses (name, address) VALUES (?, ?)",
                           (self.name, self.address))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE warehouses SET name=?, address=? WHERE id=?",
                           (self.name, self.address, self.id))

        conn.commit()
        conn.close()


def get_all_warehouses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM warehouses")
    rows = cursor.fetchall()
    conn.close()

    return [Warehouse(*row) for row in rows]