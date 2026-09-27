# Site de Simon Hoffmann — coach sportif à Strasbourg

Site vitrine statique (HTML/CSS/JS à la main, **aucun framework, aucune étape de build**).
Hébergé sur Cloudflare Pages, déployé automatiquement depuis ce repo GitHub.

## Structure

- `public/` : **tout ce qui est en ligne**. Cloudflare Pages publie ce dossier tel quel.
  - Site **coaching à domicile** (design doux : crème + vert sauge, titres Fraunces, cible adultes 35-65 ans) — un menu relie les pages :
    - `index.html` : accueil
    - `credit-impot.html` : explication du crédit d'impôt 50 % (services à la personne)
    - `offres.html` : les 3 vraies offres (séance 70 €, hybride 170 €/mois, distance 140 €/mois), packs −5/−10/−15 %, calculateur
    - `resultats.html` : avant / après + témoignage de Martin
    - `zone.html` : carte Leaflet (OpenStreetMap) avec la zone desservie + vérificateur de commune
    - `contact.html` : formulaire (ouvre un e-mail pré-rempli, pas de serveur)
  - `menu.html` (URL `/menu`) : l'ancien sélecteur, qui liste toutes les versions (officielle + anciennes)
  - `brut.html`, `editorial.html`, `pop.html` : anciennes versions pro ; `gay.html` (URL `/gay`, ex-`disco`) et `calculateur.html` : versions humoristiques. Accessibles seulement via `/menu`
  - `img/` : photos (portrait de Simon, avant/après de Simon, Martin, Théo)
  - `_headers` : en-têtes HTTP Cloudflare
  - `sitemap.xml`, `robots.txt`, `favicon.svg`, `404.html` : SEO et confort
- `scripts/check.py` : mini-CI (liens, images, balises, placeholders)
- `.github/workflows/check.yml` : lance `check.py` à chaque push / PR

## Règles pour modifier le site

- Chaque page est **un seul fichier HTML autonome** : CSS dans `<style>`, JS dans `<script>`, en bas de page. Pas de fichier CSS/JS partagé.
  Le menu, le pied de page et le CSS de base sont donc copiés dans chaque page : une modif de menu/couleur se fait dans **les 6 pages**.
- Tarifs (réels, donnés par Simon) : cartes + tableau des packs + `PRIX`/`PACKS` du calculateur dans `offres.html`, aperçu dans `index.html`, liste déroulante de `contact.html`, et JSON-LD (`makesOffer`, `priceRange`) dans `index.html`.
- Rayon de la zone : `R1` / `R2` dans `zone.html`.
- Ton : doux, rassurant, lisible. Peu de texte, pas de majuscules criardes. Cible : adultes 35-65 ans, remise en forme.
- Crédit d'impôt : ne rien promettre de plus que la loi (50 %, séances à domicile uniquement, coach déclaré SAP, plafond 12 000 €). Le suivi à distance n'y ouvre **pas** droit.

## SEO (pages officielles)

- Chaque page officielle a : `<title>` et meta description uniques, `<link rel="canonical">` vers `https://simonhoffmann.fr/...`, Open Graph, un seul `<h1>`, des `alt` sur toutes les images. `check.py` le vérifie (❌ sinon).
- Données structurées JSON-LD : `LocalBusiness` sur l'accueil, `FAQPage` sur le crédit d'impôt, fil d'Ariane ailleurs.
- Nouvelle page officielle → l'ajouter à `OFFICIELLES` dans `check.py` et à `sitemap.xml`.
- Les anciennes versions et `/menu` gardent `noindex`.
- Les couleurs sont des variables CSS dans `:root` en haut de chaque page : change-les là.
- Les images vont dans `public/img/`, référencées en relatif (`img/nom.jpg`). Compresser avant d'ajouter (JPEG qualité ~85, < 300 Ko).
- Le site doit rester **impeccable sur mobile (390 px de large)** : pas de scroll horizontal, gouttière de 16 px.
- Langue : français, tutoiement, ton direct et motivant.
- Le témoignage de Martin est réel : **ne pas le modifier ni inventer d'autres témoignages**.
- Les résultats avant/après (chiffres) sont réels : ne pas les changer sans qu'on te donne les nouveaux.
- Après chaque modif : lancer `python3 scripts/check.py` et corriger les erreurs (❌). Les ⚠️ sont des rappels.

## Coordonnées (réelles)

- Téléphone : 06 71 00 53 00 · E-mail : simon.hoffmann5757@gmail.com · Instagram : @simonhoffmann.coaching

## À vérifier

- Simon doit être **déclaré services à la personne** (SAP) pour que le crédit d'impôt s'applique : sinon, retirer les mentions du crédit d'impôt.

## Déploiement

- Push sur une branche ≠ `main` → **preview** automatique sur `<branche>.site-coaching-simon.pages.dev`
- Merge dans `main` → **production** sur simonhoffmann.fr
- Rien d'autre à faire : pas de build, pas de commande de déploiement.
