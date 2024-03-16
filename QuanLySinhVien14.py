# 14. In các thông tin Mă sinh viên, Họ và tên của các sinh viên

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

for i in content.split("\n"):
    if i!= "":
        print(i.split(",")[1],",", i.split(",")[2])
        write_log(f"{i.split(',')[1]},{i.split(',')[2]}")
