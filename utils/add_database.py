import sqlite3

def add_product(path, block, shelf, level, product_name, price, stock):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("INSERT INTO Products (Block, Shelf, Level, ProductName, Price, Stock) VALUES (?, ?, ?, ?, ?, ?)",
              (block, shelf, level, product_name, price, stock))
    conn.commit()

    conn.close()

# Example usage:
path = "db/market_database.db"
block = "Block 1"
shelf = "Shelf 5"
level = "Level 2"
product_name = "Banana"
price = 1.99
stock = 50

add_product(path, block, shelf, level, product_name, price, stock)
print("Product added successfully.")
