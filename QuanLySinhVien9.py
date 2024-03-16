# 9. In ra danh sách sinh viên được học bổng cao nhất

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Danh sách sinh viên được học bổng cao nhất: ")

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

max_tt = max(int(i.split(",")[-1]) for i in content.split("\n") if i)
for i in content.split("\n"):
    if i != "":
        if int(i.split(",")[-1]) == max_tt:
            print(i)
            write_log(i)
