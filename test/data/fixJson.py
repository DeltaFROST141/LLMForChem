import json
import re

# TODO 值内双引号转义问题仍未解决。
def escape_quotes_in_value(value):
    """
    检查并修复字符串值中的双引号转义问题
    """
    # 如果找到未转义的双引号（即双引号前不是反斜杠），则将其转义
    corrected_value = re.sub(r'(?<!\\)"', r'\\"', value)
    return corrected_value

def fix_newline_quotes(value):
    """
    修复字符串值中右引号不在同一行的问题
    """
    corrected_value = re.sub(r'\n"', r'"', value)
    return corrected_value

def fix_json_values(data):
    """
    递归检查并修复 JSON 数据中的双引号问题
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                value = escape_quotes_in_value(value)
                value = fix_newline_quotes(value)
                data[key] = value
            else:
                fix_json_values(value)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, str):
                item = escape_quotes_in_value(item)
                item = fix_newline_quotes(item)
                data[index] = item
            else:
                fix_json_values(item)
    return data

def fix_json_file(input_file, output_file):
    with open(input_file, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

    # 修正 JSON 数据中的双引号转义问题和新行引号问题
    fixed_data = fix_json_values(data)

    with open(output_file, 'w') as f:
        json.dump(fixed_data, f, indent=2)

if __name__ == "__main__":
    input_file = 'database.json'  # 输入文件
    output_file = 'fixed_data.json'  # 输出文件
    fix_json_file(input_file, output_file)
    print(f"Processed file saved as {output_file}")
