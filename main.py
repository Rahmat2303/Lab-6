from Boidata import Data

def menu():
    print("\n")
    print("=========== MENU ==============")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")

    menu = int (input("Masukkan pilihan dalam angka => "))

    if (menu == 1):
        Data.tambah()
    elif (menu == 2):
        Data.tampilkan()
    elif (menu == 3):
        Data.ubah()
    elif (menu == 4):
        Data.hapus()
    else:
        print("ANDA SALAH MEMASUKKAN PILIHAN !!!")

while(True):
    menu()