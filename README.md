ME230 Term Project Database

Repository for managing data, analysis scripts, and visuals for the ME230 Removable Anti Ram Bollard term project.
This repo is the central source of truth for materials data, calculations, plots, and video assets.

Project Goals

Maintain a clean materials and design database.

Make analysis reproducible with Python.

Store all code related to MPI, heat treatment, corrosion, and durability analysis.

Store assets for the final video presentation.

Tech Stack

Languages and Tools

Python 3

SQLite (optional)

Jupyter notebooks (optional)

Python Libraries

pandas

numpy

matplotlib or plotly

sqlalchemy

manim (optional for animations)

Repository Structure
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
├─ docs/                   # Generated plots, tables, supporting files
├─ tests/                  # Unit tests for core analysis functions
├─ requirements.txt        # Python dependencies
└─ README.md               # Project overview

Getting Started
1. Clone the repository
git clone https://github.com/<username>/<repo>.git
cd <repo>

2. Create a virtual environment
python -m venv .venv


Activate it:

Windows:

.venv\Scripts\activate


macOS and Linux:

source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

Data Workflow
Data Sources

Lab 2 aluminum tensile data

CES Granta exports

Supplier material sheets

Textbook property tables

Steps

Place raw files in data/raw/.

Process with scripts in src/analysis/.

Store cleaned CSVs in data/processed/.

Optionally load into SQLite (data/db/).

Analysis Scripts

Includes:

MPI derivation and ranking

Bending, yield, and deflection calculations

Corrosion susceptibility table

Heat treatment suitability

ASTM crash rating mechanical checks

Example command:

python src/analysis/run_all.py


Outputs are stored in docs/.

Visuals and Animations

For 3Blue1Brown style animations:

Scenes stored in src/visuals/

Render example:

manim -pqh 01_intro_scene.py IntroScene

Collaboration Guidelines
Branching

main for stable code

feature branches such as:

feature/db-schema

feature/mpi-calcs

feature/visuals

Commit messages

Examples:

Add materials database schema

Implement bending based MPI

Generate comparison plot for aluminum vs steel

Pull Requests

Open PR into main

Request review from group mates

Merge after approval

References

ME230 Course Outline

ME230 Topic 7 Bollard Description

ASTM F2656 crash rating details

Askeland (Science and Engineering of Materials)

Ashby (Materials Selection in Mechanical Design)

Callister (Materials Science and Engineering)

To Do List

 Finalize repo structure

 Add Python dependencies

 Implement database schema

 Import and clean Lab 2 aluminum data

 Implement all MPI calculations

 Generate plots and diagrams

 Build Manim animations for video

 Prepare outputs for Bongo submission
