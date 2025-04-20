
import pandas as pd

def charger_catalogue(fichier_excel):
    try:
        return pd.read_excel(fichier_excel)
    except Exception as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        return None

def rechercher_article(df, mot_cle):
    resultats = df[df["Nom d'article"].str.contains(mot_cle, case=False, na=False)]
    if resultats.empty:
        print("Aucun article trouvé pour ce mot-clé.")
    else:
        print("\nRésultats trouvés :")
        print(resultats.to_string(index=False))

def main():
    chemin_fichier = "catalogue_articles_final.xlsx"
    catalogue = charger_catalogue(chemin_fichier)
    if catalogue is None:
        return

    while True:
        mot_cle = input("\nEntrez le nom ou une partie du nom de l'article à rechercher (ou 'exit' pour quitter) : ")
        if mot_cle.lower() == 'exit':
            break
        rechercher_article(catalogue, mot_cle)

if __name__ == "__main__":
    main()
