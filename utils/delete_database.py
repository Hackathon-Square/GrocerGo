import sqlite3

def delete_product_by_info(path, product_name, block, shelf, level):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("DELETE FROM Products WHERE ProductName=? AND Block=? AND Shelf=? AND Level=?",
              (product_name, block, shelf, level))
    conn.commit()

    conn.close()

# Example usage:
path = "db/market_database.db"
product_name = "Banana"
block = "Block 1"
shelf = "Shelf 5"
level = "Level 2"

delete_product_by_info(path, product_name, block, shelf, level)
print("Product deleted successfully.")
