
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama Mahasiswa:", self.nama)
        print("NIM Mahasiswa:", self.nim)
        print("Jurusan Mahasiswa:", self.jurusan.nama_jurusan)
# Kelas mahasiswa


class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("➤ Daftar Mahasiswa", self.nama_jurusan, ":")
        if len(self.daftar_mahasiswa) > 0:
            print("No  | Nama Mahasiswa  | NIM")
            print("---------------------------------")
            for i, mahasiswa in enumerate(self.daftar_mahasiswa, 1):
                print(f"{i:2}  | {mahasiswa.nama:15} | {mahasiswa.nim}")
        else:
            print("Tidak ada mahasiswa terdaftar dalam jurusan ini.")
        
        print("")
# Kelas jurusan


class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("➤ Daftar Jurusan di", self.nama_universitas)
        if len(self.daftar_jurusan) > 0:
            for i, jurusan in enumerate(self.daftar_jurusan, 1):
                print(f"{i}. {jurusan.nama_jurusan}")
        else:
            print("Tidak ada jurusan terdaftar dalam universitas ini.")
        print("=======================================")
# Kelas universitas


universitas_xyz = Universitas("XYZ University")
# Membuat objek Universitas XYZ dengan nama "XYZ University"

jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)
# Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ


mhs1 = Mahasiswa("Evelyn", "G1A022024", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mhs1)

mhs2 = Mahasiswa("Mikasa", "G1A022040", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mhs2)

mhs3 = Mahasiswa("Eren", "G1A022030", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mhs3)
# Membuat objek Mahasiswa dengan nama Evelyn, NIM G1A022024, dan dua mahasiswa lain lalu menambahkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ


jurusan_tm = Jurusan("Teknik Mesin")
universitas_xyz.tambah_jurusan(jurusan_tm)

mhs4 = Mahasiswa("Levi", "G1C022025", jurusan_tm)
jurusan_tm.tambah_mahasiswa(mhs4)

mhs5 = Mahasiswa("Historia", "G1C022026", jurusan_tm)
jurusan_tm.tambah_mahasiswa(mhs5)

mhs6 = Mahasiswa("Ymir", "G1C022027", jurusan_tm)
jurusan_tm.tambah_mahasiswa(mhs6)
# Menambahkan Jurusan "Teknik Mesin" dan mahasiswa-mahasiswa di dalamnya


jurusan_te = Jurusan("Teknik Elektro")
universitas_xyz.tambah_jurusan(jurusan_te)

mhs7 = Mahasiswa("Armin", "G1D022028", jurusan_te)
jurusan_te.tambah_mahasiswa(mhs7)

mhs8 = Mahasiswa("Jean", "G1D022029", jurusan_te)
jurusan_te.tambah_mahasiswa(mhs8)

mhs9 = Mahasiswa("Annie", "G1D022030", jurusan_te)
jurusan_te.tambah_mahasiswa(mhs9)
# Menambahkan Jurusan "Teknik Elektro" dan mahasiswa-mahasiswa di dalamnya


universitas_xyz.tampilkan_daftar_jurusan()
# Menampilkan daftar jurusan yang ada di Universitas XYZ

jurusan_ti.tampilkan_daftar_mahasiswa()
# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ

jurusan_tm.tampilkan_daftar_mahasiswa()
# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Mesin di Universitas XYZ

jurusan_te.tampilkan_daftar_mahasiswa()
# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Elektro di Universitas XYZ