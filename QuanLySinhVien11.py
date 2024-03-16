# 11. Tính tổng tiền học bổng của một lớp niên chế nào đó

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
    x=input('Nhập lớp niên chế: ')
    total = 0
    for i in content.split("\n"):
        if i!= "":
            if (i.split(",")[3]) == x:
                total += int(i.split(",")[-1])
        
    print(f"Tổng tiền học bổng của lớp niên chế {x}: {total}")
    write_log(f"[{timestamp}]: Tổng tiền học bổng của lớp niên chế {x}: {total}")

    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break
