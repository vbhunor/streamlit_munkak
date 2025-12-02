import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('Szia!')
st.header("Kedvenc szín és gyümölcs választása")

# Radio button
szin = st.radio("Válassz egy színt:", ["Piros", "Kék", "Zöld"])

# Checkbox
elfogadom = st.checkbox("Elfogadom a feltételeket")

# Select / Dropdown
gyumolcs = st.selectbox("Válassz gyümölcsöt:", ["Alma", "Banán", "Cseresznye"])

# Text input
nev = st.text_input("Írd be a neved:")
lakcim = st.text_area("Lakcímed:")
lehetosegek = st.multiselect("Válassz kedvenc állatot:", ["Koala", "Kutya", "Hörcsög"])
beadás_idopont = st.date_input("Válaszd ki a munkád beadásának időpontját:")
kor = st.number_input("Írdd be az életkorodat", min_value=0, max_value=100, step=1)
fajl_feltoltes = st.file_uploader("Töltsd fel a fájlod")
# Button
if st.button("Küldés"):
    # Adatok táblázatba rendezése
    adat = {
        "Mező": ["Név", "Lakcím", "Kor", "Szín", "Állat", "Gyümölcs", "Feltételek elfogadva", "Beadási időpont"],
        "Érték": [nev, lakcim, kor, szin, lehetosegek, gyumolcs, "Igen" if elfogadom else "Nem", beadás_idopont]
    }
    df = pd.DataFrame(adat)

    st.subheader("📊 Összegzés táblázatban")
    st.table(df)

st.map()
st.title("Másodfokú függvény vizualizáció")

# Csúszkák a paraméterekhez
a = st.slider("A értéke", min_value=-20, max_value=20, value=1)
b = st.slider("B értéke", min_value=-20, max_value=20, value=0)
c = st.slider("C értéke", min_value=-20, max_value=20, value=0)

# Függvény értékek
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

# Diszkrimináns és gyökök
D = b**2 - 4*a*c
roots = []
if D >= 0 and a != 0:
    r1 = (-b + D**0.5) / (2*a)
    r2 = (-b - D**0.5) / (2*a)
    roots = [r1, r2]

# Ábra készítése
fig, ax = plt.subplots()
ax.plot(x, y, label=f"${a}x^2 + {b}x + {c}$", color="royalblue")
ax.axhline(0, color="gray", linestyle="--", linewidth=1)
ax.axvline(0, color="gray", linestyle="--", linewidth=1)

# Gyökök megjelenítése
for r in roots:
    ax.plot(r, 0, "ro")
    ax.annotate(f"{r:.2f}", (r, 0), xytext=(0, 10), textcoords="offset points", ha="center", color="red")

# Tengelyek és címkék
ax.set_xlabel("x értékek")
ax.set_ylabel("y értékek")
ax.set_title("Másodfokú függvény ábrázolása")
ax.legend()
ax.grid(True)

st.pyplot(fig)


st.latex(r"y = ax^2 + bx + c")


st.latex(r"bx + c")

x = np.linspace(-10, 10, 400)
y = b * x + c   # itt b a meredekség, c a tengelymetszet

# Megoldás (x tengely metszéspont)
solution = None
if b != 0:
    solution = -c / b
    st.write(f"📍 Megoldás: x = {solution:.2f}")

# Ábra
fig, ax = plt.subplots()
ax.plot(x, y, label=f"${b}x + {c}$", color="royalblue", linewidth=2)
ax.axhline(0, color="gray", linestyle="--", linewidth=1)
ax.axvline(0, color="gray", linestyle="--", linewidth=1)

# Megoldás jelölése a grafikonon
if solution is not None and -10 <= solution <= 10:
    ax.plot(solution, 0, "ro", markersize=8)
    ax.annotate(f"{solution:.2f}", (solution, 0),
                xytext=(0, 10), textcoords="offset points",
                ha="center", color="red")

# Tengelyek és címkék
ax.set_xlabel("x értékek")
ax.set_ylabel("y értékek")
ax.set_title("Elsőfokú függvény grafikon megoldással")
ax.legend()
ax.grid(True)

st.pyplot(fig)

#A két függvény ábrázolása közös koordináta-rendszerben
# x tartomány
x = np.linspace(-10, 10, 400)

# Másodfokú függvény
y_quad = a * x**2 + b * x + c
D = b**2 - 4*a*c
roots = []
if D >= 0 and a != 0:
    r1 = (-b + D**0.5) / (2*a)
    r2 = (-b - D**0.5) / (2*a)
    roots = [r1, r2]

# Elsőfokú függvény
y_lin = b * x + c
solution = None
if b != 0:
    solution = -c / b

# Ábra készítése
fig, ax = plt.subplots(figsize=(8,5))

# Másodfokú görbe
ax.plot(x, y_quad, label=f"${a}x^2 + {b}x + {c}$", color="royalblue")

# Elsőfokú egyenes
ax.plot(x, y_lin, label=f"${b}x + {c}$", color="darkorange")

# Tengelyek
ax.axhline(0, color="gray", linestyle="--", linewidth=1)
ax.axvline(0, color="gray", linestyle="--", linewidth=1)

# Gyökök jelölése (másodfokú)
for r in roots:
    ax.plot(r, 0, "ro")
    ax.annotate(f"{r:.2f}", (r, 0), xytext=(0, 10),
                textcoords="offset points", ha="center", color="red")

# Megoldás jelölése (elsőfokú)
if solution is not None and -10 <= solution <= 10:
    ax.plot(solution, 0, "go", markersize=8)
    ax.annotate(f"{solution:.2f}", (solution, 0),
                xytext=(0, -15), textcoords="offset points",
                ha="center", color="green")

# Címkék és rács
ax.set_xlabel("x értékek")
ax.set_ylabel("y értékek")
ax.set_title("Másodfokú és elsőfokú függvény közös ábrán")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# LaTeX képletek
st.latex(r"y = ax^2 + bx + c")
st.latex(r"y = bx + c")