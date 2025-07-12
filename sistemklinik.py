# Muhammad Fachry Albany IF24B (1012) 
# Aplikasi Sistem Antrian Klinik

import csv
from collections import deque
import os

# Inisialisasi struktur data
data_pasien = {}  # HashMap: {ID: {Nama, Umur, Keluhan}}
antrian = deque()  # Queue untuk antrian pasien
filename = 'data_pasien.csv'

# =========================
# Fungsi Baca Data dari CSV
# =========================
def load_data():
    if not os.path.isfile(filename):
        print("File CSV tidak ditemukan, membuat file baru.")
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Umur', 'Keluhan'])
        return

    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id_pasien = row['ID']
            data_pasien[id_pasien] = {
                'Nama': row['Nama'],
                'Umur': row['Umur'],
                'Keluhan': row['Keluhan']
            }
            antrian.append(id_pasien)

# =========================
# Fungsi Simpan Data ke CSV
# =========================
def save_data():
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['ID', 'Nama', 'Umur', 'Keluhan']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for id_pasien, info in data_pasien.items():
            writer.writerow({
                'ID': id_pasien,
                'Nama': info['Nama'],
                'Umur': info['Umur'],
                'Keluhan': info['Keluhan']
            })

# =========================
# Tambah Pasien Baru (Create)
# =========================
def tambah_pasien():
    id_pasien = input("Masukkan ID Pasien: ")
    if id_pasien in data_pasien:
        print("ID sudah terdaftar.")
        return

    nama = input("Masukkan Nama: ")
    umur = input("Masukkan Umur: ")
    keluhan = input("Masukkan Keluhan: ")

    data_pasien[id_pasien] = {'Nama': nama, 'Umur': umur, 'Keluhan': keluhan}
    antrian.append(id_pasien)
    save_data()
    print(f"Pasien {nama} berhasil didaftarkan dan masuk antrian.")

# =========================
# Panggil Pasien (FIFO)
# =========================
def panggil_pasien():
    if not antrian:
        print("Tidak ada pasien dalam antrian.")
        return

    id_pasien = antrian.popleft()
    info = data_pasien.get(id_pasien, {})

    print(f"Memanggil Pasien:")
    print(f"ID: {id_pasien}")
    print(f"Nama: {info.get('Nama', '-')}")
    print(f"Umur: {info.get('Umur', '-')}")
    print(f"Keluhan: {info.get('Keluhan', '-')}")

# =========================
# Cari Data Pasien berdasarkan ID (Read)
# =========================
def cari_pasien():
    id_pasien = input("Masukkan ID Pasien yang dicari: ")
    info = data_pasien.get(id_pasien)

    if info:
        print(f"Data Pasien:")
        print(f"ID: {id_pasien}")
        print(f"Nama: {info['Nama']}")
        print(f"Umur: {info['Umur']}")
        print(f"Keluhan: {info['Keluhan']}")
    else:
        print("Data pasien tidak ditemukan.")

# =========================
# Edit Data Pasien (Update)
# =========================
def edit_pasien():
    id_pasien = input("Masukkan ID Pasien yang akan diedit: ")
    if id_pasien not in data_pasien:
        print("Data pasien tidak ditemukan.")
        return

    nama = input("Masukkan Nama baru: ")
    umur = input("Masukkan Umur baru: ")
    keluhan = input("Masukkan Keluhan baru: ")

    data_pasien[id_pasien] = {'Nama': nama, 'Umur': umur, 'Keluhan': keluhan}
    save_data()
    print("Data pasien berhasil diperbarui.")

# =========================
# Hapus Data Pasien (Delete)
# =========================
def hapus_pasien():
    id_pasien = input("Masukkan ID Pasien yang akan dihapus: ")
    if id_pasien not in data_pasien:
        print("Data pasien tidak ditemukan.")
        return

    del data_pasien[id_pasien]

    try:
        antrian.remove(id_pasien)
    except ValueError:
        pass  # Pasien tidak ada dalam antrian

    save_data()
    print("Data pasien berhasil dihapus.")

# =========================
# Tampilkan Antrian Saat Ini
# =========================
def tampilkan_antrian():
    if not antrian:
        print("Antrian kosong.")
        return

    print("Daftar Antrian:")
    for i, id_pasien in enumerate(antrian, start=1):
        print(f"{i}. {id_pasien} - {data_pasien[id_pasien]['Nama']}")

# =========================
# Menu Utama Program
# =========================
def menu():
    load_data()

    while True:
        print("\n===== Sistem Antrian Klinik =====")
        print("1. Tambah Pasien Baru (Create)")
        print("2. Panggil Pasien")
        print("3. Cari Data Pasien (Read)")
        print("4. Edit Data Pasien (Update)")
        print("5. Hapus Data Pasien (Delete)")
        print("6. Tampilkan Antrian")
        print("7. Keluar Program")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_pasien()
        elif pilihan == '2':
            panggil_pasien()
        elif pilihan == '3':
            cari_pasien()
        elif pilihan == '4':
            edit_pasien()
        elif pilihan == '5':
            hapus_pasien()
        elif pilihan == '6':
            tampilkan_antrian()
        elif pilihan == '7':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan Program
if __name__ == "__main__":
    menu()
