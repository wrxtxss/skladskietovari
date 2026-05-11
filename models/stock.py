from database.db_manager import get_connection

class Stock:
    def __init__(self, id=None, product_id=None, warehouse_id=None, quantity=0):
        self.id = id
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.quantity = quantity

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute("""
            INSERT INTO stocks (product_id, warehouse_id, quantity)
            VALUES (?, ?, ?)
            """, (self.product_id, self.warehouse_id, self.quantity))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE stocks SET quantity=? WHERE id=?
            """, (self.quantity, self.id))

        conn.commit()
        conn.close()