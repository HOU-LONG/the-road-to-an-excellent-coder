# 这个Python脚本用于从Python源代码文件中提取所有注释，并将它们保存到一个文本文件中。

def extract_comments_from_file(file_path):
    """
    从给定的Python文件中提取所有注释。
    
    参数:
        file_path (str): Python源代码文件的路径。
        
    返回:
        list: 包含所有注释的列表。
    """
    comments = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.startswith('#'):
                comments.append(stripped_line)
            elif '"""' in stripped_line or "'''" in stripped_line:
                # 处理多行字符串注释
                if stripped_line.count('"""') % 2 != 0 or stripped_line.count("'''") % 2 != 0:
                    comment = stripped_line
                    next_line = file.readline().strip()
                    while not (next_line.endswith('"""') or next_line.endswith("'''")):
                        comment += '\n' + next_line
                        next_line = file.readline().strip()
                    comment += '\n' + next_line
                    comments.append(comment)
    return comments

def write_comments_to_file(comments, output_file):
    """
    将提取的注释写入指定的文本文件。
    
    参数:
        comments (list): 注释列表。
        output_file (str): 输出文本文件的路径。
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for comment in comments:
            file.write(comment + '\n')

# 使用示例
if __name__ == "__main__":
    input_file = 'E:\scGPT-integrate-huggingface-model\scGPT-integrate-huggingface-model\examples\pretrain.py'  # 替换为你的Python文件路径
    output_file = 'C:/Users/houlong/Desktop/pretrain.txt'  # 替换为你想要保存注释的文本文件路径
    comments = extract_comments_from_file(input_file)
    write_comments_to_file(comments, output_file)
    print(f"Comments have been extracted and saved to {output_file}")