list_kar=[
     {"NPK":"K01","Nama":"Doni","Gender":"Pria","Usia":30,"Jabatan":"Kepala Cabang", "Level" : "Manager"},
     {"NPK":"K02","Nama":"Dara","Gender":"Wanita","Usia":26,"Jabatan":"Sales UsedCar", "Level" : "Officer"},
     {"NPK":"K03","Nama":"Aziz","Gender":"Wanita","Usia":27,"Jabatan":"Sales NewCar", "Level" : "Officer"},
     {"NPK":"K04","Nama":"Satria","Gender":"Wanita","Usia":21,"Jabatan":"Credit Analyst", "Level" : "Officer"},
     {"NPK":"K05","Nama":"Sophie","Gender":"Wanita","Usia":22,"Jabatan":"Customer Service", "Level" : "Officer"}]  

def dataKaryawan():
    totalkar = 0
    print('''NPK \t | Nama \t\t\t | Gender \t\t | Usia \t | Jabatan \t\t\t\t | Level''')
    print('''---------------------------------------------------------------------------------------------------------------------------------------''')
    for x in range(len(list_kar)):        
        print(f'{list_kar[x]["NPK"]} \t | {list_kar[x]["Nama"]} \t\t\t | {list_kar[x]["Gender"]} \t\t | {list_kar[x]["Usia"]} \t\t | {list_kar[x]["Jabatan"]} \t\t\t | {list_kar[x]["Level"]}')
        totalkar += 1
    print(f"Total Karyawan : {totalkar}")    
    
def welcome():
    print('''
 ==========================**===========================
|           DATABASE KARYAWAN PT MAJU MUNDUR            |
 =======================================================
Selamat Datang! Pilihan menu yang tersedia:         

1. Lihat data karyawan
2. Tambahkan data baru
3. Perbaharui data
4. Hapus data Karyawan
5. Keluar
            ''')

#fungsi tampilkan karyawan
def report():
    while True:
        print('''
 =======================**============================
|     Database Karyawan Perusahaan Maju Mundur        |
 ==========-==========================================
1. Lihat seluruh data karyawan
2. Cari data karyawan tertentu
3. Kembali ke Menu Utama''')
        pilih_menu = input("\nSilahkan Pilih Menu: ")
        if pilih_menu == '1':
            if list_kar == []:
                print("Data belum tersedia. Silahkan tambah daftar karyawan.")
                break
            else:
                dataKaryawan()
        elif pilih_menu == '2':
            cariKar = input("Masukkan NPK : ")
            for a in range(len(list_kar)):
                if cariKar in list_kar[a]["NPK"]:
                    print('''NPK \t | Nama \t\t\t | Gender \t\t | Usia \t | Jabatan \t\t\t\t | Level \n''')
                    print('''---------------------------------------------------------------------------------------------------------------------------------------''')
                    print(f'{list_kar[a]["NPK"]} \t | {list_kar[a]["Nama"]} \t\t\t | {list_kar[a]["Gender"]} \t\t | {list_kar[a]["Usia"]} \t\t | {list_kar[a]["Jabatan"]} \t\t\t | {list_kar[a]["Level"]}')
                    break
                elif a == max(range(len(list_kar))):
                    print(f"Karyawan dengan NPK {cariKar} Tidak ada!")
                    break
                else:
                    continue
        elif pilih_menu == '3':
            break
        else:
            continue
                    
