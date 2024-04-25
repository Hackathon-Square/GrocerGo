import json

from managegoods.find_database import *
from managegoods.add_database import *
from managegoods.delete_database import *
from managegoods.update_database import *


def process_gpt(model_output):
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
    print(product_names)
    price = details["Price"]
    stock = details["Stock"]
    unit = "kg"
    product_id = fake.uuid4()

    # TODO
    # 根据账号识别用户权限

    # example
    authority = 1  # administrator
    authority = 0  # customer

    # TODO
    # 根据账号识别所绑定邮箱

    # example
    user_email = "fdubob233@gmail.com"

    # 根据动作调用相应的函数
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

                # TODO
                # Does the administrator need to refine the details of the addition based on customer?

                add_product(
                    block, shelf, level, product_name, price, unit, stock, product_id
                )
                print("Product added successfully.")

            else:
                print("You don't have permission to do this!!!!")
                send_an_email_to_customer(user_query, user_email)

        if authority == 1:

            add_product(
                block, shelf, level, product_name, price, unit, stock, product_id
            )
            print("Product added successfully.")

    elif action == "delete":

        if authority == 1:
            delete_product_by_info(product_name, block, shelf, level)
            print("Product deleted successfully.")

        else:
            print("You don't have permission to do this!!!!")
            send_an_email_to_customer(user_query, user_email)

    elif action == "update":

        if authority == 1:

            if price != None:
                update_product_price(product_name, block, shelf, level, price)
                print("Price updated successfully.")

            if stock != None:
                update_product_stock(product_name, block, shelf, level, stock)
                print("Stock updated successfully.")

            # TODO

            # it's combination of delete & add

            # if block != None:
            #     update_product_location(product_name, current_block, current_shelf, current_level, new_block, new_shelf, new_level)

        else:
            print("You don't have permission to do this!!!!")
            send_an_email_to_customer(user_query, user_email)
