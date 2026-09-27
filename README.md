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

## Version coaching à domicile

Cette branche expose directement le site « coaching à domicile » (plus de sélecteur de versions) :
accueil, crédit d'impôt, offres + calculateur, avant/après, zone (carte), contact.

Avant la mise en prod :
1. Les anciennes versions restent accessibles via `/menu` (`/gay` pour l'ex-Disco Gym)
2. Retirer `<meta name="robots" content="noindex">` des 6 pages
3. Remplacer les placeholders (prix provisoires, e-mail, téléphone, n° SAP)
4. Merge dans `main` → en ligne en ~30 s

Voir `CLAUDE.md` pour les règles d'édition.
# site-coaching-simon
