data = []

# Menambah data
def tambah():
    nama = input("1. Nama       : ")
    nim = input("2. NIM        : ")
    uts = input("3. Nilai UTS  : ")
    uas = input("4. Nilai UAS  : ")
    data.append({"nama":nama, "nim":nim, "uts":uts, "uas":uas})

# Menampilkan data
def tampilkan():
    for raw in data:
        print("1. Nama      : ", raw["nama"])
        print("2. NIM       : ", raw["nim"])
        print("3. Nilai UTS : ", raw["uts"])
        print("4. Nilai UAS : ", raw["uas"])
        print("==============================")

# Menghapus data
def hapus():
    data.clear()
    print("Data Kosong !")

# Mengubah data
def ubah():
    data.clear()
    tambah()