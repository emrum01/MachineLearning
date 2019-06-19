#ベーシックな書き方
file = open("sample.txt","r",encoding = "utf-8")
try:
    whole_str = file.read()
    print(whole_str)
finally:
    file.close()

with open("sample.txt","r",encoding = "utf-8") as file:
    any_str = file.read()
    
print("\n"+any_str+"ヤサイスクナメニンニクベツザラアブラカラメ")

