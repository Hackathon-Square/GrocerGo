import sqlite3
import random

# Predefined product names
PRODUCT_NAMES = [
    "apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple", "kiwi", "blueberry", "pear",
    "peach", "plum", "lemon", "lime", "mango", "cherry", "apricot", "pomegranate", "fig", "nectarine",
    "avocado", "coconut", "papaya", "cranberry", "raspberry", "blackberry", "gooseberry", "tangerine", "cantaloupe", "honeydew",
    "peanut", "almond", "cashew", "walnut", "pecan", "hazelnut", "macadamia", "pistachio", "sesame", "flaxseed",
    "quinoa", "amaranth", "barley", "oats", "wheat", "rice", "corn", "bulgur", "buckwheat", "sorghum",
    "potato", "carrot", "broccoli", "spinach", "lettuce", "cucumber", "tomato", "onion", "garlic", "ginger",
    "celery", "bell pepper", "mushroom", "zucchini", "eggplant", "asparagus", "cauliflower", "cabbage", "sweet potato", "pumpkin",
    "chicken", "beef", "pork", "lamb", "fish", "shrimp", "crab", "lobster", "clam", "oyster",
    "milk", "cheese", "yogurt", "butter", "cream", "eggs", "sour cream", "ice cream", "whipped cream", "cream cheese",
    "bread", "bagel", "muffin", "croissant", "roll", "biscuit", "pancake", "waffle", "crepe", "tortilla",
    "coffee", "tea", "espresso", "latte", "cappuccino", "macchiato", "mocha", "americano", "chai", "matcha"
]

# Generate fake market database
def generate_market_database(num_blocks, num_shelves_per_block, num_levels_per_shelf, num_products_per_level):
    market_database = []

    for block_id in range(1, num_blocks + 1):
        block_name = f"Block {block_id}"

        for shelf_number in range(1, num_shelves_per_block + 1):
            shelf_name = f"Shelf {shelf_number}"

            for level_number in range(1, num_levels_per_shelf + 1):
                level_name = f"Level {level_number}"

                for _ in range(num_products_per_level):
                    product_name = random.choice(PRODUCT_NAMES)
                    price = round(random.uniform(0.5, 100), 2)
                    stock = random.randint(0, 100)

                    product = {
                        'block': block_name,
                        'shelf': shelf_name,
                        'level': level_name,
                        'product_name': product_name,
                        'price': price,
                        'stock': stock
                    }

                    market_database.append(product)

    return market_database

# Create SQLite database and table
def create_database_table(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute('''CREATE TABLE Products
                 (Block TEXT, Shelf TEXT, Level TEXT, ProductName TEXT, Price REAL, Stock INTEGER)''')

    conn.commit()
    conn.close()

# Insert data into SQLite database
def insert_data_into_database(path, market_database):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    for product in market_database:
        c.execute("INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?)",
                  (product['block'], product['shelf'], product['level'], product['product_name'], product['price'], product['stock']))

    conn.commit()
    conn.close()

# Generate market database
num_blocks = 5
num_shelves_per_block = 10
num_levels_per_shelf = 3
num_products_per_level = 20
path = "db/market_database.db"

market_database = generate_market_database(num_blocks, num_shelves_per_block, num_levels_per_shelf, num_products_per_level)

# Create database table
create_database_table(path)

# Insert data into database
insert_data_into_database(path, market_database)

print(f"Market database has been created in {path}.")
