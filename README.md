# simon-site

Site vitrine de **Simon Hoffmann**, coach sportif diplômé d'État à Strasbourg.
HTML statique, hébergé sur Cloudflare Pages, déploiement automatique à chaque push.

## En bref

| Action | Résultat |
| --- | --- |
| Push / PR sur une branche | Preview : `https://<branche>.site-coaching-simon.pages.dev` |
| Merge dans `main` | Production : https://simonhoffmann.fr |
| Chaque push / PR | GitHub Actions lance `scripts/check.py` |

## Tester en local

```bash
python3 -m http.server 8000 --directory public   # puis http://localhost:8000
python3 scripts/check.py                          # vérif liens / images / placeholders
```

## Site officiel

Site coaching à domicile (6 pages : accueil, tarifs, crédit d'impôt, résultats, zone, contact), indexé par Google.
Les anciennes versions restent accessibles via `/menu` (`/gay` pour l'ex-Disco Gym), en `noindex`.

Voir `CLAUDE.md` pour les règles d'édition.
# site-coaching-simon
