# 16. Xác định số sinh viên trong danh sách lớp mà tên có n từ

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
    n=int(input("Nhập n (n là số từ có trong tên sinh viên): "))
    count=0
    for i in content.split("\n"):
        if i != "":
            a=i.split(",")[2]
            if len(a.split()) == n:
                count +=1

    print(f"Số sinh viên trong danh sách lớp mà tên có {n} từ: {count} sinh viên")
    write_log(f"Số sinh viên trong danh sách lớp mà tên có {n} từ: {count} sinh viên")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break
        
