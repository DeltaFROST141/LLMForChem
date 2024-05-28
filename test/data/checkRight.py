import json

file_path = 'fixed_database.json'

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("JSON 文件格式正确")
except json.JSONDecodeError as e:
    print(f"JSON 文件格式错误: {e}")
