import sqlite3

def find_product(path, query):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("SELECT * FROM Products WHERE ProductName LIKE ?", ('%' + query + '%',))
    products = c.fetchall()

    conn.close()

    return products

# Example usage:
path = "db/market_database.db"
query = "Banana"

products = find_product(path, query)
print(products)