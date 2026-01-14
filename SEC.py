a=True
b=True
while a==True:
    try:
        origin=int(input("Nhập số tiền bn có: "))
        dom=int(input("Nhập chi phí tiền nhà ở: "))
        do_time=int(input("Thời gian thuê (theo tháng): "))
        device=int(input("Nhập giá trị tài sản cố định: "))
        de_time=int(input("Thiết bị dự kiến sử dụng trong bao lâu (theo năm): "))
        if 0 < origin <= 10**7 and 0 < dom <= 2*10**7 and 0 < device <= 10**8 and 0 < do_time <= 12 and 0 < de_time <= 20:
            a = False
        else:
            print("Invalid")
            continue
    except ValueError:
        print("Invalid")
spend1d=0

while b==True:
    try:
        food=int(input("Tiền ăn: "))
        vehi=int(input("Tiền chi cho phương tiện di chuyển: "))
        water=int(input("Tiền nước: "))
        elec=int(input("Tiền điện: "))
        hou=int(dom/(do_time*30))
        print(f"Tiền nhà ở: {hou}")
        kh=int(device/(de_time*365))
        print(f"Tiền khấu hao tài sản cố định: {kh}")
        other=int(input("Chi phí khác: "))
        if food<0 or vehi<0 or other<0 or water<0:
            print("Invalid")
            continue
        else:
            spend1d=food+vehi+other+water+hou+elec+kh
            print(f"Số tiền tiêu cho 1 ngày là {spend1d}")
            b=False
    except ValueError:
        print("Invalid")
print(f"Tổng số tiền tiêu trong 1 tuần là {spend1d*7}")
print(f"Số tiền còn lại sau 1 tuần là: {origin-spend1d*7}")