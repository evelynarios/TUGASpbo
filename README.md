# UAS pbo ( Pembuatan Aplikasi Notepad)
Nama: Evelyn Eunike Aritonang

NPM: G1A022024

Kelas: Informatika-B


Pada  Tugas  Akhir  kami  yang  diperuntukkan  UAS  kali  ini,  kami  membuat  Notepad  menggunakan  bahasa  pemrograman  Pyhton  menggunakan  tkinter.  
Notepad  memiliki  beragam  kegunaan  yang  membuatnya  menjadi  salah  satu  aplikasi  yang  penting  dalam  komputasi  sehari-hari.  Dengan  Notepad,  pengguna  dapat  membuat,  mengedit,  dan  menyimpan  catatan  teks  sederhana,  memo,  atau  daftar  tugas  yang  penting.  Selain  itu,  Notepad  juga  dapat  digunakan  untuk  menulis  dan  mengedit  kode  sederhana  dalam  bahasa  pemrograman,  melakukan  pengeditan  cepat  pada  file  konfigurasi,  menyimpan  catatan  penting  secara  sementara,  menyalin  dan  menempelkan  teks  tanpa  format,  serta  membaca  dan  memodifikasi  file  teks  biasa  dengan  mudah.  Kemudahan  penggunaan  dan  kesederhanaan  Notepad  menjadikannya  alat  yang  serbaguna  dan  praktis  untuk  penggunaan  sehari-hari.

Kami  akan  menjelaskan  secara  singkat  penjelasan  koding  yang  telah  kami  buat.  Berikut  penjelasannya  :  

Pertama ada `import tkinter as tk`: Baris ini mengimpor modul Tkinter dan memberikan alias `tk` ke modul tersebut. Tkinter digunakan untuk membuat antarmuka grafis (GUI) pada Python. dan`from tkinter import filedialog, messagebox, font`: Baris ini mengimpor beberapa kelas dan fungsi dari modul Tkinter yang akan digunakan, yaitu `filedialog`, `messagebox`, dan `font`.
Lalu  konstruktor  init,  kita  menginisialisasi  jendela  utama  (root)  menggunakan  root  yang  diterima  sebagai  argumen.  Kemudian,  kita  memberi  judul  pada  jendela  utama  menggunakan  self.root.title("Notepad").  Selanjutnya,  kita  membuat  area  teks  menggunakan  tk.Text(self.root)  dan  mengaturnya  agar  mengisi  seluruh  ruang  yang  tersedia  menggunakan  .pack(expand=True,  fill='both').  Terakhir,  kita  memanggil  metode  create_menu()  untuk  membuat  menu.

Selanjutnya create_menu()  dalam  kelas  Notepad.  Di  dalam  metode  ini,  kita  membuat  beberapa  menu  pada  menu-bar  yang  akan  ditampilkan  di  aplikasi  Notepad.Objek  menu-file  dibuat  menggunakan  tk.Menu(menu_bar,  tearoff=0).Kemudian,  kita  menambahkan  opsi-opsi  seperti  "New"  ,  "Open"  ,"Save"  ,dan  "Exit"menggunakan.add_command().menu_bar.add_cascade(label="File",menu=file_menu)  digunakan  untuk  menambahkan  menu-file  ke  dalam  menu-bar.Objekmenu-edit  dibuat  menggunakan  tk.Menu(menu_bar,  tearoff=0).

Kemudian,  kita  menambahkan  opsi-opsi  seperti  "Cut",  "Copy",  dan  "Paste"  menggunakan  .add_command().  menu_bar.add_cascade(label="Edit",  menu=edit_menu)  digunakan  untuk  menambahkan  menu-edit  ke  dalam  menu-bar.Objek

Menu-zoom  dibuat  menggunakan  tk.Menu(menu_bar,  tearoff=0).Kemudian,  kita  menambahkan  opsi-opsi  seperti  "Increase  Font  Size"  dan  "Decrease  Font  Size"  menggunakan  .add_command().menu_bar.add_cascade(label="Zoom",  menu=zoom_menu)  digunakan  untuk  menambahkan  menu-zoom  ke  dalam  menu-bar.Terakhir,  kita  mengatur  menu-bar  yang  telah  dibuat  pada  jendela  utama  menggunakan  self.root.config(menu=menu_bar).  Dengan  demikian,  menu-bar  akan  ditampilkan  di  aplikasi  Notepad.

Selanjutnya lagi metode  new_file(self):  Metode  ini  digunakan  untuk  membuat  file  baru  dengan  menghapus  seluruh  teks  yang  ada  di  dalam  text_area.  Ini  dilakukan  dengan  menggunakan  self.text_area.delete(1.0,  tk.END)  yang  menghapus  teks  dari  baris  1,  kolom  0  hingga  akhir  teks. 

Metode  open_file(self):  Metode  ini  digunakan  untuk  membuka  file  yang  ada  dengan  menggunakan  dialog  pemilihan  file  menggunakan  filedialog.askopenfilename().  Jika  file  berhasil  dipilih,  maka  metode  ini  akan  membaca  konten  file  tersebut  menggunakan  open(file_path,  'r')  dan  menghapus  teks  yang  ada  di  text_area.  Selanjutnya,  konten  file  akan  dimasukkan  ke  dalam  text_area  menggunakan  self.text_area.insert(tk.END,  file.read()).

