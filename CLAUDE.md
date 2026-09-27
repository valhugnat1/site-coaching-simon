# Site de Simon Hoffmann — coach sportif à Strasbourg

Site vitrine statique (HTML/CSS/JS à la main, **aucun framework, aucune étape de build**).
Hébergé sur Cloudflare Pages, déployé automatiquement depuis ce repo GitHub.

## Structure

- `public/` : **tout ce qui est en ligne**. Cloudflare Pages publie ce dossier tel quel.
  - Site **coaching à domicile** (design « brut » adapté, fond clair + orange) — un menu relie les pages :
    - `index.html` : accueil
    - `credit-impot.html` : explication du crédit d'impôt 50 % (services à la personne)
    - `offres.html` : 3 formules (Essentiel / Suivi / Intégral) + calculateur d'abonnement
    - `resultats.html` : avant / après + témoignage de Martin
    - `zone.html` : carte Leaflet (OpenStreetMap) avec la zone desservie + vérificateur de commune
    - `contact.html` : formulaire (ouvre un e-mail pré-rempli, pas de serveur)
  - `menu.html` (URL `/menu`) : l'ancien sélecteur, qui liste toutes les versions (officielle + anciennes)
  - `brut.html`, `editorial.html`, `pop.html` : anciennes versions pro ; `gay.html` (URL `/gay`, ex-`disco`) et `calculateur.html` : versions humoristiques. Accessibles seulement via `/menu`
  - `img/` : photos (portrait de Simon, avant/après de Simon, Martin, Théo)
  - `_headers` : en-têtes HTTP Cloudflare
- `scripts/check.py` : mini-CI (liens, images, balises, placeholders)
- `.github/workflows/check.yml` : lance `check.py` à chaque push / PR

## Règles pour modifier le site

- Chaque page est **un seul fichier HTML autonome** : CSS dans `<style>`, JS dans `<script>`, en bas de page. Pas de fichier CSS/JS partagé.
  Le menu, le pied de page et le CSS de base sont donc copiés dans chaque page : une modif de menu/couleur se fait dans **les 6 pages**.
- Tarifs : dans les cartes de `offres.html`, `index.html` (aperçu), `contact.html` (liste déroulante) **et** l'objet `TARIFS` du calculateur (`offres.html`). Rayon de la zone : `R1` / `R2` dans `zone.html`.
- Crédit d'impôt : ne rien promettre de plus que la loi (50 %, séances à domicile uniquement, coach déclaré SAP, plafond 12 000 €).
- Les couleurs sont des variables CSS dans `:root` en haut de chaque page : change-les là.
- Les images vont dans `public/img/`, référencées en relatif (`img/nom.jpg`). Compresser avant d'ajouter (JPEG qualité ~85, < 300 Ko).
- Le site doit rester **impeccable sur mobile (390 px de large)** : pas de scroll horizontal, gouttière de 16 px.
- Langue : français, tutoiement, ton direct et motivant.
- Le témoignage de Martin est réel : **ne pas le modifier ni inventer d'autres témoignages**.
- Les résultats avant/après (chiffres) sont réels : ne pas les changer sans qu'on te donne les nouveaux.
- Après chaque modif : lancer `python3 scripts/check.py` et corriger les erreurs (❌). Les ⚠️ sont des rappels.

## Placeholders encore à remplacer

- Prix des offres : **provisoires** (55 / 65 / 75 € la séance, duo +20 €, remises 5/10/15 %, +10 € de 20 à 30 km), à valider par Simon
- N° de déclaration SAP (`[à compléter]` dans le pied de page)
- E-mail `contact@exemple.fr` → vrai e-mail
- Téléphone `06 XX XX XX XX`
- Balise `<meta name="robots" content="noindex">` : à retirer de la version choisie au lancement

## Déploiement

- Push sur une branche ≠ `main` → **preview** automatique sur `<branche>.simon-coaching.pages.dev`
- Merge dans `main` → **production** sur simonhoffmann.fr
- Rien d'autre à faire : pas de build, pas de commande de déploiement.
