import time
import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(page_title="CampusQuest", page_icon="🎓", layout="centered")

# Judul dan Header Aplikasi
st.title("🎓 CampusQuest")
st.caption("Student Productivity Quest")
st.divider()

# Input Informasi Pengguna
name = st.text_input("Masukkan Nama:", placeholder="Contoh: Anezka")
fakultas = st.text_input("Masukkan Fakultas:", placeholder="Contoh: Teknik")

if name and fakultas:
    st.success(f"Selamat datang, **{name}** dari **{fakultas}**! 👋")
    st.write("---")
    
    # Input Aktivitas dan Durasi
    aktivitas = st.text_input("Kamu mau belajar apa hari ini?", placeholder="Contoh: Pemrograman Python")
    
    durasi_pilihan = st.selectbox(
        "Pilih Durasi Belajar:",
        ("15 menit", "30 menit", "45 menit", "60 menit")
    )
    
    # Tombol untuk Mulai Quest
    if st.button("🚀 Mulai Quest Belajar", type="primary"):
        if not aktivitas.strip():
            st.error("Aktivitas tidak boleh kosong!")
        else:
            durasi_menit = int(durasi_pilihan.split()[0])
            total_detik = durasi_menit * 60
            
            st.info(f"Fokus belajar **{aktivitas}** selama **{durasi_menit} menit** dimulai. Semangat! 🔥")
            
            # Wadah untuk Tampilan Timer dan Progress Bar
            status_text = st.empty()
            progress_bar = st.progress(0)
            
            # Hitung Mundur (Countdown Timer)
            for detik_berlalu in range(total_detik):
                sisa = total_detik - detik_berlalu
                menit_sisa = sisa // 60
                detik_sisa = sisa % 60
                
                # Tampilkan Waktu Berjalan
                status_text.metric(label="⏱️ Sisa Waktu", value=f"{menit_sisa:02d}:{detik_sisa:02d}")
                progress_bar.progress((detik_berlalu + 1) / total_detik)
                
                # Jeda 1 detik
                time.sleep(1)
            
            # Pengingat & Perayaan Selesai
            st.balloons()
            st.success("🎉 Waktu belajar selesai!")
            
            # Hitung XP
            xp = (durasi_menit // 15) * 10
            st.metric(label="Reward Terkumpul", value=f"+{xp} XP")
            
            # Catatan Kesehatan / Istirahat
            st.warning("💡 **Tips:** Jangan lupa istirahat 5-10 menit, minum air putih, dan regangkan tubuhmu!")
            