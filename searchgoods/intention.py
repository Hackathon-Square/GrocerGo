# -*- coding:utf-8 -*-

import openai
import random


openai.api_base = "https://api.chatgpt-4.net.cn/v1"
openai.api_key = "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"


def use_gpt(user_prompt):

    system_context = '''
    Given a user's inquiry, the system is designed to identify the user's intent among the four basic operations: add, delete, update, and find. The system extracts key parameters related to the database schema, including Block, Shelf, Level, ProductName, Price, and Stock. These parameters are crucial for accurately understanding and fulfilling the user's request. When multiple products are mentioned or implied in the inquiry, they should be listed under ProductName. The output format should strictly adhere to the following structure:

    {
    "Action": "The CRUD action the user wants to take",
    "Details": {
        "Block": "The storage block, if specified",
        "Shelf": "The shelf number, if specified",
        "Level": "The level on the shelf, if specified",
        "ProductName": ["List of product names, in singular form"],
        "Price": "The price of the product, if specified",
        "Stock": "The stock quantity, if specified"
    }
    }

    Examples:

    Input: "Where can I find bananas?"
    Output: {
    "Action": "find",
    "Details": {
        "Block": null,
        "Shelf": null,
        "Level": null,
        "ProductName": ["banana"],
        "Price": null,
        "Stock": null
    }
    }

    Input: "Where are the tomatoes and eggs?"
    Output: {
    "Action": "find",
    "Details": {
        "Block": null,
        "Shelf": null,
        "Level": null,
        "ProductName": ["tomato", "egg"],
        "Price": null,
        "Stock": null
    }
    }

    Input: "Add new types of apples to the inventory in Shelf 3 of Block A."
    Output: {
    "Action": "add",
    "Details": {
        "Block": "Block A",
        "Shelf": "3",
        "Level": null,
        "ProductName": ["apple"],
        "Price": null,
        "Stock": null
    }
    }

    Input: "Update the price of oranges to $5 per kg."
    Output: {
    "Action": "update",
    "Details": {
        "Block": null,
        "Shelf": null,
        "Level": null,
        "ProductName": ["orange"],
        "Price": "5",
        "Stock": null
    }
    }

    Input: "I'd like scrambled eggs with tomatoes tonight."
    Output: {
    "Action": "find",
    "Details": {
        "Block": null,
        "Shelf": null,
        "Level": null,
        "ProductName": ["egg", "tomato"],
        "Price": null,
        "Stock": null
    }
    }

    Input: "Delete the expired pineapples from the stock in Level 2 of Shelf 4."
    Output: {
    "Action": "delete",
    "Details": {
        "Block": null,
        "Shelf": "Shelf 4",
        "Level": "Level 2",
        "ProductName": ["pineapple"],
        "Price": null,
        "Stock": null
    }
    }

    Now, based on the user's inquiry, analyze and output the result in the specified format, ensuring that product names are in singular form and that any available details are also captured.
    '''

    try:
        response = openai.ChatCompletion.create(

            model = "gpt-4",
            messages=[
                {"role": "system", "content": system_context},
                {"role": "user", "content": user_prompt},
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return str(e)



if __name__ == "__main__":

    user_prompt = "I'd like to buy apples tonight"
    model_output = use_gpt(user_prompt)
    print(model_output)
