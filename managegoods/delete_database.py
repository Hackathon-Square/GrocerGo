import sqlite3

def delete_product_by_info(product_name, block, shelf, level):
    conn = sqlite3.connect("./db.sqlite3")
    c = conn.cursor()

    c.execute("DELETE FROM managegoods_product WHERE ProductName=? AND Block=? AND Shelf=? AND Level=?",
              (product_name, block, shelf, level))
    conn.commit()

    conn.close()


if __name__ == "__main__":

    # Example usage:
    product_name = "Banana"
    block = "Block 1"
    shelf = "Shelf 5"
    level = "Level 2"

    delete_product_by_info(product_name, block, shelf, level)
    print("Product deleted successfully.")
