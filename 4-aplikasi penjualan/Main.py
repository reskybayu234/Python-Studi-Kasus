menu = [["nasi goreng", 10000], ["nasi kuning", 13000], [" nasi pecel",5000]]

def menu_makanan():
    a = "=" * 25
    print(a.center(40))
    b = "No | Nama Makanan | Harga"
    c = "=" * 25
    print(b.center(40))
    print(c.center(40))
    i = 1
    for item in menu:
        kal = str(i) + " | " + item[0] + "  | " + str(item[1])
        print(kal.center(40))
        i += 1
    a = "=" * 25
    print(a.center(40))

menu_makanan()
jawaban = ""
catatan_menu = []
while jawaban != "0":
    jawaban = input("Pilih menu : ")
    # menu_makanan()
    if jawaban != "0":
        catatan_menu.append(int(jawaban)-1)

no = 1
total = 0
print("pesanan anda : ")
for item_beli in catatan_menu:
    print("Makanan ke-"+ str(no) + " = " + menu[item_beli][0] + " harga " + str(menu[item_beli][1]))
    no += 1
    total = total + int(menu[item_beli][1])
print("Total Pembayaran : " + str(total))
    