#fungsi tambah karyawan              
def tambahKaryawan():
    while True:
        print('''
 =======================**============================
|     Tambah Data Karyawan Perusahaan Maju Mundur     |
 ==========-==========================================
1. Tambah data Karyawan
2. Kembali ke menu utama''')
        subMenu1 = input("Silahkan Pilih Sub Menu Create Data [1-2] : ")
        if subMenu1 == "1":
            npk = input("Masukkan NPK : ")
            for a in range(len(list_kar)):
                if list_kar[a]["NPK"] == npk:
                    print(f"Gagal Menambahkan!. Karyawan dengan {npk} sudah ada")
                    break
                elif a == max(range(len(list_kar))):
                    nama = input("Masukkan nama karyawan : ")
                    gender = input("Jenis kelamin karyawan : ")
                    usia = int(input("Masukkan usia karyawan : "))
                    while usia <= 0:
                        print("Usia harus bernilai bilangan bulat positif")
                        usia = int(input("Masukkan Usia karyawan : "))
                        continue
                    jabatan = input("Masukkan jabatan karyawan : ")
                    level = input("Masukkan level karyawan : ")
                    while True:
                        konfirmasi = input("Apakah data akan disimpan? (Y/N) : ")
                        if konfirmasi == "Y" or konfirmasi == "y":
                            list_kar.append({"NPK":npk, "Nama":nama, "Gender":gender, "Usia":usia, "Jabatan":jabatan, "Level" : level})
                            print("Data berhasil tersimpan")
                            break
                        elif konfirmasi == "N" or konfirmasi == "n":
                            print("Data tidak tersimpan")
                            break
                        else:
                            continue
                else:
                    continue
                
                
        elif subMenu1 == "2":
            break
        else:
            continue

#fungsi update karyawan            
def updateData():
    while True:
        print('''
 ==========**==========
|     Perbaharui Data   |
 ==========-============
1. Ubah data karyawan
2. Kembali ke menu utama''')
        subMenu2 = input("Silahkan pilih sub menu Update Data [1-2] : ")
        if subMenu2 == "1":
            dataKaryawan()
            npk = input("Masukkan NPK yang ingin diupdate : ")
            for a in range(len(list_kar)):
                if npk == list_kar[a]["NPK"]:
                    print('''NPK \t | Nama \t\t\t | Gender \t\t | Usia \t | Jabatan \t\t\t\t | Level \n''')
                    print('''---------------------------------------------------------------------------------------------------------------------------------------''')
                    print(f'{list_kar[a]["NPK"]} \t | {list_kar[a]["Nama"]} \t\t\t | {list_kar[a]["Gender"]} \t\t | {list_kar[a]["Usia"]} \t\t | {list_kar[a]["Jabatan"]} \t\t\t | {list_kar[a]["Level"]}')   
                    while True:
                        lanjut_update = input("Tekan 'Y' apabila untuk melanjutkan update data atau 'N' apabila ingin membatalkan update (Y/N) : ")
                        if lanjut_update == "y" or lanjut_update == "Y":
                            edit_kolom = input("Masukkan Nama kolom yang ingin di edit : ")
                            if edit_kolom == "nama"or edit_kolom == "Nama":
                                nama=input("Masukkan nama baru : ")
                                while True:
                                    konfirmasi_edit_kolom = input("Apakah data akan diupdate? (Y/N) : ")
                                    if konfirmasi_edit_kolom == "y" or konfirmasi_edit_kolom == "Y":
                                        list_kar[a]["Nama"] = nama
                                        print("data berhasil diperbaharui!")
                                        break
                                    elif konfirmasi_edit_kolom == "n" or konfirmasi_edit_kolom == "N":
                                        print("data batal diperbaharui!")
                                        break
                                    else:
                                        continue
                            elif edit_kolom == "npk" or edit_kolom == "NPK":
                                npk = input("Masukkan NPK Baru : ")
                                while True:
                                    konfirmasi_edit_kolom = input("Apakah data akan diupdate? (Y/N) : ")
                                    if konfirmasi_edit_kolom == "y" or konfirmasi_edit_kolom == "Y":                                
                                        list_kar[a]["NPK"] = npk
                                        print("data berhasil diperbaharui!")
                                        break
                                    elif konfirmasi_edit_kolom == "n" or konfirmasi_edit_kolom == "N":
                                        print("data batal diperbaharui!")
                                        break
                                    else:
                                        continue
                            elif edit_kolom == "gender"or edit_kolom == "Gender":
                                gender = input("Masukkan Gender Baru : ")
                                while True:
                                    konfirmasi_edit_kolom = input("Apakah data akan diupdate? (Y/N) : ")
                                    if konfirmasi_edit_kolom == "y" or konfirmasi_edit_kolom == "Y":                                
                                        list_kar[a]["Gender"] = gender
                                        print("data berhasil diperbaharui!")
                                        break
                                    elif konfirmasi_edit_kolom == "n"or konfirmasi_edit_kolom == "N":
                                        print("data batal diperbaharui!")
                                        break
                                    else:
                                        continue
                            elif edit_kolom == "usia"or edit_kolom == "Usia":
                                usia = int(input("Masukkan Usia Baru : "))
                                while True:
                                    konfirmasi_edit_kolom = input("Apakah data akan diupdate? (Y/N) : ")
                                    if konfirmasi_edit_kolom == "y" or konfirmasi_edit_kolom == "Y":                                
                                        list_kar[a]["Usia"]=usia
                                        print("data berhasil diperbaharui!")
                                        break
                                    elif konfirmasi_edit_kolom == "n" or konfirmasi_edit_kolom == "N":
                                        print("data batal diperbaharui!")
                                        break
                                    else:
                                        continue
                            elif edit_kolom == "Jabatan" or edit_kolom == "jabatan":
                                jabatan = input("Masukkan Jabatan baru : ")
                                while True:
                                    konfirmasi_edit_kolom = input("Apakah data akan diupdate? (Y/N) : ")
                                    if konfirmasi_edit_kolom == "y" or konfirmasi_edit_kolom == "Y":                                
                                        list_kar[a]["Jabatan"] = jabatan
                                        print("data berhasil diperbaharui!")
                                        break
                                    elif konfirmasi_edit_kolom == "n" or konfirmasi_edit_kolom == "N":
                                        print("data batal diperbaharui!")
                                        break
                            elif edit_kolom == "level" or edit_kolom == "Level":
                                level = input("Masukkan Level baru : ")
                                while True:
                                    konfirmasi_edit_kolom = input("Apakah data akan diupdate? (Y/N) : ")
                                    if konfirmasi_edit_kolom == "y" or konfirmasi_edit_kolom == "Y":                                
                                        list_kar[a]["Level"] = level
                                        print("data berhasil diperbaharui!")
                                        break
                                    elif konfirmasi_edit_kolom == "n" or konfirmasi_edit_kolom == "N":
                                        print("data batal diperbaharui!")
                                        break
                                    else:
                                        continue
                            else:
                                print("Tidak ada kolom tersebut pada data karyawan!!")
                                break
                        elif lanjut_update == "n" or lanjut_update == "N":
                            break
                        else:
                            continue
                elif a == max(range(len(list_kar))):
                    print("Tidak ada karyawan yang memiliki NPK tersebut")
                    break
                else:
                    continue
        elif subMenu2 == "2":
            break
        else:
            continue

