# PPix Photo-thumb

Application Windows pour **scanner** les bibliothèques photos d’un serveur Plex (NAS) et **forcer la génération** des miniatures manquantes.

Le serveur Plex (sur le NAS) calcule les vignettes. Ce PC envoie les ordres, affiche la jauge, et peut mettre en pause / arrêter.

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

```bat
python -m pip install -r requirements.txt
python make_icon.py
python -m PyInstaller --noconfirm --clean ppix-photo-thumb.spec
```

Le dossier `src_obf/` contient le **source obfusqué** (bytecode).  
`main.py` et `ppix_boot.py` chargent l’application.

## Licence

Usage personnel. Plex est une marque de Plex, Inc. Ce projet n’est pas affilié à Plex.
