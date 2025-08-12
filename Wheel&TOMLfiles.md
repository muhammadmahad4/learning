---

## **pyproject.toml**

- **What is it?**  
  A *configuration file* for Python projects (especially Poetry, PEP-517/518).  
  It declares:
  - *Metadata* about your project (name, version, description, authors, ...)
  - Your dependencies (runtime & dev)
  - Build settings (backend, scripts, etc.)
- **Purpose:**  
  - Used by Poetry (`poetry install`, `poetry build`) or pip+build to **resolve and fetch dependencies**, lock them, and drive packaging.
  - **Source of truth** for project definition.

> **analogy**: Like a recipe or a manifest for building your package.

---

## **Wheel File (`.whl`)**

- **What is it?**  
  A *binary distribution archive* (a built package), with your code and (optionally) metadata;  
  Standardized format for Python (`.whl`).
- **Purpose:**  
  - Can be **installed with pip** (`pip install my_package.whl`)
  - Contains: your code (`.py`), resources (data, etc.), and metadata (your dependencies—but not their code, just a list)
  - **You generate the wheel** by running `poetry build` or `python -m build`
- **What’s in it:**  
  - Everything needed for other users/systems to install and run your code (except your dependencies’ code, which pip fetches when installing the wheel).

> **analogy**: Like a baked cake from the recipe; ready to eat/use.

---

## **How They Work Together**

- **You write/edit `pyproject.toml` by hand** to describe your package and dependencies.
- **Poetry uses that TOML file** to build a `.whl` wheel file (plus a `tar.gz` if you want).
- *Your end users/CI/containers install the wheel* with pip.  
  (They usually never need to see your `pyproject.toml` at all.)

---

## **Quick Comparison Table**

| File               | Type           | Role                               | Created by       | Used by         |
|--------------------|----------------|------------------------------------|------------------|-----------------|
| `pyproject.toml`   | Source config  | Project metadata & dependencies    | **You**          | Poetry, build   |
| `.whl` (wheel)     | Built artifact | Installable binary package         | `poetry build`   | pip, runtime    |

---

**Bottom line:**  
- `pyproject.toml` is **the recipe** (source and config).
- `.whl` is **the cake** (finished, installable build)!

