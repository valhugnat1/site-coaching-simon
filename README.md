# simon-site

Site vitrine de **Simon Hoffmann**, coach sportif diplômé d'État à Strasbourg.
HTML statique, hébergé sur Cloudflare Pages, déploiement automatique à chaque push.

## En bref

| Action | Résultat |
| --- | --- |
| Push / PR sur une branche | Preview : `https://<branche>.simon-coaching.pages.dev` |
| Merge dans `main` | Production : https://simonhoffmann.fr |
| Chaque push / PR | GitHub Actions lance `scripts/check.py` |

## Tester en local

```bash
python3 -m http.server 8000 --directory public   # puis http://localhost:8000
python3 scripts/check.py                          # vérif liens / images / placeholders
```

## Choisir la version finale

1. `git mv public/editorial.html public/index.html` (remplace `editorial` par la version choisie ; supprime l'ancien `index.html` avant)
2. Supprimer les autres versions, dont `disco.html` et `calculateur.html`
3. Retirer `<meta name="robots" content="noindex">` de `index.html`
4. Remplacer les placeholders (prix, e-mail, téléphone)
5. Commit + push sur `main` → en ligne en ~30 s

Voir `CLAUDE.md` pour les règles d'édition.
