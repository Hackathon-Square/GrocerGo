import os
import sqlite3
import random
from faker import Faker

fake = Faker()

# Generate fake market database
def generate_market_database(PRODUCT_CATEGORIES, PRODUCT_NAMES, PRODCT_UNITS, SHELF_LEVELS, shelf_num):
    market_database = []

    for category, block in PRODUCT_CATEGORIES.items():
        for product_name in PRODUCT_NAMES.get(category, []):
            level = random.choice(SHELF_LEVELS.get(category, []))
            if level is not None:
                shelf = random.randint(1, shelf_num)
            else:
                shelf = None
            price = round(random.uniform(0.5, 100), 2)
            unit = random.choice(PRODCT_UNITS.get(category, []))
            stock = round(1000*random.random(), 2) if unit == 'kg' else random.randint(0, 1000)
            product_id = fake.uuid4()

            product = {
                'block': block,
                'shelf': shelf,  # No specific shelf for categories without shelf levels
                'level': level,
                'product_name': product_name,
                'price': price,
                'unit': unit,
                'stock': stock,
                'product_id': product_id
            }

            market_database.append(product)

    return market_database

# Create SQLite database and table
def create_database_table(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute('''CREATE TABLE Products
                 (Block TEXT, Shelf TEXT, Level TEXT, ProductName TEXT, Price REAL, Unit TEXT, Stock REAL, ProductID TEXT)''')

    conn.commit()
    conn.close()

# Insert data into SQLite database
def insert_data_into_database(path, market_database):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    for product in market_database:
        c.execute("INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (product['block'], product['shelf'], product['level'], product['product_name'], product['price'], product['unit'], product['stock'], product['product_id']))

    conn.commit()
    conn.close()

# Define product categories and their corresponding blocks
PRODUCT_CATEGORIES = {
    'fruits_vegetables': 'Block A',
    'snacks_drinks': 'Block B',
    'clothes_shoes_hats': 'Block C',
    'sports_equipment': 'Block D',
    'personal_care': 'Block E'
}

# Predefined product names for each category
PRODUCT_NAMES = {
    'fruits_vegetables': ["apple", "banana", "orange", "grape", "strawberry", "carrot", "broccoli", "spinach", "lettuce", "watermelon", "pineapple", "kiwi", "blueberry", "pear", "peach", "plum"],
    'snacks_drinks': ["chips", "cookies", "soda", "water", "juice", "energy drink", "chocolate", "candy", "popcorn", "pretzels", "nuts", "crackers", "coffee", "tea", "milk", "smoothie"],
    'clothes_shoes_hats': ["t-shirt", "jeans", "jacket", "dress", "sneakers", "boots", "hat", "scarf"],
    'sports_equipment': ["basketball", "football", "soccer ball", "tennis racket", "yoga mat", "dumbbells", "jump rope"],
    'personal_care': ["shampoo", "soap", "toothpaste", "toothbrush", "deodorant", "razor", "lotion", "perfume"]
}

# Predefined product units for each product name
PRODCT_UNITS = {
    'fruits_vegetables': ["kg"],
    'snacks_drinks': ["piece"],
    'clothes_shoes_hats': ["piece"],
    'sports_equipment': ["piece"],
    'personal_care': ["piece"]
}

# Predefined shelf levels for each category
SHELF_LEVELS = {
    'fruits_vegetables': [None],
    'snacks_drinks': ["Level 1", "Level 2", "Level 3", "Level 4"],
    'clothes_shoes_hats': [None],
    'sports_equipment': ["Level 1", "Level 2", "Level 3"],
    'personal_care': ["Level 1", "Level 2", "Level 3", "Level 4"]
}

path = "db/market_database.db"

# Generate market database
market_database = generate_market_database(PRODUCT_CATEGORIES, PRODUCT_NAMES, PRODCT_UNITS, SHELF_LEVELS, 8)

if not os.path.exists(path):
    # Create database table
    create_database_table(path)

    # Insert data into database
    insert_data_into_database(path, market_database)

    print(f"Market database has been created in {path}.")
else:
    print(f"Market database already exists in {path}.")