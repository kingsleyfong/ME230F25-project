# ME230 Bollard Material Selection Video Project

This repository contains the full source code, assets, and documentation for the ME230 Fall 2025 group video project. The video is produced using Manim Community Edition to create 3Blue1Brown-style animations, with scene generation assisted by Antigravity IDE. The project evaluates the commercial ANNT stainless steel bollard, performs comparative material analysis, and presents results through an animated engineering video.

---

## Project Overview

The purpose of this project is to investigate the material selection process for vehicle impact protection bollards. This includes:

- Introducing the real world problem and recent case studies involving vehicle ramming incidents.
- Presenting the commercial baseline product using the ANNT AISI 304 stainless steel bollard.
- Analyzing alternative materials using quantitative metrics such as density, cost, yield strength, and manufacturability.
- Demonstrating manufacturing steps, load cases, impact behavior, and failure modes.
- Summarizing findings through animated explanations.

The final deliverable is a 3Blue1Brown-style video containing all scenes rendered using Manim.

---

## Repository Structure

ME230Proj/
│
├── context.md # Strict project-wide rules for Antigravity scene generation
│
├── src/
│ ├── scenes/ # All Manim scene files generated through Antigravity
│ │ ├── title_scene.py
│ │ ├── attack_sequence_scene.py
│ │ ├── bollard_intro_scene.py
│ │ ├── steel_manufacturing_scene.py
│ │ ├── annt_spec_scene.py
│ │ └── (future scenes)
│ │
│ ├── visuals/ # Optional shared helper classes or drawing utilities
│ └── init.py
│
├── assets/
│ ├── images/
│ │ ├── attacks/ # Images used for vehicle attack sequence
│ │ ├── annt_spec/ # JPEG exports of ANNT spec sheet
│ │ └── diagrams/ # Custom diagrams or blueprint shapes
│ ├── audio/ # Music or VO tracks if required
│ └── fonts/ # Segoe UI if manually embedded
│
└── media/ # Manim output folder (generated automatically)

yaml
Copy code

---

## Development Workflow

### 1. Write and structure scenes in Antigravity IDE
Scene generation is prompted using natural language following the strict formatting rules defined in `context.md`.

### 2. Antigravity produces a complete Manim scene file
The IDE writes the scene into `src/scenes/`.

### 3. Render scenes locally using Manim
All scenes are rendered individually. Example:

python -m manim -pqh src/scenes/title_scene.py TitleScene

yaml
Copy code

High quality mode uses 1080p at 60 fps.

### 4. Inspect and revise scenes
Adjust prompts to change layout, motion, or text. Re-render until final.

### 5. Version control through GitHub
Regularly push updated scene files, assets, and documentation.

---

## Rendering Scenes

Every scene can be rendered using:

python -m manim -pqh path/to/scene.py SceneName

css
Copy code

To force a specific resolution:

python -m manim -p -r 1920,1080 --fps 60 path/to/scene.py SceneName

yaml
Copy code

---

## Dependencies

This project uses:

- Python 3.11 or 3.10
- Manim Community Edition 0.19
- FFmpeg (required for video export)
- Segoe UI font (installed system-wide or provided inside `assets/fonts`)

Install Manim using:

python -m pip install manim

arduino
Copy code

If FFmpeg is not available:

winget install ffmpeg

yaml
Copy code

---

## Asset Requirements

To maintain the visual consistency of the video:

- All diagrammatic elements are vector based.
- All photos must be placed in `assets/images/`.
- All spec sheet pages must be exported as JPEG.
- No external network calls occur inside scene files.

---

## Using Antigravity With This Repository

1. Open the project folder inside Antigravity IDE.
2. Load `context.md` into the system prompt.
3. Describe new scenes using structured prompts.
4. Antigravity generates validated Manim code that follows all style rules.
5. Place generated files into `src/scenes/`.

This ensures consistency across all scenes.

---

## Authors

ME230 Group Members  
- Adam Benaissa  
- Joseph Schuurman  
- Kingsley Fong  

---

## License

All Manim scene files and custom animations are released for educational use within the course. External images such as news photos or manufacturer spec sheets remain under their original copyright and are included for academic fair use only.
