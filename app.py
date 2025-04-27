import streamlit as st
import google.generativeai as genai

# Config API
genai.configure(api_key="AIzaSyDCImv-he2rtE4QNK3JONzr-gaoPjGSxu8")

# Charger modèle
model = genai.GenerativeModel('gemini-2.0-flash')

# Configuration page
st.set_page_config(page_title="Générateur d'Histoires IA", page_icon="📖")

# Choix langue
lang = st.selectbox("Choisis ta langue / Choose your language :", ("Français", "English"))

# Début du formulaire
with st.form(key="story_form"):
    if lang == "Français":
        st.title("📖 Générateur d'Histoires Courtes avec Gemini 2.0 Flash")
        st.write("Donne quelques mots-clés, et laisse l'IA inventer une histoire magique ! ✨")
        keywords = st.text_input("Entre des mots-clés séparés par des virgules (ex: pirate, trésor, tempête)")
        submit_button = st.form_submit_button("Générer l'histoire")
        spinner_message = "Génération de ton histoire..."
        warning_message = "Merci d'entrer au moins un mot-clé avant de générer l'histoire."
        error_message = "Une erreur est survenue :"
        result_title = "Ton histoire ✨ :"
        prompt_template = "Écris une courte histoire amusante et créative utilisant les mots suivants : {keywords}."
    else:
        st.title("📖 Short Story Generator with Gemini 2.0 Flash")
        st.write("Give a few keywords and let the AI create a magical story! ✨")
        keywords = st.text_input("Enter keywords separated by commas (e.g., pirate, treasure, storm)")
        submit_button = st.form_submit_button("Generate Story")
        spinner_message = "Generating your story..."
        warning_message = "Please enter at least one keyword before generating the story."
        error_message = "An error occurred:"
        result_title = "Your story ✨ :"
        prompt_template = "Write a short, funny, and creative story using the following words: {keywords}."

# Génération après submit
if submit_button:
    if keywords:
        prompt = prompt_template.format(keywords=keywords)
        with st.spinner(spinner_message):
            try:
                response = model.generate_content(prompt)
                st.subheader(result_title)
                st.write(response.text)
            except Exception as e:
                st.error(f"{error_message} {e}")
    else:
        st.warning(warning_message)
