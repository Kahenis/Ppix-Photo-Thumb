# PPix Photo-thumb

Application Windows pour **scanner** les bibliothèques photos d’un serveur Plex (NAS) et **forcer la génération** des miniatures manquantes.

Le serveur Plex (sur le NAS) calcule les vignettes. Ce PC envoie les ordres, affiche la jauge, et peut mettre en pause / arrêter.

<img width="1123" height="757" alt="capture-ecran" src="https://github.com/user-attachments/assets/0ab6a277-e9b1-43cd-964c-9d275d536afb" />

## Téléchargement

Release Windows : [`ppix-photo-thumb.exe`](https://github.com/Kahenis/Ppix-Photo-Thumb/releases)

Si Windows Defender bloque l’exe (faux positif fréquent avec PyInstaller non signé) : *Plus d’infos* → *Exécuter quand même*.

## Fonctions

- Connexion **PIN plex.tv** ou **URL + jeton**
- Bibliothèques photos, dossiers et sous-dossiers, clips inclus
- Compteurs : médias / miniatures manquantes
- Génération par dossier ou pour toute la lib
- Pause, reprise, arrêt
- Reset des thumbs **d’un dossier** (double confirmation, fichiers originaux intacts)
- Tests NAS prudent / agressif (confirmation avant d’appliquer)
- Option anti-veille pendant le travail

## Compilation

Aucune compilation n'est nécessaire. Le fichier .exe est directement fourni dans la release Windows.

## Licence

Usage personnel, pas de modification sans l'accord de l'auteur. Plex est une marque de Plex, Inc. Ce projet n’est pas affilié à Plex.
