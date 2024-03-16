# 15. Xác định số sinh viên trong danh sách lớp mà tên có 4 từ

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

count=0
for i in content.split("\n"):
    if i != "":
        a=i.split(",")[2]
        if len(a.split()) == 4:
            count +=1

print(f"Số sinh viên trong danh sách lớp mà tên có 4 từ: {count} sinh viên")
write_log(f"Số sinh viên trong danh sách lớp mà tên có 4 từ: {count} sinh viên")
        
