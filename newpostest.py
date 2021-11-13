barang_toko = {
    "Yamaha F-400" : 1250000,
    "Cort AD-810E" : 1750000,
    "Cadenza CE203" : 1500000,
    "Segovia D-W07" : 1850000,
    "Prodinne 40CN" : 1450000
}
keuntungan_harian = []

def menu_kasir():
    R = False
    while not R:
        print("=======================================================")
        print("              >> GUITAR ACCOUSTIC STORE <<             ")
        print("=======================================================")
        print("Nama Gitar:                 Harga:      \n")
        barang_toko
        for nama, harga in barang_toko.items():
            print(nama,"             ","Rp.", harga)
        print("=======================================================")
        print("=               --> DISKON SPESIAL! <--               =")
        print("=                                                     =")
        print("=     >Diskon 10% jika belanja lebih dari 5 juta      =")
        print("=     >Diskon 25% jika belanja lebih dari 7 juta      =")
        print("=======================================================")
        jumlah_tipe = int(input("Banyak tipe   : "))
        x = 0
        total = []
        while x < jumlah_tipe:
            print("\nTipe ke -", 1 + x)
            produk = barang_toko[(input("Nama produk   : "))]
            jumlah = int(input("Jumlah produk : "))
            total.append(produk * jumlah)
            total1 = produk * jumlah
            print("Total harga   : Rp.", total1)
            x += 1           
        print("==============================================")
        sub_total =sum(total)
        print("sub total                    : Rp.", sub_total)
        diskon1 = sub_total * 0.10
        diskon2 = sub_total * 0.25
        if sub_total <= 5000000:
            print("Diskon - %                   : Rp. -")
            keuntungan_harian.append(sub_total)
            print("\nTotal                        : Rp.", sub_total)
            print("==============================================")
            uang_tunai1 = int(input("Uang tunai                   : Rp. "))
            kembalian1 = uang_tunai1 - sub_total
            print("Kembalian                    : Rp.", kembalian1)
            print("\n----------------------------------------------")
        elif sub_total <= 7000000:
            print("Diskon 10%, potongan sebesar : Rp.", diskon1)
            keuntungan_harian.append(sub_total - diskon1)
            total_bayar2 = sub_total - diskon1
            print("\nTotal                        : Rp.", total_bayar2)
            print("==============================================")
            uang_tunai2 = int(input("Uang tunai                   : Rp. "))
            kembalian2 = uang_tunai2 - total_bayar2
            print("Kembalian                    : Rp.", kembalian2)
            print("\n----------------------------------------------")
        elif sub_total > 7000000:
            print("Diskon 25%, potongan sebesar : Rp.", diskon2)
            keuntungan_harian.append(sub_total - diskon2)
            total_bayar3 = sub_total - diskon2
            print("\nTotal                        : Rp.", total_bayar3)
            print("==============================================")
            uang_tunai3 = int(input("Uang tunai                   : Rp. "))
            kembalian3 = uang_tunai3 - total_bayar3
            print("Kembalian                    : Rp.", kembalian3)
            print("\n----------------------------------------------")
        tanya1 = input("Apakah ingin kembali ke awal [Y]/[T] : ")
        if tanya1 == "T" or tanya1 == "t":
            R = True
            tanya2 = input("Lihat keuntungan hari ini [Y]/[T] : ")
            if tanya2 == "t" or tanya2 == "T":
                EE = True
            else:
                print("\nLogin sebagai admin untuk melihat keuntungan hari ini\n")
    

def menu_crud():
    print("Silahkan pilih menu berikut : ")
    print("[1]. Keuntungan harian","\n[2]. Menu Update", "\n[3]. Kembali ke menu kasir", "\n[4]. Keluar")
    xyz = int(input("Pilih 1/2/3/4 ?  : "))
    if xyz == 1:
        print("Keuntungan harian anda sebesar : Rp.", sum(keuntungan_harian))
    elif xyz == 3:
        print("\nLogin sebagai user untuk kembali ke menu kasir\n")
    elif xyz == 4:
        print("Silahkan Login")
    elif xyz == 2:
        stop = False
        while not stop:
            print("Apa yang anda inginkan?")
            print("[1]. Menghapus barang ", "\n[2]. menambah list barang", "\n[3]. Mengupdate harga barang")
            pilihan = int(input("Masukkan pilihan 1/2/3 : "))
            if pilihan == 1:
                bj = int(input("Banyak barang yang ingin di hapus : "))
                i = 0
                while i < bj:
                    print("\nBarang ke -", i + 1)
                    kd = input("Masukkan nama barang yang ingin di hapus : ")
                    del barang_toko[kd]
                    i += 1                            
                print("\n===== Barang berhasil di hapus =====\n")
            elif pilihan == 2:
                bj = int(input("Banyak barang yang ingin di tambah : "))
                a = 0
                while a < bj:
                    print("\nBarang ke -", a + 1)
                    kd = input("Masukkan nama barang yang ingin di tambah : ")
                    hh = int((input("Harga barang : ")))
                    barang_toko[kd] = hh
                    a += 1
                print("\n===== Barang berhasil di tambah pada list menu =====\n")
            elif pilihan == 3:
                b = 0
                bj = int(input("Banyak barang yang ingin di update harganya : "))
                while b < bj:
                    print("\nBarang ke -", b + 1)
                    kd = input("Masukkan nama barang yang ingin di update harganya : ")
                    ubah_harga = int(input("Ubah harga menjadi : "))
                    barang_toko[kd] = ubah_harga
                    b += 1
                print("\n===== Harga berhasil di update =====\n")
            else:
                stop = True    
            tanya = input("Apakah ingin kembali ke menu awal? {Y}/{T} : ")
            if tanya == "T" or tanya == "t":
                stop = True
            else:
                stop = False

#program
EE = False
while not EE:
    xx = input("Login sebagai user/admin? : ")
    if xx == "user":
        xx1 = input("Username : ")
        yy1 = int(input("Password : "))
        while not yy1 == 210:
            print("\nPassword salah!")
            yy1 = int(input("Password : "))
        else:
            menu_kasir()
    elif xx == "admin":
        xx1 = input("Username : ")
        yy1 = input("Password : ")
        while not yy1 == "078":
            print("\nPassword salah!")
            yy1 = input("Password : ")
        else:
            menu_crud()



