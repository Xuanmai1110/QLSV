# 12. Tính học bổng trung bình trên các sinh viên được học bổng

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
total = 0
for i in content.split("\n"):
    if i!= "":
        if int(i.split(",")[4]) != 0:
            count += 1
            total += int(i.split(",")[4])
average_tt = total / count

print(f"Học bổng trung binh trên các sinh viên được học bổng: {round(average_tt,2)}")
write_log(f"Học bổng trung binh trên các sinh viên được học bổng: {round(average_tt,2)}")
