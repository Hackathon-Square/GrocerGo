# -*- coding:utf-8 -*-

import openai


openai.api_base = "https://api.zhiyungpt.com/v1"
openai.api_key = "sk-mMag0QVCTbog5iJmA7Cb5a3047Ee4f0d8b81D2477a5b61Da"


def use_gpt(user_prompt):

    system_context = '''

    Given a user's inquiry, identify the user's intent among the four basic operations: add, delete, update, and find. In addition to focusing on the key object mentioned in the inquiry, this system also extracts additional parameters related to the database schema including Block, Shelf, Level, ProductName, Price, and Stock. When information about these parameters is mentioned or implied in the inquiry, they should be included in the output. The output should be formatted as follows:

    {
    "Action": "The CRUD action the user wants to take",
    "Details": {
        "Block": "The storage block, if specified",
        "Shelf": "The shelf number, if specified",
        "Level": "The level on the shelf, if specified",
        "ProductName": "The name of the product, in singular form",
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
        "ProductName": "banana",
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
        "ProductName": "apple",
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
        "ProductName": "orange",
        "Price": "5",
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
        "ProductName": "pineapple",
        "Price": null,
        "Stock": null
    }
    }

    Now, based on the user's inquiry, analyze and output the result in the specified format, ensuring the object is in singular form and that any available details are also captured.


    '''

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": system_context},
                {"role": "user", "content": user_prompt},
            ]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return str(e)



if __name__ == "__main__":

    user_prompt = "where is the banana?"
    model_output = use_gpt(user_prompt)
    print(model_output)
