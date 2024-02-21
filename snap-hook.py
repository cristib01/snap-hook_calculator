import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from snap_hooks_data import *

ROOT_WIDTH = 1000
ROOT_HEIGHT = 800


def afiseaza_informatii():
    selectie = dropdown_var.get()

    # Șterge orice imagine anterioară și câmpuri
    canvas.delete("all")
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) and hasattr(afiseaza_campuri, 'campuri_frame'):
            widget.destroy()

    # Afișează informațiile despre snap-hook
    for snap_hook in snap_hooks:
        if snap_hook["nume"] == selectie:
            canvas.delete("all")
            afiseaza_imagine(snap_hook["cale_imagine"])
            afiseaza_campuri(snap_hook["campuri"])
            calculeaza_button.config(state=tk.NORMAL)
            afisare_label.config(text=f"Introduceți informațiile despre {snap_hook['nume']}:")

            # Adaugă butonul "Tabele ajutătoare" pentru C1, C2, C3, D1, D2, D3
            if snap_hook["nume"] in ["C1", "C2", "C3", "D1", "D2", "D3"]:
                tabel_button = tk.Button(root, text="Tabele ajutătoare",
                                         command=lambda s=snap_hook: afiseaza_tabele_ajutatoare(s),
                                         font=("Arial", 12), width=int(ROOT_WIDTH / 25))
                tabel_button.grid(row=5, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

            break

    # Restabilește eticheta de afișare și dropdown
    afisare_label.grid(row=3, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)
    dropdown.grid(row=0, column=0, pady=10, sticky=tk.W)


def afiseaza_tabele_ajutatoare(snap_hook):
    # Creează un nou window pentru tabele ajutătoare
    tabel_window = tk.Toplevel(root)
    tabel_window.title("Tabele ajutătoare")

    # Alege calea corectă a imaginii în funcție de tipul snap-hook-ului
    if snap_hook["nume"] in ["C1", "C2", "C3"]:
        cale_imagine = "media/K1K2.JPG"  # Înlocuiți "cale_imagini_tabel_c.jpg" cu calea reală către imaginea C
    elif snap_hook["nume"] in ["D1", "D2", "D3"]:
        cale_imagine = "Z1Z2.JPG"  # Înlocuiți "cale_imagini_tabel_d.jpg" cu calea reală către imaginea D

    # Adaugă imaginea în noul window
    imagine_tabel = Image.open(cale_imagine)
    img_tk_tabel = ImageTk.PhotoImage(imagine_tabel)

    label_tabel = tk.Label(tabel_window, image=img_tk_tabel)
    label_tabel.image = img_tk_tabel
    label_tabel.pack()


def afiseaza_imagine(cale_imagine):
    global ROOT_HEIGHT, ROOT_WIDTH
    # Obține calea curentă a directorului scriptului
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construiește calea absolută la imagine
    imagine_abs_path = os.path.join(current_dir, cale_imagine)

    # Deschide imaginea folosind modulul Pillow
    imagine = Image.open(imagine_abs_path)
    # Redimensioneaza imaginea dacă este necesar
    imagine = imagine.resize((int(158), int(155)))

    # Converteste imaginea in format Tkinter PhotoImage
    img_tk = ImageTk.PhotoImage(imagine)

    # Adauga imaginea pe canvas
    canvas.create_image(int(1), int(1), anchor=tk.NW, image=img_tk)
    canvas.img_tk = img_tk  # Retine o referință la imagine pentru a o menține în viață


def afiseaza_campuri(campuri):
    # Creează un frame pentru a împacheta widget-urile specifice tipului de snap-hook
    campuri_frame = tk.Frame(root, bg="#BEB2A7", relief="groove", bd=3)
    campuri_frame.grid(row=4, column=0, pady=10, sticky=tk.W)

    # Salvează referința la variabilele care conțin valorile câmpurilor
    afiseaza_campuri.campuri_values = []

    # Adaugă campurile specifice tipului de snap-hook în frame
    for i, camp in enumerate(campuri):
        label = tk.Label(campuri_frame, text=camp, bg="#BEB2A7", font=("Arial", 10, "bold"))
        label.grid(row=i, column=0, sticky=tk.W)
        entry = tk.Entry(campuri_frame, width=20, font=("Arial", 10))
        entry.grid(row=i, column=1)
        afiseaza_campuri.campuri_values.append((label, entry))

    # Salvează referința la frame pentru a o utiliza ulterior pentru distrugere
    afiseaza_campuri.campuri_frame = campuri_frame


def convert_to_float(value):
    try:
        # Încercăm conversia directă
        return float(value)
    except ValueError:
        # În caz de eroare, încercăm să înlocuim ',' cu '.' și să repetăm conversia
        return float(value.replace(',', '.'))


def calculeaza():
    # Implementează aici logica de calcul folosind valorile din câmpurile generate

    # Preluarea valorilor
    valoare_material = afiseaza_campuri.campuri_values[0][1].get()
    e_flexural_modulus = convert_to_float(afiseaza_campuri.campuri_values[1][1].get())
    latime_b = convert_to_float(afiseaza_campuri.campuri_values[2][1].get())
    intaltime_h = convert_to_float(afiseaza_campuri.campuri_values[3][1].get())
    lungime_l = convert_to_float(afiseaza_campuri.campuri_values[4][1].get())
    unghi_alpha = convert_to_float(afiseaza_campuri.campuri_values[5][1].get())
    epsilon_strain = convert_to_float(afiseaza_campuri.campuri_values[6][1].get())
    valoare_miu = convert_to_float(afiseaza_campuri.campuri_values[7][1].get())
    valoare_q = convert_to_float(afiseaza_campuri.campuri_values[8][1].get())
    valoare_k = convert_to_float(afiseaza_campuri.campuri_values[9][1].get())
    valoare_a_big_base = convert_to_float(afiseaza_campuri.campuri_values[10][1].get())
    valoare_b_small_base = convert_to_float(afiseaza_campuri.campuri_values[11][1].get())
    valoare_l1_slot = convert_to_float(afiseaza_campuri.campuri_values[12][1].get())
    valoare_l2_support_1 = convert_to_float(afiseaza_campuri.campuri_values[13][1].get())
    valoare_l3_support_2 = convert_to_float(afiseaza_campuri.campuri_values[14][1].get())
    valoare_r1_inner_radius = convert_to_float(afiseaza_campuri.campuri_values[15][1].get())
    valoare_r2_outer_radius = convert_to_float(afiseaza_campuri.campuri_values[16][1].get())
    valoare_r_neutral_axis = convert_to_float(afiseaza_campuri.campuri_values[17][1].get())
    valoare_c_distance_outer_fiber = convert_to_float(afiseaza_campuri.campuri_values[18][1].get())
    valoare_i_inertia = convert_to_float(afiseaza_campuri.campuri_values[19][1].get())
    valoare_r_radius_at_base = convert_to_float(afiseaza_campuri.campuri_values[20][1].get())

    # Exemplu: preluarea valorilor
    for label, entry in afiseaza_campuri.campuri_values:
        valoare = entry.get()
        print(f"{label.cget('text')}: {valoare}")

    # Exemplu de afișare a unui rezultat
    rezultat = 0.67 * (epsilon_strain * lungime_l ** 2) / intaltime_h
    rezultat_label.config(text=f"Y = {rezultat}")
    print(rezultat_label)


# Creare fereastra principala


root = tk.Tk()
root.title("Snap-hook calculator \u00A9 PC")

root.geometry(f"{ROOT_HEIGHT}x{ROOT_WIDTH}")
root.configure(bg="#84CEEB")  # Setează culoarea de fundal a ferestrei

# Cadranul 1: Dropdown și butonul de afișare
optiuni = ["Selectează tipul de snap-hook"] + [snap_hook["nume"] for snap_hook in snap_hooks]
dropdown_var = tk.StringVar()
dropdown_var.set(optiuni[0])
dropdown = ttk.Combobox(root, values=optiuni, textvariable=dropdown_var, font=("Arial", 12), width=int(ROOT_WIDTH / 25))
dropdown.grid(row=0, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

afisare_button = tk.Button(root, text="Afișează informații", command=afiseaza_informatii, font=("Arial", 12),
                           width=int(ROOT_WIDTH / 25))
afisare_button.grid(row=1, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

# Cadranul 2: Canvas pentru imagine
canvas = tk.Canvas(root, width=158, height=155, bg="#BEB2A7", relief="groove")
canvas.grid(row=2, column=0, sticky=tk.W)

# Cadranul 3: Etichetă pentru afișare informații
afisare_label = tk.Label(root, text="", font=("Arial", 12), bg="#84CEEB")
afisare_label.grid(row=4, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

# Cadranul 4: Buton pentru calculare și etichetă pentru rezultat
calculeaza_button = tk.Button(root, text="Calculează", command=calculeaza, font=("Arial", 12), state=tk.DISABLED)
calculeaza_button.grid(row=1, column=1, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

rezultat_label = tk.Label(root, text="", font=("Arial", 12), bg="#84CEEB")
rezultat_label.grid(row=2, column=1, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

root.mainloop()
