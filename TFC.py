n=0
while n<10:
    n+=1
    try:
        km=float(input("Nhập quãng đường: "))
        tongtien=0
        if km<0 or km>=1000:
            print("Invalid")
            continue
        tongtien=0
        if km<=1 and km>0:
            tongtien=15000
            print(f"{int(tongtien)} nghìn đồng")
        elif km>1 and km<=10:
            tongtien=15000+((km-1)*13500)
            print(f"{int(tongtien)} nghìn đồng")
        elif km==0:
            print(f"{int(tongtien)} nghìn đồng")
        else:
            tongtien=15000+(9*13500)+((km-10)*11000)
            if km>=120:
                tongtien=tongtien*0.9
            print(f"{int(tongtien)} nghìn đồng")
    except ValueError:
        print("Invalid")