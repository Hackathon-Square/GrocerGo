import sqlite3

def find_product(query):
    path = "./db.sqlite3"
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("SELECT * FROM managegoods_product WHERE ProductName LIKE ?", ('%' + query + '%',))
    products = c.fetchall()

    conn.close()

    return products




if __name__ == "__main__":

    query = "apple"

    products = find_product(query)
    print(products)