"""
================================================================================
RANGKUMAN LENGKAP PEMBELAJARAN OPENCV - BOOTCAMP PROGRAMMING DAY 6
Topik: Pengenalan OpenCV, Operasi Dasar Citra, Preprocessing, Video/Webcam,
       dan Studi Kasus Deteksi Objek Berwarna (Ruang Warna HSV + OOP)
================================================================================

RINGKASAN KONSEP FUNDAMENTAL OPENCV:
1. Format Warna BGR : OpenCV membaca urutan kanal warna sebagai Blue, Green, Red
                      (BGR), BUKAN RGB.
2. Sistem Koordinat : Titik asal (0, 0) berada di POJOK KIRI ATAS gambar.
                      Sumbu X mengarah ke kanan (lebar), sumbu Y ke bawah (tinggi).
3. Struktur Matriks : Gambar direpresentasikan sebagai array NumPy.
                      Atribut `img.shape` menghasilkan `(tinggi, lebar, kanal)`.
4. Kontrol Jendela  : `cv2.waitKey(0)` menunggu tombol keyboard untuk gambar diam;
                      `cv2.waitKey(1)` dipakai di dalam loop video/webcam.
                      Selalu akhiri dengan `cv2.destroyAllWindows()`.

REFERENSI RENTANG WARNA HSV DI OPENCV (H: 0-179, S: 0-255, V: 0-255):
- Biru   : lower = [100, 120,  70] | upper = [130, 255, 255]
- Hijau  : lower = [ 35,  80,  70] | upper = [ 85, 255, 255]
- Kuning : lower = [ 20, 100, 100] | upper = [ 35, 255, 255]
- Merah  : lower = [  0, 120,  70] | upper = [ 10, 255, 255]

INSTALASI LIBRARY:
    pip install opencv-python numpy
================================================================================
"""

import cv2
import numpy as np


def tutup_jendela_aman():
    """Menutup seluruh jendela OpenCV dengan bersih di Windows maupun Ubuntu."""
    cv2.destroyAllWindows()
    cv2.waitKey(1)


# ==============================================================================
# BAGIAN 1: MEMBUAT, MENYIMPAN (imwrite), DAN MEMBACA GAMBAR (imread)
# ==============================================================================
def demo_1_baca_simpan_gambar(tampilkan=True):
    print("\n[1] Membuat & Membaca Gambar (cv2.imwrite & cv2.imread)...")

    # Membuat kanvas ukuran tinggi=400, lebar=600, 3 kanal warna (BGR)
    kanvas = np.ones((400, 600, 3), dtype=np.uint8) * 240  # Latar abu-abu terang

    # Menggambar objek berwarna (ingat format warna OpenCV adalah BGR)
    cv2.circle(kanvas, (130, 150), 60, (255, 50, 50), -1)           # Lingkaran BIRU
    cv2.rectangle(kanvas, (250, 90), (370, 210), (50, 200, 50), -1) # Kotak HIJAU
    cv2.circle(kanvas, (480, 150), 60, (0, 220, 255), -1)           # Lingkaran KUNING
    cv2.circle(kanvas, (300, 300), 55, (40, 40, 240), -1)           # Lingkaran MERAH
    cv2.putText(
        kanvas,
        "Bootcamp OpenCV Day 6",
        (150, 385),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (30, 30, 30),
        2,
    )

    # Menyimpan gambar ke disk
    nama_file = "sample_gambar.png"
    cv2.imwrite(nama_file, kanvas)

    # Membaca kembali gambar dari disk
    gambar = cv2.imread(nama_file, cv2.IMREAD_COLOR)
    if gambar is None:
        raise FileNotFoundError(f"Gagal membaca {nama_file}")

    print(f"    Dimensi (tinggi, lebar, kanal) : {gambar.shape}")
    print(f"    Tipe data piksel               : {gambar.dtype}")

    if tampilkan:
        print("    -> Tekan sembarang tombol pada keyboard untuk lanjut...")
        cv2.imshow("1. Hasil cv2.imread('sample_gambar.png')", gambar)
        cv2.waitKey(0)
        tutup_jendela_aman()

    return gambar


