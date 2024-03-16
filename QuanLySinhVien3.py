# 3. In ra danh sách các sinh viên có trùng họ tên trong 2 lớp CQ59/41.01 và CQ59/41.02

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="utf-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Danh sách các sinh viên có trùng họ tên trong 2 lớp CQ59/41.01 và CQ59/41.02: ")

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

list_1 = []
list_2 = []
for i in content.split("\n"):
    if i != "":
        if str(i.split(",")[3]) == "CQ59/41.01":
            list_1.append(i.split(",")[2])
        if str(i.split(",")[3]) == "CQ59/41.02":
            list_2.append(i.split(",")[2])

found = False
for i in content.split("\n"):
    if i != "":
        if str(i.split(",")[3]) in ["CQ59/41.01","CQ59/41.02"] and i.split(",")[2] in list(set(list_1) & set(list_2)):
            print(i)
            write_log(i)
            found = True
if not found:
    kq = "Không có sinh viên nào thỏa mãn"
    print(kq)
    write_log(kq)
