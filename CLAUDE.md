# Site de Simon Hoffmann — coach sportif à Strasbourg

Site vitrine statique (HTML/CSS/JS à la main, **aucun framework, aucune étape de build**).
Hébergé sur Cloudflare Pages, déployé automatiquement depuis ce repo GitHub.

## Structure

- `public/` : **tout ce qui est en ligne**. Cloudflare Pages publie ce dossier tel quel.
  - `index.html` : page d'accueil (pour l'instant, le sélecteur de versions)
  - `brut.html`, `editorial.html`, `pop.html` : les 3 versions pro du site
  - `disco.html`, `calculateur.html` : versions humoristiques (pas pour la prod)
  - `img/` : photos (portrait de Simon, avant/après de Simon, Martin, Théo)
  - `_headers` : en-têtes HTTP Cloudflare
- `scripts/check.py` : mini-CI (liens, images, balises, placeholders)
- `.github/workflows/check.yml` : lance `check.py` à chaque push / PR

## Règles pour modifier le site

- Chaque page est **un seul fichier HTML autonome** : CSS dans `<style>`, JS dans `<script>`, en bas de page. Pas de fichier CSS/JS partagé.
- Les couleurs sont des variables CSS dans `:root` en haut de chaque page : change-les là.
- Les images vont dans `public/img/`, référencées en relatif (`img/nom.jpg`). Compresser avant d'ajouter (JPEG qualité ~85, < 300 Ko).
- Le site doit rester **impeccable sur mobile (390 px de large)** : pas de scroll horizontal, gouttière de 16 px.
- Langue : français, tutoiement, ton direct et motivant.
- Le témoignage de Martin est réel : **ne pas le modifier ni inventer d'autres témoignages**.
- Les résultats avant/après (chiffres) sont réels : ne pas les changer sans qu'on te donne les nouveaux.
- Après chaque modif : lancer `python3 scripts/check.py` et corriger les erreurs (❌). Les ⚠️ sont des rappels.

## Placeholders encore à remplacer

- Prix des offres (`XX €`, `XXX €`)
- E-mail `contact@exemple.fr` → vrai e-mail
- Téléphone `06 XX XX XX XX`
- Balise `<meta name="robots" content="noindex">` : à retirer de la version choisie au lancement

## Déploiement

- Push sur une branche ≠ `main` → **preview** automatique sur `<branche>.simon-coaching.pages.dev`
- Merge dans `main` → **production** sur simonhoffmann.fr
- Rien d'autre à faire : pas de build, pas de commande de déploiement.