# ==============================================================================
# BAGIAN 2: OPERASI DASAR CITRA (RESIZE, CROPPING, KONVERSI RUANG WARNA)
# ==============================================================================
def demo_2_operasi_dasar():
    print("\n[2] Operasi Dasar: Resize, Cropping, Grayscale, dan HSV...")
    gambar = demo_1_baca_simpan_gambar(tampilkan=False)

    # 1. Resize: format ukuran adalah (lebar, tinggi)
    gambar_kecil = cv2.resize(gambar, (300, 200))

    # 2. Cropping: slicing array NumPy -> gambar[y_awal:y_akhir, x_awal:x_akhir]
    potongan_biru = gambar[70:230, 50:210]

    # 3. Konversi ruang warna
    abu_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(gambar, cv2.COLOR_BGR2HSV)

    print(f"    Ukuran asli: {gambar.shape} -> Setelah resize: {gambar_kecil.shape}")
    print("    -> Tekan sembarang tombol pada keyboard untuk menutup jendela...")

    cv2.imshow("2A. Resize (300x200)", gambar_kecil)
    cv2.imshow("2B. Cropping (Lingkaran Biru)", potongan_biru)
    cv2.imshow("2C. Grayscale (1 Kanal)", abu_abu)
    cv2.imshow("2D. Ruang Warna HSV", hsv)
    cv2.waitKey(0)
    tutup_jendela_aman()


# ==============================================================================
# BAGIAN 3: MENGGAMBAR BENTUK GEOMETRIS & ANOTASI TEKS
# ==============================================================================
def demo_3_menggambar_anotasi():
    print("\n[3] Menggambar Garis, Kotak, Lingkaran, dan Teks...")
    kanvas = np.zeros((400, 500, 3), dtype=np.uint8)

    # cv2.line(img, titik_awal, titik_akhir, warna_BGR, ketebalan)
    cv2.line(kanvas, (40, 40), (460, 40), (255, 0, 0), 3)

    # cv2.rectangle(img, kiri_atas, kanan_bawah, warna_BGR, ketebalan)
    cv2.rectangle(kanvas, (100, 90), (400, 290), (0, 255, 0), 2)

    # cv2.circle(img, pusat, radius, warna_BGR, -1 untuk penuh)
    cv2.circle(kanvas, (250, 190), 50, (0, 0, 255), -1)

    # cv2.putText(img, teks, posisi_kiri_bawah, font, skala, warna_BGR, ketebalan)
    cv2.putText(
        kanvas,
        "Visualisasi Anotasi",
        (125, 345),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )

    print("    -> Tekan sembarang tombol pada keyboard untuk lanjut...")
    cv2.imshow("3. Menggambar Bentuk & Teks", kanvas)
    cv2.waitKey(0)
    tutup_jendela_aman()


# ==============================================================================
# BAGIAN 4: PREPROCESSING (GAUSSIAN BLUR, THRESHOLDING, CANNY EDGE)
# ==============================================================================
def demo_4_filtering_dan_tepi():
    print("\n[4] Filtering (Gaussian Blur), Thresholding, dan Deteksi Tepi Canny...")
    demo_1_baca_simpan_gambar(tampilkan=False)
    gambar_gray = cv2.imread("sample_gambar.png", cv2.IMREAD_GRAYSCALE)

    # 1. Gaussian Blur: kernel wajib ganjil, contoh (5, 5)
    blur = cv2.GaussianBlur(gambar_gray, (5, 5), 0)

    # 2. Binary Thresholding: piksel > 180 menjadi 0, sisanya 255 (INV)
    _, biner = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY_INV)

    # 3. Canny Edge Detection: ambang bawah=50, ambang atas=150
    tepi = cv2.Canny(blur, 50, 150)

    print("    -> Tekan sembarang tombol pada keyboard untuk lanjut...")
    cv2.imshow("4A. Gaussian Blur", blur)
    cv2.imshow("4B. Binary Threshold", biner)
    cv2.imshow("4C. Deteksi Tepi Canny", tepi)
    cv2.waitKey(0)
    tutup_jendela_aman()


