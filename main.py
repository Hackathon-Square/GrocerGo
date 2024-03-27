from aiiiiii.intention import use_gpt
from utils.find_database import *
import json

# user_query = "where is the banana?"
user_query = "where is the apple?"
model_output = use_gpt(user_query)

try:
    model_output_dict = json.loads(model_output)
except json.JSONDecodeError:
    print("Error: model_output is not a valid JSON string.")

# 提取动作和对象
action = model_output_dict.get("Action")
object_name = model_output_dict.get("Object")

# 根据动作调用相应的函数
if action == "find":
    result = find_product(object_name)
    print(result)


elif action == "add":
    pass


elif action == "delete":
    pass


elif action == "update":
    pass



