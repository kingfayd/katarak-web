import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import time
import os
import gdown

# Konfigurasi halaman
st.set_page_config(
    page_title="Deteksi Katarak",
    page_icon="👁️",
    layout="centered"
)

# Judul Aplikasi
st.markdown("<h1 style='text-align: center;'>Deteksi Katarak</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Unggah gambar mata untuk memeriksa apakah terdapat katarak</p>", unsafe_allow_html=True)

# Fungsi untuk mengunduh model
def download_model():
    model_path = 'model/final_model_100.h5'
    if not os.path.exists(model_path):
        os.makedirs('model', exist_ok=True)
        url = 'https://drive.google.com/uc?id=1FvjZ7fhonrKu9qdM-tR5b2e0aRVB6Yvc'
        gdown.download(url, model_path, quiet=False)
    return model_path

# Fungsi untuk memuat model
@st.cache_resource
def load_eye_model():
    try:
        model_path = download_model()
        model = load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Gagal memuat model: {str(e)}")
        return None

# Memuat model
model = load_eye_model()
if model is None:
    st.stop()

# Fungsi untuk prediksi
def predict_eye(image):
    img = Image.open(image).convert('RGB')
    img = img.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    probability = prediction[0][0]
    return ("NORMAL", float(probability)) if probability > 0.5 else ("KATARAK", float(1 - probability))

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar mata...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Tampilkan gambar yang diupload
    image = Image.open(uploaded_file)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image, caption='Gambar yang Diunggah', width=400)

    # Lakukan prediksi
    with st.spinner('Menganalisis...'):
        label, confidence = predict_eye(uploaded_file)
        time.sleep(1)

    st.success('Analisis selesai!')

    # Tampilkan hasil
    col1, col2 = st.columns(2)
    col1.metric("Hasil", label)
    col2.metric("Tingkat Kepercayaan", f"{confidence*100:.2f}%")

    # Saran berdasarkan hasil
    if label == "KATARAK":
        st.warning("Terdeteksi kemungkinan katarak. Silakan konsultasi dengan dokter spesialis mata.")
    else:
        st.info("Tidak terdeteksi katarak. Tetap jaga kesehatan mata dengan pemeriksaan rutin.") 