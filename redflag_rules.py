# redflag_rules.py
# Modul deteksi redflag otomatis dari data HR dan audit

import pandas as pd

# Fungsi deteksi redflag berdasarkan aturan sederhana
def detect_redflags(hr_df):
    df = hr_df.copy()

    # Contoh deteksi RF (bisa dikembangkan lebih lanjut)
    df["RF01"] = df["kinerja_delta"] < -20                 # Penurunan kinerja signifikan
    df["RF02"] = df["cuti_mendadak"] > 2                  # Cuti mendadak dalam 3 bulan
    df["RF03"] = df["burnout_score"] > 7                  # Skor burnout tinggi (1–10)
    df["RF04"] = df["terindikasi_kickback"] == True       # Audit menyebut dugaan kickback
    df["RF05"] = df["jumlah_pelatihan"] == 0              # Tidak aktif pelatihan > 12 bulan
    df["RF06"] = df["rotasi_tanpa_permohonan"] >= 2       # Sering dipindah paksa
    df["RF07"] = df["laporan_konflik"] == True            # Ada laporan konflik atau pelanggaran
    df["RF08"] = df["engagement_score"] < 50              # Keterlibatan rendah

    rf_cols = [f"RF0{i}" for i in range(1, 9)]
    df[rf_cols] = df[rf_cols].astype(int)

    return df[["nama", "unit"] + rf_cols]
