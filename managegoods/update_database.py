import sqlite3

def update_product_location(product_name, current_block, current_shelf, current_level, new_block, new_shelf, new_level):
    conn = sqlite3.connect(path = "./db.sqlite3")
    c = conn.cursor()

    c.execute("UPDATE managegoods_product SET Block=?, Shelf=?, Level=? WHERE ProductName=? AND Block=? AND Shelf=? AND Level=?",
              (new_block, new_shelf, new_level, product_name, current_block, current_shelf, current_level))
    conn.commit()

    conn.close()

def update_product_stock(product_name, block, shelf, level, new_stock):
    conn = sqlite3.connect(path = "./db.sqlite3")
    c = conn.cursor()

    c.execute("UPDATE managegoods_product SET Stock=? WHERE ProductName=? AND Block=? AND Shelf=? AND Level=?",
              (new_stock, product_name, block, shelf, level))
    conn.commit()

    conn.close()

def update_product_price(product_name, block, shelf, level, new_price):
    conn = sqlite3.connect(path = "./db.sqlite3")
    c = conn.cursor()

    c.execute("UPDATE managegoods_product SET Price=? WHERE ProductName=? AND Block=? AND Shelf=? AND Level=?",
              (new_price, product_name, block, shelf, level))
    conn.commit()

    conn.close()


if __name__ == "__main__":

    # Example usage:
    product_name = "Banana"
    current_block = "Block 1"
    current_shelf = "Shelf 5"
    current_level = "Level 2"
    new_block = "Block 2"
    new_shelf = "Shelf 3"
    new_level = "Level 1"

    update_product_location(product_name, current_block, current_shelf, current_level, new_block, new_shelf, new_level)
    print("Location information updated successfully.")

    # Example usage for updating stock:
    product_name = "Banana"
    block = "Block 1"
    shelf = "Shelf 5"
    level = "Level 2"
    new_stock = 60

    update_product_stock(product_name, block, shelf, level, new_stock)
    print("Stock updated successfully.")

    # Example usage for updating price:
    product_name = "Banana"
    block = "Block 1"
    shelf = "Shelf 5"
    level = "Level 2"
    new_price = 2.25

    update_product_price(product_name, block, shelf, level, new_price)
    print("Price updated successfully.")
