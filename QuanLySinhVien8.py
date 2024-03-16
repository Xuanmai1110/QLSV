# 8. Xác định số lượng sinh viên được học bổng

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

count = 0
for i in content.split("\n"):
    if i!= "":
        if int(i.split(",")[4]) != 0:
            count += 1

print(f"Số lượng sinh viên được học bổng: {count} sinh viên")
write_log(f"Số lượng sinh viên được học bổng: {count} sinh viên")
