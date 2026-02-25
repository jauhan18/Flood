#  Flood Probability Prediction

## Deskripsi Proyek
Proyek ini bertujuan untuk memprediksi probabilitas terjadinya banjir (*Flood Probability*) di suatu wilayah berdasarkan berbagai interaksi kompleks dari faktor lingkungan, kualitas infrastruktur, dan variabel sosial ekonomi. Proyek ini sangat berguna untuk upaya mitigasi bencana dan perencanaan tata ruang yang lebih cerdas.


## Dataset
Dataset yang digunakan dalam proyek ini bersumber dari dataset Kaggle (`jauhanahmad/flood`). 
Data ini memiliki lebih dari 1 juta baris untuk data latih (train) dan berisi 20 fitur prediktor, antara lain:
- `MonsoonIntensity` (Intensitas Monsun)
- `TopographyDrainage` (Topografi dan Drainase)
- `Deforestation` (Tingkat Deforestasi)
- `Urbanization` (Tingkat Urbanisasi)
- `ClimateChange` (Dampak Perubahan Iklim)
- `DamsQuality` (Kualitas Bendungan)
- `AgriculturalPractices` (Praktik Pertanian)
- Fitur pendukung lainnya yang berdampak pada risiko hidrologis.

## Alur Kerja (Pipeline)
1. **Data Loading:** Memuat data latih (`train.csv`) dan data uji (`test.csv`).
2. **Data Cleaning & Transformasi:** - Pengecekan *missing values* (data kosong).
   - Analisis statistik deskriptif untuk memahami sebaran data.
3. **Exploratory Data Analysis (EDA):** Menggunakan *box plot* untuk mendeteksi *outliers* pada setiap fitur independen.
4. **Model Training & Evaluasi:** Melatih beberapa algoritma regresi dan membandingkan performanya.

## Hasil Evaluasi Model
Beberapa model dievaluasi menggunakan metrik *Mean Absolute Error* (MAE), *Mean Squared Error* (MSE), dan *R-squared* (R²). Hasil yang didapatkan adalah:

| Model | MAE | MSE | R² Score |
| :--- | :--- | :--- | :--- |
| **Linear Regression** | **0.329** | **0.171** | **0.828** |
| Gradient Boosting Regressor | 0.512 | 0.380 | 0.619 |
| LARS | 0.806 | 0.998 | 0.0007 |

Berdasarkan pengujian, algoritma **Linear Regression** bekerja paling optimal pada dataset ini, mampu menjelaskan sekitar 82.8% variansi dari probabilitas banjir.

## Teknologi & Library
- **Python 3**
- **Pandas** (Manipulasi Data)
- **Matplotlib & Seaborn** (Visualisasi Data)
- **Scikit-Learn** (Pemodelan Machine Learning)

## Cara Menjalankan Proyek
1. *Clone* repositori ini:
   ```bash
   git clone [https://github.com/jauhan18/Flood.git](https://github.com/jauhan18/Flood.git)

jika tidak ada library, install :
 pip install pandas matplotlib seaborn scikit-learn
