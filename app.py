import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Simulasi Statistik Deskriptif")

# Input data
uploaded = st.file_uploader("Unggah file CSV", type="csv")
manual = st.text_area("Masukkan data manual (pisahkan koma)", "")

if uploaded:
    df = pd.read_csv(uploaded)
    data = df.iloc[:,0].dropna().astype(float).values
elif manual:
    try:
        data = np.array(list(map(float, manual.split(","))))
    except:
        st.error("Format data manual tidak valid.")
        data = None
else:
    data = None

if data is not None and len(data) > 0:
    # Perhitungan
    mean = np.mean(data)
    median = np.median(data)
    mode = pd.Series(data).mode().iloc[0]
    var = np.var(data, ddof=1)
    sd = np.std(data, ddof=1)

    st.subheader("📋 Hasil Statistik")
    st.write({
        "Mean": mean,
        "Median": median,
        "Modus": mode,
        "Varians": var,
        "Standar Deviasi": sd
    })

    # Grafik
    fig, axes = plt.subplots(1, 2, figsize=(12,4))
    sns.histplot(data, kde=True, ax=axes[0]).set_title("Histogram")
    sns.boxplot(x=data, ax=axes[1]).set_title("Boxplot")
    st.pyplot(fig)
elif data is not None:
    st.warning("Tidak ada data untuk dianalisis.")
