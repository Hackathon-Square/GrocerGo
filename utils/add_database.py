import sqlite3
from faker import Faker

fake = Faker()

def add_product(block, shelf, level, product_name, price, unit, stock, product_id):
    conn = sqlite3.connect("./db/market_database.db")
    c = conn.cursor()

    c.execute("INSERT INTO Products (Block, Shelf, Level, ProductName, Price, Unit, Stock, ProductID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (block, shelf, level, product_name, price, unit, stock, product_id))
    conn.commit()

    conn.close()


if __name__ == "__main__":

    # Example usage:
    block = "Block 1"
    shelf = "Shelf 5"
    level = "Level 2"
    product_name = "Banana"
    price = 1.99
    unit = "kg"
    stock = 50
    product_id = fake.uuid4()

    add_product(block, shelf, level, product_name, price, unit, stock, product_id)
    print("Product added successfully.")
