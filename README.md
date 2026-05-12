# WooCommerce Price Updater via REST API 🚀

Script ini memudahkan pemilik toko online berbasis WooCommerce untuk memperbarui harga produk secara massal (bulk update) menggunakan file Excel. Script ini sangat berguna jika Anda memiliki ribuan produk dan ingin sinkronisasi harga dengan cepat tanpa harus klik satu per satu di dashboard WordPress.

## ✨ Fitur Utama
- **Bulk Update**: Memproses ratusan hingga ribuan baris data Excel sekaligus.
- **Exact Name Matching**: Mencari produk berdasarkan nama yang sama persis (case-insensitive) untuk menghindari salah update.
- **Error Logging**: Otomatis menghasilkan file `produk_gagal_update.xlsx` jika ada produk yang tidak ditemukan atau terjadi konflik nama.
- **Secure Integration**: Menggunakan WooCommerce REST API versi terbaru (v3).

## 📋 Prasyarat
- Python 3.x
- Pandas & Openpyxl (`pip install pandas openpyxl`)
- WooCommerce Python SDK (`pip install woocommerce`)

## 🛠️ Persiapan
1. **API Key**: Dapatkan `Consumer Key` dan `Consumer Secret` dari Dashboard WordPress anda (**WooCommerce > Settings > Advanced > REST API**).
2. **Format Excel**: Pastikan file Excel Anda bernama `data_harga.xlsx` dengan header kolom:
    - `Nama Produk`
    - `Harga`

## 🚀 Cara Penggunaan
1. Clone repositori ini:
   ```bash
   git clone [https://github.com/ilhamrofiqi/auto-update-harga-woocommerce.git]
   cd nama-repo
   ```

2. Buka file update_harga_web_api.py dan sesuaikan bagian kredensial:
   ```bash
   url="[https://domain-anda.com/]",
   consumer_key="ck_xxx",
   consumer_secret="cs_xxx",
   ```

3. Jalankan script:
   ```bash
   python update_harga_web_api.py
   ```
