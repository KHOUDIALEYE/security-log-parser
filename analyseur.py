compteur_alertes = 0
total_lignes = 0

print("=== ANALYSEUR DE LOGS DYNAMIQUE ===")

mot_cle = input("Entrez le mot-clé à rechercher (ex: ERROR, WARNING, INFO) : ").strip()

print(f"\n--- Recherche des occurrences de '{mot_cle}' ---")

try:
  with open("serveur.log", "r") as fichier_source, open("rapport_alertes.txt", "w") as fichier_rapport:
    fichier_rapport.write(f"=== RAPPORT D'ANALYSE POUR : {mot_cle} ===\n\n")
    for ligne in fichier_source:
        total_lignes += 1
        if mot_cle in ligne:
            print("Alerte détectée :", ligne.strip())
            fichier_rapport.write(ligne)
            compteur_alertes += 1
        else:
            pass

  print("---------------------------------------")
  print(f"Analyse terminée.")
  print(f"Lignes totales analysées : {total_lignes}")  # <--- NOUVEAU : affichage du total
  print(f"Alerte(s) sauvegardée(s) : {compteur_alertes}")
except FileNotFoundError:
    
    print("\n[ERREUR] Le fichier 'serveur.log' est introuvable dans le dossier.")
    print("Veuillez vérifier son nom ou le replacer ici avant de relancer le script.")