#fungsi hapus karyawan
def hapusDataKaryawan():
    while True:
        print('''
 ==========**===========
|     Hapus Data        |
 ==========-============
1. Hapus data Karyawan
2. Kembali ke menu utama''')
        pilih_menu_hapus=input("Silahkan pilih sub menu Hapus Data [1-2] : ")
        if pilih_menu_hapus == "1":
            dataKaryawan()
            hapusnpk = input("Silahkan masukkan NPK yang ingin dihapus : ")
            for x in range(len(list_kar)):
                if hapusnpk == list_kar[x]["NPK"]:
                    while True:
                        konfirmasi_hapus = input("Apakah data akan dihapus? (Y/N) : ")
                        if konfirmasi_hapus == "y"or konfirmasi_hapus == "Y":
                            for x in range(len(list_kar)):
                                if hapusnpk == list_kar[x]["NPK"]:
                                    list_kar.pop(x)
                                    print("Data telah dihapus..")
                                    break
                                else:
                                    continue
                            break
                        elif konfirmasi_hapus == "n"or konfirmasi_hapus == "N":
                            print("Data tidak dihapus..")
                            break
                        else:
                            continue     
                elif x == max(range(len(list_kar))):
                    print("data tidak tersedia!!")
                    break
                else:
                    continue
        elif pilih_menu_hapus == "2":
            break
        else:
            continue

# main_menu
while True:
    welcome() 
    opsi=input("Silahkan Pilih Menu: ")
    if opsi == "1":
        report()
    elif opsi == "2":
        tambahKaryawan()
    elif opsi == "3":
        updateData()
    elif opsi == "4":
        hapusDataKaryawan()
    elif opsi == "5":
        print("Terima Kasih!")
        break   
    else:
        print("Pilihan tidak tersedia. Silahkan coba lagi")