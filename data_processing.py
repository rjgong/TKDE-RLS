import os
import re

# 初始化存储结果的字典
data = {
    'xxx': [],
    'yyy': []
}

# 遍历文件夹中的所有.py文件
folder_path = 'test'
for filename in os.listdir(folder_path):
    if filename.endswith('.py'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()

            lines = [line for line in lines if not line.strip().startswith('ax.text')]
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                
                # 检查以xxx或yyy开头的行
                if line.startswith('xxx =') or line.startswith('yyy ='):
                    if line.startswith('xxx'):
                        key = 'xxx'
                    else:
                        key = 'yyy'
                    current_data = []
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith(']'):
                        match = re.search(r'\b\d+(\.\d+)?(\+\d+(\.\d+)?)?\b', lines[i])  # 匹配小数的格式，例如 1.5+3.25
                        if match:
                            decimals = match.group().split('+')
                            decimal_sum = 0
                            for decimal in decimals:
                                decimal_sum += float(decimal)
                            current_data.append(decimal_sum)
                        
                        i += 1
                        print(filename, "current_data", current_data)
                    data[key].extend(current_data)
                    print("y_val", "x_val", data['yyy'], data['xxx'])
                # 检查以ax.set_xlabel开头的行
                elif line.startswith('ax.set_xlabel'):
                    increment = -0.1
                    for y_val, x_val in zip(data['yyy'], data['xxx']):
                        
                        new_lines = []
                        new_line = f'ax.text({increment}, ({y_val + 200:.2f}), "{round(y_val / x_val, 2):.2f}x", fontsize=35)\n'
                        new_lines.append(new_line)
                        lines[i:i] = new_lines
                        i += len(new_lines)
                        increment += 1
                    i += 1
                else:
                    i += 1

        # 将修改后的内容写回文件
        with open(file_path, 'w') as file:
            file.writelines(lines)
        data = {
            'xxx': [],
            'yyy': []
        }