# -*- coding:utf-8 -*-

import openai


openai.api_base = "https://api.zhiyungpt.com/v1"
openai.api_key = "sk-mMag0QVCTbog5iJmA7Cb5a3047Ee4f0d8b81D2477a5b61Da"


def use_gpt(user_prompt):

    system_context = '''

    Given a user's inquiry, identify the user's intent among the four basic operations: add, delete, update, and find. Focus particularly on the key object mentioned in the inquiry, converting it to its singular form, even if the inquiry suggests plural or multiple objects. The output should be formatted as follows:
   
    {
    "Action": "The CRUD action the user wants to take",
    "Object": "The key object mentioned in the inquiry in singular form"
    }

    Examples:

    Input: "Where can I find bananas?"
    Output: {"Action": "find", "Object": "banana"}

    Input: "Add new types of bananas to the inventory."
    Output: {"Action": "add", "Object": "banana"}

    Input: "Update the prices of bananas."
    Output: {"Action": "update", "Object": "banana"}

    Input: "Delete the expired bananas from the stock."
    Output: {"Action": "delete", "Object": "banana"}

    Now, based on the user's inquiry, analyze and output the result in the specified format, ensuring the object is in singular form.

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
