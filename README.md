# ML Learning Workspace

This repository contains my machine learning and Python learning practice files. The current focus is NumPy basics using Jupyter notebooks.

## Contents

- `numpy/phase1.ipynb` - NumPy array creation, NumPy arrays vs Python lists, arrays from scratch, vectors, matrices, and tensors.
- `numpy/phase2.ipynb` - NumPy array operations, sorting, filtering, masks, fancy indexing, and `np.where()`.
- `numpy/phase4.ipynb` - Continued NumPy practice and examples.
- `numpy/arr1.npy`, `numpy/arr2.npy`, `numpy/arr3.npy` - Saved NumPy array files used during practice.
- `numpy/img.jpeg` - Image file used in notebook examples.

## Setup

Create and activate a virtual environment, then install the required packages:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install common notebook dependencies:

```bash
pip install numpy jupyter matplotlib
```

## Usage

Start Jupyter Notebook from the project folder:

```bash
jupyter notebook
```

Then open the notebooks inside the `numpy` folder.

## Notes

Virtual environments are intentionally ignored by Git. Recreate them locally using the setup steps above instead of uploading them to GitHub.
