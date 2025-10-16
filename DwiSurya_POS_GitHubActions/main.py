
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3, datetime, pandas as pd

DB_FILE = "pos_data.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS produk(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        harga REAL,
        stok INTEGER
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS penjualan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal TEXT,
        nama_produk TEXT,
        qty INTEGER,
        total REAL
    )''')
    conn.commit()
    conn.close()

def tambah_penjualan(nama, qty):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT harga, stok FROM produk WHERE nama=?", (nama,))
    row = c.fetchone()
    if not row:
        messagebox.showerror("Error", f"Produk '{nama}' tidak ditemukan")
        return
    harga, stok = row
    if qty > stok:
        messagebox.showerror("Error", "Stok tidak cukup!")
        return
    total = harga * qty
    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO penjualan (tanggal,nama_produk,qty,total) VALUES (?,?,?,?)",
              (tanggal, nama, qty, total))
    c.execute("UPDATE produk SET stok=stok-? WHERE nama=?", (qty, nama))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sukses", f"Penjualan {nama} x{qty} berhasil. Total Rp{total:,.0f}")

def ekspor_excel():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM penjualan", conn)
    conn.close()
    fname = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel","*.xlsx")])
    if fname:
        df.to_excel(fname, index=False)
        messagebox.showinfo("Export", "Data berhasil diekspor ke Excel.")

def ui():
    win = tk.Tk()
    win.title("PT. Dwi Surya POS")
    win.geometry("400x400")
    win.configure(bg="#e0e0e0")
    ttk.Label(win, text="PT. Dwi Surya POS", font=("Segoe UI", 14, "bold")).pack(pady=10)

    frame = ttk.Frame(win)
    frame.pack(pady=10)
    ttk.Label(frame, text="Nama Produk").grid(row=0, column=0, padx=5, pady=5)
    nama = ttk.Entry(frame); nama.grid(row=0, column=1, padx=5)
    ttk.Label(frame, text="Jumlah").grid(row=1, column=0, padx=5, pady=5)
    qty = ttk.Entry(frame); qty.grid(row=1, column=1, padx=5)

    ttk.Button(win, text="Tambah Penjualan", command=lambda: tambah_penjualan(nama.get(), int(qty.get() or 0))).pack(pady=5)
    ttk.Button(win, text="Ekspor ke Excel", command=ekspor_excel).pack(pady=5)
    ttk.Button(win, text="Keluar", command=win.destroy).pack(pady=10)
    win.mainloop()

if __name__ == "__main__":
    init_db()
    ui()
