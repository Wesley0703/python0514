print("Hello, Python!")
print(456):
import sys

print("===============")
print(sys.version)

name = "Alice"
greeting = 'Hello, World!'
print(123)
print(name)
print(greeting)
text = "  Hello, Python  "

# 去除空白
print(text.strip())           # "Hello, Python"
print(text.lstrip())          # "Hello, Python  "
print(text.rstrip())          # "  Hello, Python"

# 大小寫
print(text.strip().upper())   # "HELLO, PYTHON"
print(text.strip().lower())   # "hello, python"
print("hello world".title())  # "Hello World"
print("hello world".capitalize())  # "Hello world"

# 搜尋與判斷
text2 = "Hello, Python"
print(text2.find("Python"))        # 7（回傳索引，找不到回傳 -1）
print(text2.startswith("Hello"))   # True
print(text2.endswith("Python"))    # True
print("Python" in text2)          # True

# 取代與分割
print(text2.replace("Hello", "Hi"))   # "Hi, Python"
print("a,b,c".split(","))             # ['a', 'b', 'c']
print(",".join(["a", "b", "c"]))      # "a,b,c"
print(*456)
# 補位
print("42".zfill(5))          # "00042"
print("hi".center(10))        # "    hi    "
print("hi".ljust(10, "-"))    # "hi--------"
print("hi".rjust(10, "-"))    # "--------hi"
