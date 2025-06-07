# Aplikasi Deteksi Katarak

Aplikasi web untuk mendeteksi katarak menggunakan model deep learning.

## Persyaratan

- Python 3.9 atau lebih baru
- pip (Python package manager)

## Instalasi

1. Clone repository ini:

```bash
git clone [URL_REPOSITORY]
cd katarak-app
```

2. Buat dan aktifkan virtual environment:

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Untuk Windows:
venv\Scripts\activate
# Untuk Linux/Mac:
source venv/bin/activate
```

3. Install dependensi:

```bash
pip install -r requirements.txt
```

## Penggunaan

1. Pastikan model sudah ada di folder `model/` dengan nama `final_model_100.h5`

2. Jalankan aplikasi:

```bash
streamlit run app.py
```

3. Buka browser dan akses `http://localhost:8501`

## Struktur Proyek

```
katarak-app/
├── app.py            # File utama aplikasi
├── requirements.txt  # Dependensi proyek
├── model/           # Folder untuk model
│   └── final_model_100.h5
├── examples/        # Gambar contoh
│   ├── normal.png
│   └── katarak.png
└── README.md        # Dokumentasi
```

## Catatan

- Pastikan model yang digunakan (`final_model_100.h5`) sudah dilatih dengan benar
- Gambar yang diunggah harus dalam format JPG, JPEG, atau PNG
- Ukuran gambar akan otomatis diubah menjadi 224x224 pixel
- Aplikasi ini menggunakan Streamlit versi 1.32.0
