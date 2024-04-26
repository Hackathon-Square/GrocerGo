import json

from managegoods.find_database import *
from managegoods.add_database import *
from managegoods.delete_database import *
from managegoods.update_database import *
from .interaction import *
from .intention import *


def process_gpt(user_query, user_email, authority):

    model_output = use_gpt(user_query)
    try:
        model_output_dict = json.loads(model_output)
    except json.JSONDecodeError:
        print("Error: model_output is not a valid JSON string.")

    # 提取动作和对象
    action = model_output_dict.get("Action")
    details = model_output_dict.get("Details")
    block = details["Block"]
    shelf = details["Shelf"]
    level = details["Level"]
    product_names = details["ProductName"]
    price = details["Price"]
    if price is None:
        price = fake.random_number(digits=2)
    stock = details["Stock"]
    if stock is None:
        stock = fake.random_number(digits=2)
    unit = "kg"
    product_id = fake.uuid4()
    print("========================")
    print(details)

    if action == "find":

        for product_name in product_names:
            result = find_product(product_name)
            print(result)

    elif action == "add":

        if authority == 0:

            confirm = send_message_and_wait_administrator_confirm(
                user_query, user_email
            )

            if confirm == 1:
                for product_name in product_names:
                    add_product(
                        block, shelf, level, product_name, price, unit, stock, product_id
                    )
                print("Product added successfully.")

            else:
                print("You don't have permission to do this!!!!")
                send_an_email_to_customer(user_query, user_email)

        if authority == 1:
            for product_name in product_names:
                add_product(
                    block, shelf, level, product_name, price, unit, stock, product_id
                )
            print("Product added successfully.")

    elif action == "delete":

        if authority == 1:
            for product_name in product_names:
                delete_product_by_info(product_name, block, shelf, level)
            print("Product deleted successfully.")

        else:
            confirm = send_message_and_wait_administrator_confirm(
                user_query, user_email
            )

            if confirm == 1:
                for product_name in product_names:
                    add_product(
                        block, shelf, level, product_name, price, unit, stock, product_id
                    )
                print("Product added successfully.")
            else:
                print("You don't have permission to do this!!!!")
                send_an_email_to_customer(user_query, user_email)

    elif action == "update":

        if authority == 1:
            if price != None:
                for product_name in product_names:
                    update_product_price(product_name, block, shelf, level, price)
                print("Price updated successfully.")

            if stock != None:
                for product_name in product_names:
                    update_product_stock(product_name, block, shelf, level, stock)
                print("Stock updated successfully.")

        else:
            confirm = send_message_and_wait_administrator_confirm(
                user_query, user_email
            )

            if confirm == 1:
                for product_name in product_names:
                    add_product(
                        block, shelf, level, product_name, price, unit, stock, product_id
                    )
                print("Product added successfully.")
            else:
                print("You don't have permission to do this!!!!")
                send_an_email_to_customer(user_query, user_email)
