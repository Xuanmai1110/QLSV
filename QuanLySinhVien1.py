# 1. Nhập các thông tin sau cho mỗi sinh viên: STT, Mã sinh viên (13 chữ số), Họ tên sinh viên, Lớp niên chế (Dạng CQxx/41.0y), Học bổng

import os
from datetime import datetime
import re
os.chdir("D:\Xuân Mai\Tài liệu môn học\Lập trình Python căn bản\Quản lý sinh viên")
def write_dulieu(Mode, message):
    f = open("DanhSach.txt", mode=Mode, encoding="UTF-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{timestamp}]: {message}\n")
    f.close()
while True:
    while True:
        try:
            k = int(input("Số lượng sinh viên: "))
            if k <= 0:
                print("Giá trị nhập phải >0. Hăy nhập lại!")
                continue
        except ValueError:
            print("Giá trị nhập sai kiểu dữ liệu!")
            continue
        break
    for i in range(k):
        while True:
            try:
                stt=int(input(f"Nhập STT ({i+1}): "))
                if stt <= 0:
                    print("Nhập lại STT>0")
                    continue
            except ValueError:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break
        while True:
            try:
                MaSinhVien=input(f"Nhập mă sinh viên (13 chữ số) ({i+1}): ")
                if len(MaSinhVien) != 13:
                    print("Giá trị nhập phải có độ dài bằng 13. Hăy nhập lại!")
                    continue
                if not MaSinhVien.isdigit():
                    print("Giá trị nhập phải là chữ số. Hăy nhập lại!")
                    continue
            except ValueError:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break
        while True:
            Ten=input(f"Nhập họ và tên sinh viên ({i+1}): ")
            if not Ten.replace(" ","").isalpha():
                print("Tên sinh viên chỉ chứa kí tự chữ cái. Hăy nhập lại!")
                continue
            break
        while True:
            LopNienChe=input(f"Nhập lớp niên chế (Dạng CQxx/41.0y) ({i+1}): ")
            pattern = re.compile(r'^CQ\d{2}/41\.0\d$')
            if not bool(pattern.match(LopNienChe)):
                print("Định dạng lớp niên chế không hợp lệ. Vui lòng nhập lại.")
                continue
            break
        while True:
            try:
                HocBong=int(input(f"Nhập học bổng ({i+1}): "))
                if HocBong < 0:
                    print("Học bổng phải >= 0. Hăy nhập lại!")
                    continue
            except ValueError:
                print("Giá trị nhập sai kiểu dữ liệu!")
                continue
            break
        write_dulieu("a",f"{str(stt)},{str(MaSinhVien)},{Ten},{str(LopNienChe)},{str(HocBong)}")
    tiep_tuc = input("Bạn có muốn tiếp tục? (y/n): ")
    while tiep_tuc.lower() not in ['y', 'n']:
        tiep_tuc = input("Lựa chọn không hợp lệ. Bạn có muốn tiếp tục? (y/n): ")
    if tiep_tuc.lower() == 'n':
        break

            
            
                          
            
        
                    
