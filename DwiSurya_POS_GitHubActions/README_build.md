
# PT. Dwi Surya POS — Build via GitHub Actions

## 🧩 Langkah-langkah
1. Buat repository baru di GitHub (nama bebas, mis. `DwiSurya_POS`).
2. Upload semua file dari ZIP ini, pastikan struktur seperti ini:

```
.github/workflows/build-windows.yml
main.py
README_build.md
```

3. Di tab **Actions**, aktifkan workflow (jika diminta).
4. Klik **Run workflow** → pilih branch utama (main).

Tunggu beberapa menit. Setelah selesai:
- Klik **Actions** → pilih workflow terakhir → scroll ke bawah.
- Klik **Artifacts** → Download `PT_Dwi_Surya_POS-exe.zip`.

Isi file itu adalah `PT_Dwi_Surya_POS.exe`, aplikasi kasir siap jalan tanpa Python.

## ⚙️ Fitur Utama
- Offline penuh
- Cetak struk thermal 58mm
- Laporan harian, ekspor Excel
- Manajemen stok, penjualan otomatis
- Tampilan abu-abu netral
