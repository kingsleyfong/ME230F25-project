# ME230 Bollard Material Selection Video Project

This repository contains the full source code, assets, and documentation for the ME230 Fall 2025 group video project. The video is produced using Manim Community Edition to create 3Blue1Brown style animations, with scene generation assisted by Antigravity IDE. The project evaluates the commercial ANNT stainless steel bollard, performs comparative material analysis, and presents results through an animated engineering sequence.

---

## Project Overview

The purpose of this project is to investigate the material selection process for vehicle impact protection bollards. This includes:

- Introducing the real world problem and recent case studies involving vehicle ramming incidents.
- Presenting the commercial baseline product using the ANNT AISI 304 stainless steel bollard.
- Analyzing alternative materials using quantitative metrics such as density, cost, yield strength, and manufacturability.
- Demonstrating manufacturing steps, load cases, impact behavior, and failure modes.
- Summarizing findings through animated explanations.

The final deliverable is a 3Blue1Brown inspired engineering animation rendered using Manim.

---

## Repository Structure

ME230Proj/
│
├── context.md # Strict rules for Antigravity scene generation
│
├── src/
│ ├── scenes/ # All Manim scene files generated via Antigravity
│ │ ├── title_scene.py
│ │ ├── attack_sequence_scene.py
│ │ ├── bollard_intro_scene.py
│ │ ├── steel_manufacturing_scene.py
│ │ ├── annt_spec_scene.py
│ │ └── (future scenes)
│ │
│ ├── visuals/ # Optional shared drawing helpers
│ └── init.py
│
├── assets/
│ ├── images/
│ │ ├── attacks/ # Photos used for attack sequence
│ │ ├── annt_spec/ # JPEG exports of ANNT spec sheet
│ │ └── diagrams/ # Custom diagrams or blueprint elements
│ ├── audio/ # Music or VO tracks if needed
│ └── fonts/ # Segoe UI or other local fonts
│
└── media/ # Manim output directory (auto generated)

yaml
Copy code

---

## Development Workflow

### 1. Write scenes in Antigravity IDE  
Scene creation is driven by natural language prompts following the rules in `context.md`.

### 2. Antigravity generates full scene code  
The IDE outputs complete Manim `.py` scene files into `src/scenes/`.

### 3. Render scenes locally using Manim  
Example:

python -m manim -pqh src/scenes/title_scene.py TitleScene

yaml
Copy code

High quality mode renders at 1080p and 60 fps.

### 4. Iterate  
Adjust prompts, refine animations, re render until the visual meets quality expectations.

### 5. Version control  
Push new scenes, assets, and documentation to the GitHub repository.

---

## Rendering Scenes

Default high quality render:

python -m manim -pqh path/to/scene.py SceneName

css
Copy code

Force a specific resolution:

python -m manim -p -r 1920,1080 --fps 60 path/to/scene.py SceneName

yaml
Copy code

---

## Requirements and Dependencies

- Python 3.11 or 3.10  
- Manim Community Edition 0.19  
- FFmpeg for media export  
- Segoe UI font installed system wide or included in `assets/fonts`

Install Manim:

python -m pip install manim

yaml
Copy code

Install FFmpeg:

winget install ffmpeg

yaml
Copy code

---

## Asset Requirements

- All diagrams are vector based for consistency.
- All external images must be placed in `assets/images/`.
- Spec sheets must be exported as JPEG before use in scenes.
- No external network calls inside scenes.

---

## Using Antigravity With This Repository

1. Open this repository inside Antigravity IDE.  
2. Load `context.md` as the system prompt.  
3. Describe scenes using structured prompting.  
4. Antigravity writes valid Manim code reflecting the project style.  
5. Commit changes to GitHub.

This workflow ensures scene consistency across the entire video.

---

## Authors

ME230 Group Members  
- Adam Benaissa  
- Joseph Schuurman  
- Kingsley Fong

---

## License

Manim scene files are provided for educational use for ME230 course requirements.  
External images (news photos and manufacturer spec sheets) remain under their original copyright.  
Included under academic fair use for analysis and presentation.
