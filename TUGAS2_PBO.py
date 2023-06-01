class Mahasiswa:
    def __init__(self, nama, npm, prodi):
        self.nama = nama  # Menyimpan nama mahasiswa ke atribut 'nama'
        self.npm = npm  # Menyimpan NPM mahasiswa ke atribut 'npm'
        self.prodi = prodi  # Menyimpan objek prodi ke atribut 'prodi'

    def tampilkan_info(self):
        print("Nama:", self.nama)  # Menampilkan nama mahasiswa
        print("NPM:", self.npm)  # Menampilkan NPM mahasiswa
        print("Prodi:", self.prodi.NamaProdi)  # Menampilkan nama prodi melalui atribut 'NamaProdi' pada objek prodi


class Prodi:
    def __init__(self, nama_prodi):
        self.NamaProdi = nama_prodi  # Menyimpan nama prodi ke atribut 'NamaProdi'
        self.DaftarMahasiswa = []  # Menyimpan daftar mahasiswa ke atribut 'DaftarMahasiswa'

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)  # Menambahkan objek mahasiswa ke dalam daftar mahasiswa pada objek prodi

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa", self.NamaProdi + ":")  # Menampilkan judul daftar mahasiswa berdasarkan nama prodi
        for mahasiswa in self.DaftarMahasiswa:
            print("- Nama:", mahasiswa.nama)  # Menampilkan nama mahasiswa
            print("  NPM:", mahasiswa.npm)  # Menampilkan NPM mahasiswa


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas  # Menyimpan nama universitas ke atribut 'NamaUniversitas'
        self.DaftarProdi = []  # Menyimpan daftar prodi ke atribut 'DaftarProdi'

    def tambah_prodi(self, prodi):
        self.DaftarProdi.append(prodi)  # Menambahkan objek prodi ke dalam daftar prodi pada objek universitas

    def tampilkan_daftar_prodi(self):
        print("Daftar prodi di", self.NamaUniversitas + ":")  # Menampilkan judul daftar prodi berdasarkan nama universitas
        for prodi in self.DaftarProdi:
            print("- Prodi:", prodi.NamaProdi)  # Menampilkan nama prodi


# 1. Implementasi kelas Mahasiswa, Jurusan, dan Universitas sesuai dengan spesifikasi yang diberikan.

# 2. Buatlah sebuah objek Universitas dengan nama "XYZ University".
xyz_university = Universitas("XYZ University")

# 3. Buatlah objek Jurusan dengan nama "Teknik Informatika" dan tambahkan objek tersebut ke dalam Universitas XYZ.
teknik_informatika = Prodi("Teknik Informatika")
xyz_university.tambah_prodi(teknik_informatika)

# 4. Buatlah objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ.
mahasiswa_1 = Mahasiswa("M. Satria Halim", "G1A022080", teknik_informatika)
teknik_informatika.tambah_mahasiswa(mahasiswa_1)

# 5. Tampilkan daftar jurusan yang ada di Universitas XYZ.
xyz_university.tampilkan_daftar_prodi()

# 6. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.
teknik_informatika.tampilkan_daftar_mahasiswa()
