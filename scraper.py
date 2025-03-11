from google_play_scraper import reviews, Sort
import pandas as pd

# Konfigurasi
app_id = "com.kurogame.wutheringwaves.global"  # ID aplikasi Wuthering Waves
max_reviews = 10000  # Target jumlah ulasan yang ingin diambil
data = []  # List untuk menyimpan data
batch_size = 100  # Jumlah ulasan per batch
counter = 0  # Counter untuk menghitung jumlah ulasan yang sudah diambil
continuation_token = None  # Token untuk melanjutkan pengambilan data

print("Memulai proses scraping...")

# Looping untuk mengambil data secara bertahap
while counter < max_reviews:
    # Ambil ulasan dalam batch
    result, continuation_token = reviews(
        app_id,
        lang='id',  # Bahasa Indonesia
        country='id',  # Negara Indonesia
        sort=Sort.NEWEST,  # Urutkan dari ulasan terbaru
        count=batch_size,  # Ambil 100 ulasan per batch
        continuation_token=continuation_token if counter > 0 else None  # Token untuk melanjutkan
    )

    # Proses data dalam batch
    for review in result:
        data.append({
            "Username": review["userName"],
            "Text": review["content"],
            "Rating": review["score"],
            "Tanggal": review["at"],
            "Jumlah Suka": review["thumbsUpCount"],
            "Balasan Pengembang": review["replyContent"] if review["replyContent"] else None,
            "Versi Aplikasi": review["reviewCreatedVersion"] if review["reviewCreatedVersion"] else None
        })
        counter += 1
        print(f"Sukses ambil data ke - {counter}")

        # Hentikan jika sudah mencapai 10.000
        if counter >= max_reviews:
            break

    # Jika tidak ada lagi ulasan yang tersedia, hentikan
    if not continuation_token:
        print("Tidak ada lagi ulasan yang tersedia.")
        break

# Buat DataFrame
df = pd.DataFrame(data)

# Simpan ke CSV
df.to_csv("dataset.csv", index=False, encoding="utf-8")
print(f"\nTotal data berhasil diambil: {len(df)}")
print("Data disimpan di: dataset.csv")