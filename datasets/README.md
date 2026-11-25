# Dataset — Paddy Doctor (PaddyDoctor)

The classifier is trained on the **Paddy Doctor** dataset. The images are
**not** stored in this repository (16,225 images do not belong in git —
`datasets/` is git-ignored); this page is the guide to getting them from
the canonical source.

## What the implemented paper states

Singh et al. (2026), "Data and code availability":

> "This paper utilizes the publicly available Paddy Doctor dataset [16]."

Reference [16] is the dataset paper:

> Petchiammal, A., Briskline Kiruba, S., Murugan, D., & Pandarasamy, A.
> (2023). "Paddy Doctor: A Visual Image Dataset for Automated Paddy Disease
> Classification and Benchmarking." *Proceedings of the 6th Joint
> International Conference on Data Science & Management of Data
> (CODS-COMAD 2023)*, pp. 1–5.
> DOI: [10.1145/3570991.3570994](https://doi.org/10.1145/3570991.3570994)

## Facts

- **Images:** 16,225 field photographs of rice leaves (RGB, original
  resolution 1080 × 1440)
- **Classes:** 13 — 12 diseases/pests and Healthy:

  1. Bacterial Leaf Blight
  2. Bacterial Leaf Streak
  3. Bacterial Panicle Blight
  4. Black Stem Borer
  5. Blast
  6. Brown Spot
  7. Downy Mildew
  8. Hispa
  9. Leaf Roller
  10. Tungro
  11. White Stem Borer
  12. Yellow Stem Borer
  13. Healthy

  (Singh et al. canonicalise the dataset's "Normal" label to "Healthy".)

## Canonical sources

- **Project website:** https://paddydoc.github.io — the dataset authors'
  own page; links the releases below.
- **IEEE DataPort:** https://ieee-dataport.org/documents/paddy-doctor-visual-image-dataset-automated-paddy-disease-classification-and-benchmarking
  (dataset DOI: 10.21227/hz4v-af08) — hosts the full dataset in four
  variants: original (~4.7 GB, 1080×1440), medium (~1.24 GB, 480×640),
  small (~323 MB, 256×256), and small-split (~323 MB, pre-split
  train/test).
- **Kaggle competition subset:** https://www.kaggle.com/c/paddy-disease-classification/
  — 10,407 annotated images from the same corpus.

## Licence

The dataset was released open-source by its authors for research use; the
terms of use are stated on the IEEE DataPort page above. We link to the
source rather than redistributing the images — nothing under `datasets/`
is committed to this repository.

## Expected local layout

After downloading and extracting a variant, arrange it as one folder per
class under `datasets/paddydoctor/`:

```
datasets/
└── paddydoctor/
    ├── Bacterial Leaf Blight/
    │   ├── IMG_....jpg
    │   └── ...
    ├── Bacterial Leaf Streak/
    ├── Bacterial Panicle Blight/
    ├── Black Stem Borer/
    ├── Blast/
    ├── Brown Spot/
    ├── Downy Mildew/
    ├── Hispa/
    ├── Leaf Roller/
    ├── Tungro/
    ├── White Stem Borer/
    ├── Yellow Stem Borer/
    └── Healthy/
```

## Download instructions

**Option A — manual (IEEE DataPort, no tooling):**

1. Open the IEEE DataPort page above (a free IEEE account may be required
   to download).
2. Download a variant zip — `paddy-doctor-diseases-small.zip` (256×256) is
   enough for training on a free Colab GPU; take the original only if you
   need full resolution.
3. Extract it so the class folders land in `datasets/paddydoctor/` as in
   the layout above.

**Option B — script (direct zip link):**

```bash
python scripts/download_dataset.py --url <zip-url>
```

Downloads the zip, extracts it into `datasets/paddydoctor/`, and prints
the class folders it finds, with image counts.

**Option C — script (Kaggle mirror):**

If you use a Kaggle mirror of the dataset, Kaggle credentials are read
from the environment — never hardcode them and never commit them:

```bash
pip install kaggle
export KAGGLE_USERNAME=<your-kaggle-username>
export KAGGLE_KEY=<your-kaggle-api-key>
export PADDYDOCTOR_KAGGLE_DATASET=<owner/dataset-slug>
python scripts/download_dataset.py --kaggle
```

## Notes for our reproduction

Singh et al. do **not** use the raw corpus as-is: they build a
leakage-resistant split with perceptual-hash de-duplication, fit the
calibration (temperature scaling) on a separate calibration split, and
persist split indices, the random seed, and checksums. Our data pipeline
(see `brain/`) follows the same protocol — a plain random split will not
reproduce their numbers.
