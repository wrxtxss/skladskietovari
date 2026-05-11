from database.db_manager import get_connection

class Product:
    def __init__(self, id=None, name=None, article=None, price=0, category_id=None, supplier_id=None):
        self.id = id
        self.name = name
        self.article = article
        self.price = price
        self.category_id = category_id
        self.supplier_id = supplier_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute("""
            INSERT INTO products (name, article, price, category_id, supplier_id)
            VALUES (?, ?, ?, ?, ?)
            """, (self.name, self.article, self.price, self.category_id, self.supplier_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
            UPDATE products
            SET name=?, article=?, price=?, category_id=?, supplier_id=?
            WHERE id=?
            """, (self.name, self.article, self.price, self.category_id, self.supplier_id, self.id))

        conn.commit()
        conn.close()

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id=?", (self.id,))
            conn.commit()
            conn.close()


def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()

    return [Product(*row) for row in rows]