- Tautan menuju aplikasi Railway yang sudah kamu deploy
tugas2.up.railway.app

# Tugas 3

- Apakah kita dapat menginput data selain melalui form? 
Ada, salah satunya menggunakan shell Django. 

- Namun mengapa form dapat dikatakan lebih baik daripada menggunakan cara tersebut?
Form Django memiliki keamanan sehingga tidak mudah diretas, Form Django paling mudah untuk dikelola serta diperbaharui, Form Django menyediakan validasi data built-in

- Jelaskan perbedaan antara JSON, XML, dan HTML!

| JSON | XML | HTML |
| --- | --- | --- |
| JavaScript Object Notation | Extensible Markup Language | Hypertext Markup Language |
| Sangat mudah dibaca | Lebih susah dibaca | Mudah dibaca |
| Map Structure | Tree Structure | Tree Structure |
| .json | .xml | .html | 
| Cepat | Lambat | Cepat |
| Support arrays | Tidak support arrays | Tidak support arrays |
| mengirim data antar aplikasi web atau client-server | menyimpan, mengatur, dan memperdagangkan data secara independen dari perangkat lunak dan perangkat keras | membuat struktur, isi, dan tampilan halaman web, dan juga untuk menambahkan interaksi pengguna | 

- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform.
Karena data delivery karena membantu memperoleh data yang dibutuhkan dari berbagai sumber, mengoptimalkan kinerja sistem, dan menyediakan data yang akurat dan terbaru kepada pengguna

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
dengan bantuan tutorial minggu lalu, saya bisa mengerjakannya. membuat form sesuai yang diajarkan di tutorial kemudian menambahkan fungsi tugas pada views. Setelah itu menambahkan json dan xml yang sudah diajarkan. 

# Templat Proyek Django untuk Railway

Repositori ini berisi sebuah templat untuk membuat proyek Django yang siap di-*deploy* ke [Railway](https://railway.app/).

## Daftar Isi

- [Daftar Isi](#daftar-isi)
- [Instruksi Penggunaan](#instruksi-penggunaan)
- [Lisensi](#lisensi)
- [Referensi](#referensi)

## Instruksi Penggunaan

### Pengembangan Lokal

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi, ikuti langkah-langkah berikut.

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.

2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (*filesystem*) komputermu.

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```

3. Masuk ke dalam repositori yang sudah di-*clone* dan jalankan perintah berikut
   untuk menyalakan *virtual environment*.

   ```shell
   python -m venv env
   ```

4. Nyalakan *virtual environment* dengan perintah berikut.

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

5. Instal *dependencies* yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut.

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara lokal.

   ```shell
   python manage.py runserver
   ```

7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

### Pengembangan di Railway

1. Buka situs web [Railway](https://railway.app/) dan klik tombol `Start a New Project`.

2. Klik pilihan `Deploy from GitHub repo`.

3. Klik tombol `Login With GitHub` dan masuklah ke dalam akun GitHub kamu.

4. Kamu akan kembali ke halaman pembuatan proyek baru. Klik pilihan `Deploy from GitHub repo` dan klik `Configure GitHub App`.

5. Pilih tempat kamu menyimpan repositori program ini dan klik `Install & Authorize`.

6. Kamu akan kembali ke halaman pembuatan proyek baru. Klik pilihan `Deploy from GitHub repo` dan pilih repositori program ini.

7. Klik `Add variables` dan buat variabel baru dengan nama `APP_NAME` dan isikan nama aplikasi kamu yang akan dibuat menjadi URL aplikasi.

8. Klik menu `Settings` dan ubahlah URL yang ada pada bagian `Domains` sesuai dengan `APP_NAME` yang telah dispesifikasikan sebelumnya.

9. Tekan Control + K atau Command + K dan pilih `New Service -> Database -> Add PostgreSQL` untuk menginisiasi basis data PostgreSQL sebagai basis data yang digunakan.

## Lisensi

Templat ini didistribusikan dengan lisensi [MIT](LICENSE).

## Referensi

- [django-template-heroku](https://github.com/laymonage/django-template-heroku)
- [Templat Proyek Django PBP](https://github.com/pbp-fasilkom-ui/django-pbp-template)
- [Pindah dari Heroku ke Railway](https://determinedguy.github.io/cecoret/heroku-to-railway/)
