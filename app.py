import random
import string
import streamlit as st

st.set_page_config(page_title="NajiPass", page_icon="🔐", layout="centered")

st.title("🔐 NajiPass")
st.subheader("Générateur de mots de passe sécurisés")

length = st.slider("Longueur du mot de passe", min_value=6, max_value=32, value=12)

use_letters = st.checkbox("Inclure des lettres", value=True)
use_numbers = st.checkbox("Inclure des chiffres", value=True)
use_symbols = st.checkbox("Inclure des symboles", value=True)

if st.button("Générer le mot de passe"):
  if not (use_letters or use_numbers or use_symbols):
    st.warning(
        "Sélectionne au moins une option pour générer un mot de passe !"
    )
  else:
    characters = ""
    if use_letters:
      characters += string.ascii_letters
    if use_numbers:
      characters += string.digits
    if use_symbols:
      characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    st.success("Voici ton mot de passe :")
    st.code(password, language="")
