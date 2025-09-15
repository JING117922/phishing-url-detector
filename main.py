import pandas as pd

try:
    # 强制用二进制方式逐行读取，然后转成文本
    with open("dataset.csv", "rb") as f:
        lines = f.readlines()

    # 尝试 decode
    decoded_lines = []
    for line in lines:
        try:
            decoded_lines.append(line.decode("utf-8"))
        except:
            try:
                decoded_lines.append(line.decode("latin1"))
            except:
                continue  # 跳过无法解码的行

    # 重新写入一个干净的新文件
    with open("cleaned.csv", "w", encoding="utf-8") as f:
        f.writelines(decoded_lines)

    # 读取新的清理后的 csv 文件
    df = pd.read_csv("cleaned.csv", sep=",", on_bad_lines="skip")
    print("读取成功！展示前5行：")
    print(df.head())

except Exception as e:
    print("读取失败：", e)
