import streamlit as st
import os
import base64

# Définir le code secret global
CODE_SECRET_ATTENDU = "1234"

def main():
    st.title("Escape Game - Plateforme de Partage de Fichiers et Codes Secrets")

    # Centrer les boutons et les styliser
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
        }
        .yellow-button {
            background-color: transparent;
            color: #FFD700;
            border: 2px solid #FFD700;
            width: 200px;
            text-align: center;
            padding: 10px;
            border-radius: 5px;
            margin: 10px;
        }
        .purple-button {
            background-color: transparent;
            color: #800080;
            border: 2px solid #800080;
            width: 200px;
            text-align: center;
            padding: 10px;
            border-radius: 5px;
            margin: 10px;
        }
        .error-textbox {
            color: white;
            background-color: #FF6347;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        .success-textbox {
            color: white;
            background-color: #32CD32;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Bouton "Télécharger Fichiers" (jaune)
    st.markdown("<div class='centered'><button class='yellow-button' onclick='downloadFiles()'>Télécharger Fichiers</button></div>", unsafe_allow_html=True)

    # Bouton "Tester mon code" (violet)
    st.markdown("<div class='centered'><button class='purple-button' onclick='testCode()'>Tester mon code</button></div>", unsafe_allow_html=True)

    # Zone pour le résultat du test de code
    result_area = st.empty()

    # Script JavaScript pour les boutons
    st.markdown(
        """
        <script>
        function downloadFiles() {
            // Mettez ici le code pour le bouton "Télécharger Fichiers"
            alert("Fonctionnalité de téléchargement à implémenter !");
        }

        function testCode() {
            // Mettez ici le code pour le bouton "Tester mon code"
            const code = prompt("Entrez le code secret :");
            if (code === '1234') {
                // Afficher le message de réussite
                document.getElementById('result_area').innerHTML = "<div class='success-textbox'>Vous avez réussi ! 🎉👏</div>";
            } else {
                // Afficher le message d'erreur
                document.getElementById('result_area').innerHTML = "<div class='error-textbox'>Code incorrect. Veuillez réessayer.</div>";
            }
        }
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
































################## OLD ##################


######pip install streamlit-aggrid
#####
#####
######## Packages
######import altair as alt
######import numpy as np
######import pandas as pd
######import streamlit as st
######from PIL import Image
######from st_aggrid import AgGrid
#####
#####
####### Test ChatGPT
#####
#####import streamlit as st
#####import matplotlib.pyplot as plt
#####import numpy as np
#####
#####def main():
#####    # Définir le fond de l'application en gris foncé
#####    st.markdown(
#####        """
#####        <style>
#####            .stApp {
#####                background-color: #1B1E37;
#####            }
#####        </style>
#####        """,
#####        unsafe_allow_html=True
#####    )
#####
#####    # Titre de l'application
#####    st.title("Comparaison des résultats des équipes")
#####    
#####
#####    # Données des équipes
#####    equipes = [
#####        {'Nom': 'Équipe A', 'Résultat (%)': 20},
#####        {'Nom': 'Équipe B', 'Résultat (%)': 10},
#####    ]
#####
#####    # Trier les équipes en fonction du résultat
#####    equipes_triees = sorted(equipes, key=lambda x: x['Résultat (%)'], reverse=True)
#####
#####    # Affichage des équipes dans Streamlit
#####    for equipe in equipes_triees:
#####        afficher_equipe(equipe)
#####
#####def afficher_equipe(equipe):
#####    # Créer un dégradé de couleur en fonction du résultat
#####    couleur_hex = generer_couleur_degrade(equipe['Résultat (%)'])
#####
#####    # Stylisation du texte avec fond de couleur en dégradé
#####    resultat_stylise = f"<span style='background: linear-gradient(to right, #1B1E37 0%, {couleur_hex} 100%); color: white; font-weight: bold;'>{equipe['Résultat (%)']}%</span>"
#####    st.write(f"**{equipe['Nom']}** - Résultat : {resultat_stylise}", unsafe_allow_html=True)
#####
#####def generer_couleur_degrade(percentage):
#####    # Générer une couleur en dégradé en fonction du pourcentage
#####    cmap = plt.cm.RdYlBu  # Choisissez la colormap que vous préférez
#####    norm = plt.Normalize(0, 100)
#####    couleur_rgb = cmap(norm(percentage))
#####
#####    # Convertir la couleur RGB en format hexadécimal
#####    couleur_hex = "#{:02x}{:02x}{:02x}".format(
#####        int(couleur_rgb[0] * 255),
#####        int(couleur_rgb[1] * 255),
#####        int(couleur_rgb[2] * 255)
#####    )
#####
#####    return couleur_hex
#####
#####if __name__ == "__main__":
#####    main()
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
#####
####### test 2
#####
######## Images
######img = ["Images/mario.png", "Images/luigi.png"]
######
######for i in range(len(img)):
######    st.image(img[i])
######
#####
####### test 1
#####
######## Set-Up Streamlit
################ Set the tab name
######st.set_page_config(
######    page_title="Contest",
######    page_icon="🧿",
######
######)
######
######
################# Set the page title
######st.title("Live Results")
######
################# Build the app
######df = pd.DataFrame(
######    {
######        "Team name": ["Roadmap", "Extras"],
######        "Score": [1,2],
######        "Logo":["Images/mario.png", "Images/luigi.png"]
######    }
######)
######
######AgGrid(df)
#####
#####