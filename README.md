# Data Science Project: Menyelesaikan Permasalahan Marketing Suatu Bank Portugal

## Business Understanding
Terdapat sebuah institusi perbankan di Portugal melakukan kampanye pemasaran langsung (melalui panggilan telepon). Tujuan utama dari kampanye ini adalah untuk mempromosikan deposito berjangka kepada klien. Sering kali, lebih dari satu kontak diperlukan untuk klien yang sama guna menentukan apakah mereka akan berlangganan deposito berjangka atau tidak. Oleh karena itu, perlu dianalisis faktor-faktor yang mempengaruhi klien untuk berlangganan deposito berjangka.

### Permasalahan Bisnis
Institusi perbankan di Portugal ingin meningkatkan efektivitas kampanye pemasaran langsung mereka untuk memaksimalkan jumlah klien yang berlangganan deposito berjangka. Berikut adalah beberapa permasalahan bisnis utama yang dihadapi oleh institusi perbankan di Portugal tersebut:

1. Reputasi Institusi: Kampanye pemasaran yang kurang efektif dapat merusak citra institusi sebagai bank yang memahami dan memenuhi kebutuhan kliennya.
2. Kehilangan Pendapatan: Setiap kampanye yang gagal menghasilkan pelanggan baru berarti potensi pendapatan dari deposito berjangka yang hilang.
3. Ketidakpuasan Stakeholder: Ketidakmampuan untuk meningkatkan konversi dan efisiensi kampanye pemasaran dapat mengurangi kepercayaan klien, calon klien, dan stakeholder lainnya terhadap bank.

### Cakupan Proyek
1. Mengumpulkan dan memproses data yang diberikan oleh suatu Institusi perbankan di Portugal.
2. Menganalisis data untuk menemukan pola dan faktor-faktor yang mempengaruhi klien untuk berlangganan deposito berjangka.
3. Membangun model prediktif menggunakan algoritma XGBoost Classifier.
4. Membuat aplikasi web untuk memprediksi apakah calon klien akan berlangganan deposito berjangka.
5. Memberikan rekomendasi tindakan berdasarkan hasil analisis.

### Persiapan
Berikut adalah tahapan untuk menyiapkannya:

sumber data: https://archive.ics.uci.edu/dataset/222/bank+marketing

Setup environment:
Apabila menginstal Python melalui Anaconda ataupun miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system. Berikut merupakan tahapan dalam membuat virtual environment menggunakan conda untuk melakukan prediksi.

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_langganan python=3.9
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_langganan
    ```
4. Instal semua library yang dibutuhkan menggunakan perintah berikut.
    ```
    pip install numpy==1.24.4 pandas==2.1.4 matplotlib==3.7.5 seaborn==0.13.2 scikit-learn==1.4.0 streamlit==1.36.0 xgboost==2.0.3
    ```
5. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```
6. Buka file python prediction.py
7. Masukkan data yang ingin diprediksi pada variabel X_new
8. Tekan tombol run code
9. Hasil prediksi akan keluar
10. Bisa juga dengan mengakses link streamlit ini: https://menyelesaikan-permasalahan-marketing-suatu-bank-di-portugal.streamlit.app/

## Conclusion
faktor-faktor yang mempengaruhi klien untuk berlangganan deposito berjangka dipengaruhi oleh berbagai faktor yang dapat dikelompokkan ke dalam kampanye pemasaran, keadaan ekonomi, dan faktor demografis.

Dari faktor kampanye pemasaran, Calon klien yang terakhir di contact pada hari kamis, di contact pada bulan maret, jumlah kontak yang dilakukan selama kampanye lebih rendah, jumlah kontak yang dilakukan sebelum kampanye lebih besar cenderung berlangganan deposito berjangka.

Dari faktor ekonomi, calon klien yang mempunyai pekerjaan rumah, tidak mempunyai pinjaman pribadi, memakai cellular, contact rate yang lebih tinggi cenderung berlangganan deposito berjangka.

Dari faktor demografis, calon klien yang memiliki umur yang lebih tua, berstatus sebagai pelajar, dan buta huruf cenderung berlangganan deposito berjangka

Perlu diperhatikan bahwa calon klien yang dihubungi terakhir pada bulan mei memiliki keberhasilan lebih besar untuk berlangganan deposito berjangka

Namun perlu diperhatikan juga pada fitur previous dan contact rate memiliki ketimpangan data 

### Rekomendasi Action Items
Berikut adalah beberapa rekomendasi action items berdasarkan analisis faktor-faktor yang mempengaruhi keputusan calon klien untuk berlangganan deposito berjangka:

1. Optimalkan Strategi Kampanye Pemasaran:
    Fokuskan upaya pemasaran pada hari Kamis dan bulan Maret, di mana tingkat respons terhadap kampanye pemasaran cenderung lebih tinggi. Kurangi frekuensi kontak selama kampanye untuk meningkatkan efektivitas. Menargetkan calon klien dengan lebih sedikit kontak dapat meningkatkan kemungkinan mereka untuk berlangganan.

2. Perhatikan Faktor Ekonomi Calon Klien:
     Berikan penawaran khusus kepada calon klien yang memiliki pekerjaan rumah, tidak memiliki pinjaman pribadi, dan menggunakan komunikasi melalui ponsel (cellular).

3. Segmentasi Berdasarkan Faktor Demografis:
    Fokuskan pemasaran kepada calon klien yang lebih tua dan mereka yang berstatus sebagai pelajar atau buta huruf. Segmentasi ini dapat meningkatkan akurasi targeting dan meningkatkan tingkat keberhasilan berlangganan.

4. Peningkatan Efisiensi Kontak Terakhir:
    Fokuskan upaya pada kontak terakhir pada bulan Mei, di mana keberhasilan untuk mengonversi calon klien menjadi pelanggan deposito berjangka lebih besar. Pastikan tim pemasaran siap untuk menangkap peluang ini dengan strategi yang lebih intensif.