# ==============================================================================
# BAGIAN 5: PENGOLAHAN VIDEO & AKSES WEBCAM LIVE
# ==============================================================================
def demo_5a_video_file():
    print("\n[5A] Membuat & Memutar Berkas Video (VideoWriter & VideoCapture)...")
    lebar, tinggi, fps = 400, 250, 30
    nama_video = "sample_video.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(nama_video, fourcc, fps, (lebar, tinggi))

    for i in range(60):
        frame = np.ones((tinggi, lebar, 3), dtype=np.uint8) * 30
        pos_x = 40 + i * 5
        cv2.circle(frame, (pos_x, 125), 25, (0, 200, 255), -1)
        cv2.putText(
            frame,
            f"Frame: {i + 1}/60",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )
        writer.write(frame)
    writer.release()

    cap = cv2.VideoCapture(nama_video)
    print("    -> Memutar video simulasi (tekan 'q' untuk berhenti lebih awal)...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("5A. Pemutar Video (sample_video.mp4)", frame)
        if cv2.waitKey(33) & 0xFF == ord("q"):
            break

    cap.release()
    tutup_jendela_aman()


def demo_5b_webcam_live():
    print("\n[5B] Membuka Webcam Live (cv2.VideoCapture(0))...")
    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("    ⚠️ Webcam tidak terdeteksi! Pastikan kamera terhubung/tidak dipakai aplikasi lain.")
        return

    print("    🎥 Kamera aktif! Tekan tombol 'q' pada jendela kamera untuk keluar.")
    while True:
        ret, frame = kamera.read()
        if not ret:
            break

        # Flip horizontal agar tampilan seperti cermin
        frame = cv2.flip(frame, 1)
        cv2.putText(
            frame,
            "Webcam Live - Tekan 'q' untuk keluar",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )
        cv2.imshow("5B. Webcam Live", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    kamera.release()
    tutup_jendela_aman()


# ==============================================================================
# BAGIAN 6: STUDI KASUS AKHIR - DETEKSI OBJEK BERWARNA TERTENTU (HSV + OOP)
# ==============================================================================
class DetektorWarna:
    """
    Pipeline Deteksi Objek Berwarna:
    1. GaussianBlur  -> Mengurangi noise pada frame
    2. BGR ke HSV    -> Memisahkan informasi warna (Hue) dari kecerahan (Value)
    3. cv2.inRange   -> Membuat binary mask piksel yang masuk rentang warna target
    4. Morfologi     -> Membersihkan bintik putih (OPEN) & menambal lubang (CLOSE)
    5. findContours  -> Menemukan batas objek, menghitung luas, & menggambar bounding box
    """

    def __init__(self, nama_warna, batas_bawah, batas_atas, luas_minimal=800):
        self.nama_warna = nama_warna
        self.batas_bawah = np.array(batas_bawah, dtype=np.uint8)
        self.batas_atas = np.array(batas_atas, dtype=np.uint8)
        self.luas_minimal = luas_minimal
        self.kernel = np.ones((5, 5), np.uint8)

    def proses_frame(self, frame):
        hasil = frame.copy()

        # Tahap 1 & 2: Haluskan dan ubah ke ruang warna HSV
        blur = cv2.GaussianBlur(hasil, (7, 7), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        # Tahap 3: Masking rentang warna target
        mask = cv2.inRange(hsv, self.batas_bawah, self.batas_atas)

        # Tahap 4: Pembersihan noise morfologi
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.kernel)

        # Tahap 5: Ekstraksi kontur & penggambaran bounding box
        kontur_list, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for kontur in kontur_list:
            luas = cv2.contourArea(kontur)
            if luas > self.luas_minimal:
                x, y, w, h = cv2.boundingRect(kontur)
                pusat_x = x + w // 2
                pusat_y = y + h // 2

                cv2.rectangle(hasil, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(hasil, (pusat_x, pusat_y), 5, (0, 0, 255), -1)
                cv2.putText(
                    hasil,
                    f"{self.nama_warna} ({pusat_x}, {pusat_y})",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 200, 0),
                    2,
                )

        return hasil, mask

    def jalankan_pada_gambar(self, path_gambar):
        img = cv2.imread(path_gambar)
        if img is None:
            print(f"    ⚠️ Gambar '{path_gambar}' tidak ditemukan.")
            return

        hasil, mask = self.proses_frame(img)
        print(f"    -> Deteksi warna '{self.nama_warna}' pada gambar selesai.")
        print("    -> Tekan sembarang tombol pada keyboard untuk lanjut...")
        cv2.imshow(f"6A. Masking HSV ({self.nama_warna})", mask)
        cv2.imshow(f"6A. Hasil Deteksi ({self.nama_warna})", hasil)
        cv2.waitKey(0)
        tutup_jendela_aman()

    def jalankan_webcam(self, kamera_id=0):
        cap = cv2.VideoCapture(kamera_id)
        if not cap.isOpened():
            print("    ⚠️ Webcam tidak tersedia untuk deteksi real-time.")
            return

        print(
            f"    🎯 Mendeteksi objek warna '{self.nama_warna}' via webcam... "
            "Tekan 'q' untuk berhenti."
        )
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            hasil, mask = self.proses_frame(frame)

            cv2.imshow(f"6B. Deteksi Real-Time ({self.nama_warna})", hasil)
            cv2.imshow("6B. Masking HSV (Biner)", mask)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        tutup_jendela_aman()


def demo_6_studi_kasus_hsv():
    print("\n[6] Studi Kasus Akhir: Deteksi Objek Berwarna Tertentu (HSV)...")
    demo_1_baca_simpan_gambar(tampilkan=False)

    # Default target: BIRU (ubah ke Hijau: [35, 80, 70] - [85, 255, 255])
    detektor_biru = DetektorWarna(
        nama_warna="Biru",
        batas_bawah=[100, 120, 70],
        batas_atas=[130, 255, 255],
        luas_minimal=500,
    )

    # Uji terlebih dahulu pada gambar statis
    detektor_biru.jalankan_pada_gambar("sample_gambar.png")

    # Lanjutkan uji real-time pada webcam jika tersedia
    detektor_biru.jalankan_webcam(0)


# ==============================================================================
# MENU UTAMA EKSEKUSI RANGKUMAN
# ==============================================================================
if __name__ == "__main__":
    menu = {
        "1": ("Membaca, Membuat, & Menyimpan Gambar (imread / imwrite)", demo_1_baca_simpan_gambar),
        "2": ("Operasi Dasar: Resize, Cropping, Grayscale, & HSV", demo_2_operasi_dasar),
        "3": ("Menggambar Bentuk Geometris & Anotasi Teks", demo_3_menggambar_anotasi),
        "4": ("Preprocessing: Gaussian Blur, Thresholding, & Canny Edge", demo_4_filtering_dan_tepi),
        "5": ("Membuat & Memutar Berkas Video (VideoWriter & VideoCapture)", demo_5a_video_file),
        "6": ("Mengakses Webcam Live (VideoCapture(0))", demo_5b_webcam_live),
        "7": ("Studi Kasus Akhir: Deteksi Objek Warna HSV + OOP", demo_6_studi_kasus_hsv),
    }

    print("=" * 68)
    print("RANGKUMAN PRAKTIKUM OPENCV - BOOTCAMP PROGRAMMING DAY 6")
    print("=" * 68)
    for kunci, (judul, _) in menu.items():
        print(f"  [{kunci}] {judul}")
    print("  [0] Jalankan Semua Materi Berurutan (1 - 7)")
    print("=" * 68)

    pilihan = input("Pilih nomor materi yang ingin dijalankan [0-7] (Enter = 0): ").strip()

    if pilihan == "" or pilihan == "0":
        for kunci in ["1", "2", "3", "4", "5", "6", "7"]:
            menu[kunci][1]()
    elif pilihan in menu:
        menu[pilihan][1]()
    else:
        print("Pilihan tidak valid. Jalankan ulang skrip dan pilih angka 0 sampai 7.")

    print("\n✅ Selesai! Seluruh contoh kode OpenCV Day 6 berhasil dijalankan.")