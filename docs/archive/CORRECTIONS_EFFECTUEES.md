# Corrections des Références aux Notebooks

## Date: 2026-01-11

## Contexte
Suite à la réorganisation pédagogique du cours, les chapitres 11-14 ont été renumérés :
- **Chapitre 11** : Best Practices → **Séries Temporelles** (était ch 12)
- **Chapitre 12** : Séries Temporelles → **Vision Avancée** (était ch 13)
- **Chapitre 13** : Vision Avancée → **Systèmes de Recommandation** (était ch 14)
- **Chapitre 14** : Systèmes de Recommandation → **Best Practices** (était ch 11)

## Corrections Appliquées

### Chapitre 11 - Séries Temporelles (11_series_temporelles.tex)
✅ Corrections effectuées :
- `% Chapitre 12` → `% Chapitre 11`
- `pdftitle={Chapitre 12...}` → `pdftitle={Chapitre 11...}`
- `\fancyhead[L]{Chapitre 12...}` → `\fancyhead[L]{Chapitre 11...}`
- `{\LARGE Chapitre 12}` → `{\LARGE Chapitre 11}`
- `12_demo_*.ipynb` → `11_demo_*.ipynb`
- `12_exercices.ipynb` → `11_exercices.ipynb`

### Chapitre 12 - Vision Avancée (12_vision_avancee.tex)
✅ Corrections effectuées :
- `% Chapitre 13` → `% Chapitre 12`
- `pdftitle={Chapitre 13...}` → `pdftitle={Chapitre 12...}`
- `\fancyhead[L]{Chapitre 13...}` → `\fancyhead[L]{Chapitre 12...}`
- `{\LARGE Chapitre 13}` → `{\LARGE Chapitre 12}`
- `13_demo_*.ipynb` → `12_demo_*.ipynb`

### Chapitre 13 - Systèmes de Recommandation (13_systemes_recommandation.tex)
✅ Corrections effectuées :
- `% Chapitre 14` → `% Chapitre 13`
- `pdftitle={Chapitre 14...}` → `pdftitle={Chapitre 13...}`
- `\fancyhead[L]{Chapitre 14...}` → `\fancyhead[L]{Chapitre 13...}`
- `{\LARGE Chapitre 14}` → `{\LARGE Chapitre 13}`
- `14_demo_*.ipynb` → `13_demo_*.ipynb`
- `14_exercices.ipynb` → `13_exercices.ipynb`
- Prérequis : `Chapitre 11` → `Chapitre 14` (Best Practices)

### Chapitre 14 - Best Practices (14_best_practices.tex)
✅ Corrections effectuées :
- `pdftitle={Chapitre 11...}` → `pdftitle={Chapitre 14...}`
- `\fancyhead[L]{Chapitre 11...}` → `\fancyhead[L]{Chapitre 14...}`
- `{\LARGE Chapitre 11}` → `{\LARGE Chapitre 14}`
- `11_demo_pipeline.ipynb` → `14_demo_pipeline.ipynb`
- `11_demo_deployment.ipynb` → `14_demo_deployment.ipynb`
- `11_demo_monitoring.ipynb` → `14_demo_monitoring.ipynb`

## Résumé des Fichiers Modifiés

4 fichiers .tex modifiés :
1. `11_series_temporelles/11_series_temporelles.tex`
2. `12_vision_avancee/12_vision_avancee.tex`
3. `13_systemes_recommandation/13_systemes_recommandation.tex`
4. `14_best_practices/14_best_practices.tex`

## Vérification

Pour vérifier les corrections :
```bash
# Vérifier chapitre 11
grep -n "Chapitre 11\|11_demo_\|11_exercices" 11_series_temporelles/11_series_temporelles.tex

# Vérifier chapitre 12
grep -n "Chapitre 12\|12_demo_" 12_vision_avancee/12_vision_avancee.tex

# Vérifier chapitre 13
grep -n "Chapitre 13\|13_demo_\|13_exercices" 13_systemes_recommandation/13_systemes_recommandation.tex

# Vérifier chapitre 14
grep -n "Chapitre 14\|14_demo_" 14_best_practices/14_best_practices.tex
```

## Prochaines Étapes

Pour générer les PDFs mis à jour :
```bash
cd cours
bash compile_all_pdfs.sh
```

Ou via Docker :
```bash
docker exec ml-sandbox bash -c "cd /workspace/cours && bash compile_all_pdfs.sh"
```

## Status
✅ TOUTES LES CORRECTIONS EFFECTUÉES AVEC SUCCÈS
