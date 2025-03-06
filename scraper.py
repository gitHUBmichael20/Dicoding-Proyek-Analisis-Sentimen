from google_play_scraper import reviews_all, Sort
import pandas as pd

# Konfigurasi
app_id = "com.kurogame.wutheringwaves.global"  # ID aplikasi Wuthering Waves
max_reviews = 10000  # Target jumlah ulasan yang ingin diambil
data = []  # List untuk menyimpan data

# Scraping ulasan dengan looping
print("Memulai proses scraping...")
counter = 0

# Ambil ulasan dalam batch (500 per batch)
reviews = reviews_all(
    app_id,
    lang='id',  # Bahasa Indonesia
    country='id',  # Negara Indonesia
    sort=Sort.NEWEST,  # Urutkan dari ulasan terbaru
    count=max_reviews,  # Target jumlah ulasan
    sleep_milliseconds=1000  # Jeda antar request untuk hindari blokir
)

# Proses data
for idx, review in enumerate(reviews, 1):
    data.append({
        "Text": review["content"],
        "Rating": review["score"],
        "Tanggal": review["at"],
        "Username": review["userName"]
    })
    print(f"Sukses ambil data ke - {idx}")
    
    # Hentikan jika sudah mencapai 10.000
    if idx >= max_reviews:
        break

# Buat DataFrame dan tambahkan label
df = pd.DataFrame(data)
df["Label Sentimen"] = df["Rating"].apply(
    lambda x: "positif" if x > 3 else ("netral" if x == 3 else "negatif")
)

# Simpan ke CSV
df.to_csv("wuthering_waves_reviews.csv", index=False, encoding="utf-8")
print(f"\nTotal data berhasil diambil: {len(df)}")
print("Data disimpan di: wuthering_waves_reviews.csv")