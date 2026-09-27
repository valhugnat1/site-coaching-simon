#!/usr/bin/env python3
"""Mini-CI du site : vérifie que tout ce que les pages référencent existe.

Lancer en local :  python3 scripts/check.py
Lancé aussi automatiquement par GitHub Actions à chaque push / pull request.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
errors, warnings = [], []

pages = sorted(ROOT.glob("*.html"))
# Pages du site officiel, indexées par Google : règles SEO strictes
OFFICIELLES = {"index.html", "offres.html", "credit-impot.html", "resultats.html", "zone.html", "contact.html"}
if not (ROOT / "index.html").exists():
    errors.append("public/index.html manquant : Cloudflare Pages n'aurait pas de page d'accueil.")

for page in pages:
    html = page.read_text(encoding="utf-8")
    name = page.name

    # 1. Liens et images locaux qui pointent vers un fichier inexistant
    for attr, ref in re.findall(r'\b(src|href)="([^"]+)"', html):
        if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "//")):
            continue
        target = (page.parent / ref.split("#")[0].split("?")[0]).resolve()
        if not target.exists():
            errors.append(f"{name}: {attr}=\"{ref}\" ne pointe vers aucun fichier")

    # 2. Balises de base
    if "<title>" not in html:
        errors.append(f"{name}: pas de <title>")
    if 'name="viewport"' not in html:
        errors.append(f"{name}: pas de meta viewport (le site serait cassé sur mobile)")
    if "{{" in html and "}}" in html:
        errors.append(f"{name}: placeholder de template {{{{...}}}} oublié")

    # 3. Rappels (n'échouent pas la CI)
    if re.search(r"\bXXX? ?€", html):
        warnings.append(f"{name}: prix encore en placeholder (XX €)")
    if "contact@exemple.fr" in html:
        warnings.append(f"{name}: e-mail placeholder contact@exemple.fr")
    if "XX XX XX XX" in html:
        warnings.append(f"{name}: téléphone placeholder")
    if "[à compléter]" in html:
        warnings.append(f"{name}: n° de déclaration SAP à compléter (obligatoire pour le crédit d'impôt)")
    # 4. SEO des pages officielles
    if name in OFFICIELLES:
        if 'name="robots" content="noindex"' in html:
            errors.append(f"{name}: noindex sur une page officielle, Google ne l'indexera pas")
        if 'rel="canonical"' not in html:
            errors.append(f"{name}: pas de <link rel=\"canonical\">")
        if 'name="description"' not in html:
            errors.append(f"{name}: pas de meta description")
        if len(re.findall(r"<h1[ >]", html)) != 1:
            errors.append(f"{name}: il faut exactement un <h1>")
        m = re.search(r"<title>(.*?)</title>", html)
        if m and len(m.group(1)) > 70:
            warnings.append(f"{name}: <title> long ({len(m.group(1))} caractères, Google coupe vers 60-70)")
        for img in re.findall(r"<img\b[^>]*>", html):
            if 'alt="' not in img:
                errors.append(f"{name}: image sans texte alternatif : {img[:60]}")

# 5. Poids des images
for img in (ROOT / "img").glob("*"):
    kb = img.stat().st_size / 1024
    if kb > 500:
        warnings.append(f"img/{img.name}: {kb:.0f} Ko, pense à compresser (< 300 Ko idéalement)")

for w in warnings:
    print(f"⚠️  {w}")
for e in errors:
    print(f"❌ {e}")
print(f"\n{len(pages)} pages vérifiées · {len(errors)} erreur(s) · {len(warnings)} rappel(s)")
sys.exit(1 if errors else 0)
