# 10. In ra danh sách sinh viên được học bổng thấp nhất (khác 0) của lớp CQ59/41.02

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

write_log(f"[{timestamp}]: Danh sách sinh viên được học bổng thấp nhất (khác 0) của lớp CQ59/41.02: ")

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

min_tt = min(int(i.split(",")[-1]) for i in content.split("\n") if i and str(i.split(",")[3]) == "CQ59/41.02" and int(i.split(",")[-1]) != 0)
for i in content.split("\n"):
    if i != "":
        if str(i.split(",")[3]) == "CQ59/41.02" and int(i.split(",")[-1]) == min_tt:
            print(i)
            write_log(f"{i}")