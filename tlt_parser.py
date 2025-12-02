import yfinance as yf
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def download_data():
    try:
        # Загружаем исторические данные по TLT
        tlt = yf.Ticker("NVDA")
        df = tlt.history(period="max")

        # Убираем таймзону, иначе Excel ругается
        df.index = df.index.tz_localize(None)

        # Сохраняем в Excel
        output_file = "tlt_history.xlsx"
        df.to_excel(output_file)

        messagebox.showinfo("Готово", f"Файл {output_file} сохранён рядом с программой!")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


# --- GUI ---
root = tk.Tk()
root.title("Парсер TLT")
root.geometry("300x120")

label = tk.Label(root, text="Скачать исторические данные TLT")
label.pack(pady=10)

btn = tk.Button(root, text="Скачать данные", command=download_data)
btn.pack(pady=10)

root.mainloop()
