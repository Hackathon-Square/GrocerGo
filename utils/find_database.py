import sqlite3

def find_product(query):
    path = "./db/market_database.db"
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("SELECT * FROM Products WHERE ProductName LIKE ?", ('%' + query + '%',))
    products = c.fetchall()

    conn.close()

    return products




if __name__ == "__main__":

    query = "Banana"

    products = find_product(query)
    print(products)