#!/usr/bin/env python3
"""Download and extract the Paddy Doctor dataset into datasets/paddydoctor/.

Two routes (see datasets/README.md for the full guide):

  1. Direct zip link (e.g. a variant zip from IEEE DataPort):
         python scripts/download_dataset.py --url <zip-url>

  2. Kaggle mirror of the dataset:
         pip install kaggle
         export KAGGLE_USERNAME=<your-kaggle-username>
         export KAGGLE_KEY=<your-kaggle-api-key>
         export PADDYDOCTOR_KAGGLE_DATASET=<owner/dataset-slug>
         python scripts/download_dataset.py --kaggle

Credentials are read from environment variables only. Nothing is
hardcoded, and the dataset itself is git-ignored — this script only
fetches it from its canonical sources.
"""

import argparse
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET = REPO_ROOT / "datasets" / "paddydoctor"
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}


def download_url(url: str, dest_zip: Path) -> None:
    print(f"Downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp, open(dest_zip, "wb") as fh:
        shutil.copyfileobj(resp, fh)
    print(f"Saved {dest_zip} ({dest_zip.stat().st_size / 1e6:.1f} MB)")


def download_kaggle(dest_dir: Path) -> None:
    slug = os.environ.get("PADDYDOCTOR_KAGGLE_DATASET")
    if not slug:
        sys.exit(
            "Set PADDYDOCTOR_KAGGLE_DATASET=<owner/dataset-slug> first "
            "(see datasets/README.md)."
        )
    if not (os.environ.get("KAGGLE_USERNAME") and os.environ.get("KAGGLE_KEY")):
        sys.exit(
            "Kaggle credentials missing: export KAGGLE_USERNAME and "
            "KAGGLE_KEY (from your Kaggle account settings). They are read "
            "from the environment only — never hardcode them."
        )
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        sys.exit("The kaggle package is not installed: pip install kaggle")
    api = KaggleApi()
    api.authenticate()
    print(f"Downloading Kaggle dataset {slug} ...")
    api.dataset_download_files(slug, path=str(dest_dir), unzip=True)


def extract(zip_path: Path, dest_dir: Path) -> None:
    print(f"Extracting {zip_path.name} into {dest_dir} ...")
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(dest_dir)


def report(root: Path) -> None:
    """Print every folder that directly contains images, with counts."""
    found = []
    for dirpath, _dirnames, filenames in os.walk(root):
        imgs = [f for f in filenames if Path(f).suffix.lower() in IMAGE_EXTS]
        if imgs:
            found.append((Path(dirpath), len(imgs)))
    if not found:
        print("No image folders found — check the archive layout against "
              "datasets/README.md.")
        return
    total = 0
    print("\nClass folders found:")
    for path, count in sorted(found):
        print(f"  {path.relative_to(root)}: {count} images")
        total += count
    print(f"Total: {total} images in {len(found)} folders")
    print("Expected: 16,225 images in 13 class folders (see "
          "datasets/README.md).")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="Direct link to a dataset zip file")
    group.add_argument("--kaggle", action="store_true",
                       help="Download via the Kaggle API (env credentials)")
    args = parser.parse_args()

    TARGET.mkdir(parents=True, exist_ok=True)

    if args.url:
        zip_path = TARGET / "paddydoctor.zip"
        download_url(args.url, zip_path)
        extract(zip_path, TARGET)
        zip_path.unlink()
    else:
        download_kaggle(TARGET)

    report(TARGET)


if __name__ == "__main__":
    main()
