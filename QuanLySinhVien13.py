# 13. Tính học bổng trung bình trên tổng số sinh viên có trong danh sách lớp

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_log(message):
    f = open("KetQua.log", mode="a", encoding="UTF-8")
    f.write(f"{message}\n")
    f.close()

f = open("DanhSach.txt", mode="r",encoding="utf-8")
content = f.read()
f.close()

while True:
    x=input("Nhập lớp niên chế: ")
    count = 0
    total = 0
    for i in content.split("\n"):
        if i!= "":
            if str(i.split(",")[3]) == x:
                count += 1
                total += int(i.split(",")[4])
    average_tt = total / count

    print(f"Học bổng trung binh trên các sinh viên được học bổng có trong danh sách lớp {x}: {round(average_tt,2)}")
    write_log(f"Học bổng trung binh trên các sinh viên được học bổng có trong danh sách lớp {x}: {round(average_tt,2)}")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break

    
