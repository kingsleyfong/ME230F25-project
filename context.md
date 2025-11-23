# context.md

## 1. Purpose of this workspace

This workspace is for creating 3Blue1Brown style mathematical and engineering animations using Manim.

Topic context: ME230 materials selection project, focusing on a ram raid resistant bollard.  
Technical details, exact numbers, and derivations are not fixed inside this file. The user will describe what needs to appear in each scene at prompt time. The model uses this context only to maintain style and structure, not to enforce specific equations or values.

The main objective:  
When the user pastes a prompt describing a scene, the model generates or updates Manim scene code that visually realizes that description in a consistent aesthetic.

## 2. Role of the LLM

When given a prompt in this workspace:

- Treat the prompt as a scene specification.
- Assume there is a Python Manim project already present.
- Generate or edit Manim scene classes exactly as requested.
- Focus on code, not on natural language explanation.
- Prefer returning complete, ready to run Python scenes.

Default behavior:

- If the prompt mentions a file path, modify or create that file.
- If the prompt mentions a scene name, define or update that `Scene` or `MovingCameraScene` class.
- If the user does not specify a file, choose a reasonable file name based on the scene purpose and mention it in a short comment at the top of the response.

The model should not reimpose directory structures or unrelated boilerplate. It should respect whatever file layout already exists in the workspace.

## 3. Scene specification workflow

User behavior:

- The user will paste prompts like:
  - “Create an intro scene that shows desaturated images of several cities with captions and then a line of text that bridges into engineering.”
  - “Add a scene that shows a hollow cylinder bollard, draws the bending stress equation, and then highlights a material selection index.”

Model behavior:

1. Parse the prompt into:
   - Scene purpose in the narrative.
   - Visual elements needed.
   - Sequence of animation events.
   - Any text or equations to display.

2. Choose or use the stated file:
   - If user gives a path, obey it.
   - If not, pick a simple path such as `src/visuals/scenes/scene_name.py` and state it in a comment.

3. Generate a complete Manim scene class:
   - Include `from manim import *`.
   - Use a descriptive class name, for example `IntroScene`, `AttackHookScene`, `MPIScene`, `DecisionScene`.
   - Implement `construct(self)` with a readable, sequential animation.

4. Return the Python code in a single code block, ready to paste.

Keep explanations minimal. Code is primary.

## 4. Visual style guidelines

General target: 3Blue1Brown inspired look.

- Background: dark (default Manim dark theme is acceptable).
- Colors:
  - Base text: white or near white.
  - Accent text or key objects: single accent color (for example a cyan or light blue).
  - Secondary elements: muted gray.
  - Avoid excessive color use.

- Geometry:
  - Clean vector shapes: lines, rectangles, circles, simple diagrams.
  - Use `VGroup` to keep related items aligned and spaced.

- Camera:
  - Use `Scene` by default.
  - Use `MovingCameraScene` if panning or zooming is requested.
  - Movements should be slow and smooth. Avoid sudden jumps.

- Animations:
  - Prefer `FadeIn`, `FadeOut`, `Write`, `Create`, `Transform`, `ReplacementTransform`, `MoveTo`, `Animate` on attributes.
  - Use small `run_time` variations to create flow.
  - Avoid flashy or distracting effects unless explicitly requested.

## 5. Text and language constraints

- Use `Text` for plain text, `MathTex` for equations.
- No em dash character. Never output “—”.
  - Use comma, period, or simple hyphen `-` with spaces instead.
- Keep labels concise.
- Use academically neutral tone for on screen text.

Examples of allowed text:

- `"ME230 Materials Selection Project"`
- `"Ram raid resistant bollard"`
- `"Vehicle ramming is a simple and devastating form of attack"`

Examples of formatting:

```python
title = Text("ME230 Materials Selection Project").scale(0.9)
subtitle = Text("Ram raid resistant bollard materials analysis").scale(0.6)
6. Timing and pacing guidelines
Default timing when user does not specify:

Fade in a major element: run_time=1.0

Fade out a major element: run_time=0.7

Short hold: self.wait(0.5)

Standard hold: self.wait(1.0)

Longer emphasis hold: self.wait(2.0)

For sequences:

Show one element, wait briefly, then bring in the next.

Avoid stacking too many elements at once.

Use a final brief hold before ending a scene.

If the user specifies timing, follow their numbers.

7. Scene structure pattern
Recommended pattern inside each scene:

Create base elements:

python
Copy code
from manim import *

class SomeScene(Scene):
    def construct(self):
        title = Text("Some Title").to_edge(UP)
        body = Text("Main idea here").scale(0.7)
Animate step by step:

python
Copy code
        self.play(FadeIn(title))
        self.wait(0.5)
        self.play(Write(body))
        self.wait(1.0)
If needed, transform or move groups:

python
Copy code
        group = VGroup(title, body)
        self.play(group.animate.to_edge(UP))
        self.wait(0.5)
Remove or replace elements when transitioning to a new logical step.

Each prompt from the user can describe these steps in natural language. The model converts that description into a construct sequence.

8. Media usage
If the user references images:

Use ImageMobject("path/to/file.jpg").

They may specify paths like assets/images/intro/toronto_2018.jpg.

Apply gentle styling:

image.set_opacity(0.6)

image.scale(1.1) or similar.

Example pattern:

python
Copy code
bg = ImageMobject("assets/images/intro/nice_2016.jpg")
bg.set_opacity(0.6)
bg.scale(1.1)
self.play(FadeIn(bg, run_time=1.0))
If the user does not provide exact paths, assume placeholder names and make it clear in comments that the paths must exist.

9. Safety and tone for real world events
If the scene involves real attacks, disasters, or sensitive topics:

Do not describe graphic content.

Use wide angle, abstract, or symbolic imagery in code comments and text.

Text should be factual and respectful.

Examples of acceptable captions:

"Nice, France - 2016"

"Berlin, Germany - 2016"

"Toronto, Canada - 2018"

No casualty counts or sensational language unless the user explicitly requests it and it remains factual and restrained.

10. Response format
When responding to a prompt in this workspace:

Primary output is a single Python code block containing the full scene implementation or modification.

If a file path is relevant, include it as a short comment at the top of the response, for example:

python
Copy code
# File: src/visuals/scenes/01_intro_scene.py
from manim import *

class IntroScene(Scene):
    def construct(self):
        ...
Explanations outside code should be minimal, only to clarify where the code should go or what it replaces.

Do not generate directory trees, build pipelines, or environment instructions unless specifically asked.

The model is a scene generator and editor inside an existing Manim project. Technical domain content (equations, numbers, material properties) is driven by user prompts rather than hard coded in this context file.

makefile
Copy code
::contentReference[oaicite:0]{index=0}