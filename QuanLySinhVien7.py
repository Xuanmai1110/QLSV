# 7. In ra danh sách sinh viên có tên đệm Thị có trong lớp CQ59/41.02

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Danh sách sinh viên tên đệm Thị có trong lớp CQ59/41.02: ")

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

found = False
for i in content.split("\n"):
    if i != "":
        a=str(i.split(",")[2])
        if str(i.split(",")[3]) == "CQ59/41.02" and str(a.split()[1]) == "Thị":
            print(i)
            write_log(i)
            found = True
if not found:
    kq = "Không có sinh viên nào thỏa mãn"
    print(kq)
    write_log(kq)
