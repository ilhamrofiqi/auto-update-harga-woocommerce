import pandas as pd
from woocommerce import API

wcapi = API(
    url="https://oneit-solution.com/",
    consumer_key="ck_xxx",
    consumer_secret="cs_xxx",
    version="wc/v3",
    timeout=60
)

def update_harga_dengan_log_lengkap(file_path):
    # Membaca file utama
    df = pd.read_excel(file_path)
    
    # List untuk menampung data yang tidak berhasil diupdate
    log_gagal = []
    
    print(f"Memproses {len(df)} baris data...")

    for index, row in df.iterrows():
        nama_excel = str(row['Nama Produk']).strip()
        harga_baru = str(row['Harga']).strip()

        try:
            # Cari produk berdasarkan nama
            res = wcapi.get("products", params={"search": nama_excel}).json()

            # Skenario 1: Produk benar-benar tidak ada di website
            if not res:
                print(f"[-] Skip: {nama_excel} (Tidak ditemukan)")
                log_gagal.append({
                    "Nama Produk": nama_excel, 
                    "Harga": harga_baru, 
                    "Alasan": "Tidak ditemukan di website"
                })
                continue

            # Logika Exact Match
            produk_target = None
            for p in res:
                if p['name'].strip().lower() == nama_excel.lower():
                    produk_target = p
                    break
            
            # Skenario 2: Nama identik ditemukan
            if produk_target:
                p_id = produk_target['id']
                wcapi.put(f"products/{p_id}", {"regular_price": harga_baru})
                print(f"[+] Berhasil: {nama_excel} -> Rp {harga_baru}")
            
            # Skenario 3: Ada hasil pencarian, tapi tidak ada yang namanya sama persis
            else:
                print(f"[!] Konflik: {nama_excel} (Nama tidak identik)")
                log_gagal.append({
                    "Nama Produk": nama_excel, 
                    "Harga": harga_baru, 
                    "Alasan": "Ditemukan kemiripan tapi nama tidak identik (cek manual)"
                })

        except Exception as e:
            print(f"[!] Error pada {nama_excel}: {str(e)}")
            log_gagal.append({
                "Nama Produk": nama_excel, 
                "Harga": harga_baru, 
                "Alasan": f"Error Teknis: {str(e)}"
            })

    # Simpan laporan kegagalan ke file Excel baru
    if log_gagal:
        df_gagal = pd.DataFrame(log_gagal)
        # Mengatur urutan kolom agar rapi
        df_gagal = df_gagal[["Nama Produk", "Harga", "Alasan"]]
        df_gagal.to_excel("produk_gagal_update.xlsx", index=False)
        print(f"\nProses selesai. {len(log_gagal)} produk gagal diupdate.")
        print("Cek file 'produk_gagal_update.xlsx' untuk detailnya.")
    else:
        print("\nProses selesai. Semua produk berhasil diupdate!")

# Jalankan fungsi
update_harga_dengan_log_lengkap("data_harga.xlsx")