Metode  save_file(self):  Metode  ini  digunakan  untuk  menyimpan  konten  text_area  ke  dalam  file  yang  dipilih  menggunakan  dialog  penyimpanan  file  menggunakan  filedialog.asksaveasfilename().  Jika  file  berhasil  dipilih,  maka  metode  ini  akan  membuka  file  tersebut  untuk  penulisan  menggunakan  open(file_path,  'w').  Kemudian,  konten  text_area  akan  diambil  menggunakan  self.text_area.get(1.0,  tk.END)  dan  ditulis  ke  dalam  file  menggunakan  file.write(text_content). 

Metode  exit_app(self):  Metode  ini  digunakan  untuk  keluar  dari  aplikasi  dengan  menghancurkan  jendela  utama  menggunakan  self.root.destroy().  Sebelum  keluar,  metode  ini  akan  menampilkan  dialog  konfirmasi  menggunakan  messagebox.askokcancel()  dengan  pesan  "Are  you  sure  you  want  to  quit?".  Jika  pengguna  memilih  "OK",  maka  jendela  utama  akan  dihancurkan.


Pada  kode  exit_app(self):  Metode  ini  digunakan  untuk  menutup  aplikasi  notepad.  Ketika  metode  ini  dipanggil,  ia  akan  menampilkan  kotak  dialog  konfirmasi  "Are  you  sure  you  want  to  quit?"  menggunakan  messagebox.askokcancel.  Jika  pengguna  menekan  tombol  "OK",  maka  self.root.destroy()  akan  dipanggil  untuk  menutup  jendela  notepad.  

cut_text(self):  Metode  ini  menghasilkan  peristiwa  "Cut"  pada  text_area.  Dengan  demikian,  teks  yang  dipilih  dalam  text_area  akan  dipotong  ke  clipboard.  copy_text(self):  Metode  ini  menghasilkan  peristiwa  "Copy"  pada  text_area.  Ini  akan  menyalin  teks  yang  dipilih  dalam  text_area  ke  clipboard.  paste_text(self):  Metode  ini  menghasilkan  peristiwa  "Paste"  pada  text_area.  Ini  akan  mengambil  teks  dari  clipboard  dan  memasukkannya  ke  text_area  pada  posisi  kursor  saat  ini.

increase_font_size(self):  Metode  ini  digunakan  untuk  meningkatkan  ukuran  font  dalam  text_area.  Itu  mengambil  ukuran  font  saat  ini  dari  text_area,  menambahkannya  dengan  1,  dan  kemudian  memanggil  metode  change_font_size  dengan  ukuran  font  yang  baru.  decrease_font_size(self):  Metode  ini  digunakan  untuk  mengurangi  ukuran  font  dalam  text_area.  Ini  mirip  dengan  increase_font_size,  tetapi  mengurangi  ukuran  font  dengan  1  dan  memeriksa  agar  ukuran  font  tidak  menjadi  negatif  sebelum  memanggil  change_font_size.  change_font_size(self,  size):  Metode  ini  mengubah  ukuran  font  dalam  text_area  menjadi  ukuran  yang  diberikan.  Itu  mengambil  keluarga  font  saat  ini  dari  text_area  dan  kemudian  mengonfigurasi  text_area  dengan  font  yang  baru,  yang  menggunakan  ukuran  yang  diberikan  tetapi  keluarga  font  yang  sama.

Kode  if  name  ==  'main':  merupakan  konvensi  dalam  Python  yang  menjalankan  blok  kode  yang  berada  di  dalamnya  hanya  jika  file  tersebut  dijalankan  langsung  sebagai  program  utama.  root  =  tk.Tk():  Baris  ini  membuat  objek  Tkinter  baru  dengan  menyimpannya  dalam  variabel  root.  Objek  Tkinter  ini  merupakan  jendela  utama  aplikasi  yang  akan  menampung  elemen-elemen  GUI  yang  akan  ditampilkan.  notepad  =  Notepad(root)  Pada  baris  ini,  objek  Notepad  dibuat  dengan  memberikan  root  sebagai  argumen  konstruktor.  Dengan  melakukan  ini,  objek  Notepad  akan  memiliki  akses  ke  jendela  utama  root  dan  dapat  menambahkan  elemen-elemen  GUI  ke  dalamnya.  root.mainloop()  Metode  mainloop()  adalah  metode  utama  dalam  aplikasi  Tkinter.  Ini  akan  menjalankan  loop  utama  yang  akan  merespons  input  pengguna,  memperbarui  tampilan,  dan  mempertahankan  aplikasi  tetap  berjalan  sampai  jendela  ditutup.  Jadi,  dengan  memanggil  root.mainloop(),  aplikasi  Tkinter  akan  dimulai  dan  berjalan  secara  terus-menerus  sampai  jendela  ditutup.
