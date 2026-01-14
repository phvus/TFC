n=1
i=1

#Tính trả góp
def tinh_tra_gop(gia_tri_may,so_thang,lai_suat):
    #tiền gốc
    du_no=gia_tri_may
    tong_tien_tra=0
    tien_goc=gia_tri_may/so_thang
    for i in range(1, int(so_thang) + 1):
        #tiền lãi tháng này
        tien_lai=du_no*(lai_suat/100)
        #tiền trả hàng tháng
        tien_tra_hang_thang=tien_goc+tien_lai
        #cộng dồn tổng tiền trả
        tong_tien_tra+=tien_tra_hang_thang
        #cập nhật dư nợ
        du_no-=tien_goc
        print(f"Tháng: {i} Tiền trả hàng tháng: {round(tien_tra_hang_thang):,}")
    return tong_tien_tra


while n<10:
    n+=1
    try:
        gia_tri_may,so_thang,lai_suat,thu_nhap=map(float,input("Nhập giá trị máy, số tháng trả góp, lãi suất hàng tháng: ").split())
        if gia_tri_may<=0 or so_thang<=0 or lai_suat<=0 or thu_nhap<=0:
            print("re-enter")
            continue
        break
    except ValueError:
        print("re-enter")
tong_tien_tra=tinh_tra_gop(gia_tri_may,so_thang,lai_suat)
print(f"Tổng số tiền phải trả: {round(tong_tien_tra):,}")

#Tính khấu hao
def tinh_khau_hao(gia_tri_may, so_thang):
    ty_le_khau_hao=3/100
    for i in range(1, int(so_thang)+1):
        gia_tri_may-=gia_tri_may*ty_le_khau_hao
    return gia_tri_may
gia_tri_thuc_te=tinh_khau_hao(gia_tri_may, so_thang)
print(f"Giá trị thực tế của máy sau {int(so_thang)} tháng là: {round(gia_tri_thuc_te):,}")

no_ban_be=[]
#Bubble Sort
def quan_ly_no_ban_be(no_ban_be):
    m=len(no_ban_be)
    for i in range(m):
        swap=False
        for j in range(0,m-i-1):
            if no_ban_be[j]>no_ban_be[j+1]:
                no_ban_be[j],no_ban_be[j+1]=no_ban_be[j+1],no_ban_be[j]
                swap=True
        if not swap:
            break
    return no_ban_be

#Nợ nhiều thế bạn ê!!!!
while n<10:
    n+=1
    try:
        n=int(input("Nhập số bạn bè nợ tiền: "))
        if n>30:
            print("Nợ nhiều thế!")
            continue
        for i in range(1,n+1):
            tien_no=int(input(f"Nhập số tiền đang nợ của người số {i}: "))
            no_ban_be.append((tien_no))
        break
    except ValueError:
        print("re-enter")
no_ban_be_new=quan_ly_no_ban_be(no_ban_be)

for tien in no_ban_be_new:
    print(f"số tiền nợ của người số {i}: {tien:,}") 
    i+=1
    if tien>200000:
        print("Trốn vội đê!!")
    else:
        print("Chill bro!!")

#Sinh tồn đê bạn ê!!!!
def main():
    chenh_lech=tong_tien_tra-gia_tri_thuc_te
    print(f"Số tiền bạn lỗ sau khi hết nợ: {round(chenh_lech):,}")
    if (gia_tri_may*lai_suat+gia_tri_may/so_thang)+sum(no_ban_be_new)>0.5*thu_nhap:
        print("Mì tôm là một lựa chọn tốt =)")
    else:
        print("Hải sản là một lựa chọn tốt =)")
main()