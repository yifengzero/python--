poem = "登鹳雀楼\t 王之涣\t 白日依山尽\t  黄河入海流\n  欲穷千里目  更上一层楼"

print(poem)

# 拆分字符串
poem_list=poem.split()
print(poem_list)

# 合并字符串
result = " ".join(poem_list)
print(result)