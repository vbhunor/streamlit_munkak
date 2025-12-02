import streamlit as st
import pandas as pd
import json 
st.title("Jelentkezés a 2026-os központi felvételire")

st.write("Üdvözlünk az űrlapunkon! Kérlek töltsd ki az összes mezőt!")

nev = st.text_input("A diák neve:")

eletkor = st.slider("A diák életkora:", min_value=0, max_value=18, step=1)

iskola = st.text_area("A diák iskolája:")

osztaly = st.text_input("A diák osztálya:")

lakhely = st.text_area("A diák lakcíme:")

jeloles = st.checkbox("SNI/BTMN?")


fajl = st.file_uploader("Kérjük töltse fel az orvosi szakvéleményt, ha az SNI/BTMN-t bejelölte")


kivalasztas = st.multiselect("Válassza ki milyen segítséget szeretne gyerekének:", ["Plusz időkérés", "Számológép használata", "Speciális világítás"]) 
if st.button("Küldés:"):
    adat = {
        "Mező":["Név", "Életkor", "Iskola", "Osztály", "Lakhely", "SNI/BTMN", "A gyermek előnyei"],
        "Érték":[nev, eletkor, iskola, osztaly, lakhely, "Igen" if jeloles else "Nem", kivalasztas]
    }
    df = pd.DataFrame(adat)
    st.subheader("Összegzés")
    st.table(df)
    st.success("✅ Az adatok elmentve a jelentkezes.json fájlba!")



with open("jelentkezes.json", "w", encoding="utf-8") as f:
        adat = {
        "Mező":["Név", "Életkor", "Iskola", "Osztály", "Lakhely", "SNI/BTMN", "A gyermek előnyei"],
        "Érték":[nev, eletkor, iskola, osztaly, lakhely, "Igen" if jeloles else "Nem", kivalasztas]
        }
        json.dump(adat, f, ensure_ascii=False, indent=4)


