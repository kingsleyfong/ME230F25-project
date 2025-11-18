# ME230 Term Project Database

Repository for managing data, analysis scripts, and visuals for the **ME230 Removable Anti Ram Bollard** term project.  
This repository is the central source of truth for materials data, calculations, plots, and video assets.

---

## Project Goals

- Maintain a clean and structured materials and design database.  
- Allow all analysis to be reproducible using Python.  
- Store code for MPI derivations, heat treatment analysis, corrosion checks, and durability comparisons.  
- Store assets for the final video presentation.

---

## Tech Stack

**Languages and Tools**  
- Python 3  
- SQLite (optional)  
- Jupyter notebooks (optional)

**Python Libraries**  
- pandas  
- numpy  
- matplotlib or plotly  
- sqlalchemy  
- manim (optional for animations)

---

## Repository Structure

```
.
├─ data/
│  ├─ raw/                 # Original, unmodified data
│  ├─ processed/           # Cleaned and structured CSV files
│  └─ db/                  # SQLite database files
│
├─ src/
│  ├─ db/                  # Database setup and query scripts
│  ├─ analysis/            # MPI, deflection, yield, corrosion analysis
│  └─ visuals/             # Manim animation scripts and figures
│
├─ notebooks/              # Optional Jupyter notebooks
├─ docs/                   # Generated plots, tables, and supporting files
├─ tests/                  # Simple tests for core analysis functions
├─ requirements.txt        # Python dependencies
└─ README.md               # Project overview
```

---

## Getting Started

### 1. Clone the repository

```
git clone https://github.com/<username>/<repo>.git
cd <repo>
```

### 2. Create a virtual environment

```
python -m venv .venv
```

Activate it:

Windows:

```
.venv\Scripts\activate
```

macOS and Linux:

```
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Data Workflow

### Data Sources

- ME230 Lab 2 aluminum data  
- CES Granta material exports  
- Supplier data sheets  
- Askeland and Callister textbook tables  

### Steps

1. Place all raw files in `data/raw/`.  
2. Use scripts in `src/analysis/` to clean and preprocess data.  
3. Save cleaned files to `data/processed/`.  
4. Optionally load processed data into a SQLite database in `data/db/`.

---

## Analysis Scripts

This project includes analysis for:

- Material Performance Index (MPI) derivations  
- Bending, deflection, and yield checks  
- Corrosion susceptibility and environmental durability  
- Heat treatment suitability for aluminum and steel  
- ASTM crash rating related metrics  

Example command:

```
python src/analysis/run_all.py
```

All outputs (plots, tables, figures) should be stored in the `docs/` folder.

---

## Visuals and Animations

If using **Manim** for 3Blue1Brown style animations, store scenes in:

```
src/visuals/
```

Example render command:

```
manim -pqh 01_intro_scene.py IntroScene
```

Rendered animations can be used in the final Bongo video submission.

---

## Collaboration Guidelines

### Branching Strategy

- `main` is the stable branch  
- Create feature branches such as:  
  - `feature/db-schema`  
  - `feature/materials-cleaning`  
  - `feature/mpi-calcs`  
  - `feature/visuals`  

### Commit Messages

Use short and descriptive messages. Examples:

- Add materials database schema  
- Implement bending based MPI  
- Generate aluminum vs steel comparison plots  

### Pull Requests

- Open a PR into `main`  
- Request review from group members  
- Merge once approved  

---

## References

- ME230 Course Outline  
- ME230 Project Topic 7 Bollard description  
- ASTM F2656 crash rating documentation  
- Askeland, Science and Engineering of Materials  
- Ashby, Materials Selection in Mechanical Design  
- Callister, Materials Science and Engineering  

---

## To Do List

- [ ] Finalize repository structure  
- [ ] Add dependencies to requirements.txt  
- [ ] Implement database schema  
- [ ] Import and clean Lab 2 aluminum data  
- [ ] Implement MPI analysis  
- [ ] Generate all plots and diagrams  
- [ ] Build Manim animations  
- [ ] Prepare all outputs for final video submission  

---
