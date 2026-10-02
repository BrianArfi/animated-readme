---
name: animated-readme
description: Write or rewrite a GitHub README so a visitor gets it in ten seconds, with animated GIFs rendered from HTML (hero, before and after, how it works) and alt text for each. Use when someone wants a better README, a README with GIFs or a demo, a project page that shows what the project does, or to re-render README animations after the copy changed.
---

# animated-readme

The loop: read the project, write the copy, fill the scenes in `readme-scenes.json`, render the
GIFs, assemble the README, and show it to the user before anything is committed or pushed.

`KIT` below means this folder (`.claude/skills/animated-readme/` in an installed project).

## Steps

1. **Read the project before writing a word.** The current README, `docs/`, the package or
   project file, the entry points, the CHANGELOG and the last releases. Write down three things:
   who uses it, what they do with it, and what is true today. A feature that is planned, half
   done or only on a branch is not "what it does".
2. **Write the copy** to `KIT/docs/writing-guide.md`. It sets the README order, the voice and
   the words to avoid. Draft the copy in the chat first and keep it short.
3. **Fill the scenes.** Copy `KIT/readme-scenes.json` to the project root and replace every
   `data` block with this project's copy. Three templates are available:
   - `hero` (1600 x 800): headline, subline, a terminal that types a prompt, a result card.
   - `before-after` (1200 x 680): up to six pain cards, a wipe, then a terminal and up to five outcomes.
   - `how-it-works` (1200 x 660): three or four steps left to right, then a loop line.
   Set the project's own colours in `theme`. Write the `alt` for every scene: what the GIF shows,
   in the order it happens, for someone who cannot see it.
4. **Render.** `python KIT/scripts/render.py --check`, then `python KIT/scripts/render.py`.
   Open the GIFs or the still PNGs and look at them. Fix overflowing text by shortening the copy,
   never by shrinking the template.
5. **Assemble the README** from `readme-snippets.md`, which holds the image line and alt text for
   each GIF. Keep install and usage sections that already work; move them below the story.
6. **Show the user** the README and the GIFs. Commit and push only after they approve.

## Tools

- `python KIT/scripts/render.py [--config PATH] [--only NAME] [--check]`: render every scene,
  write still PNGs where asked, warn over 4 MB, and write `readme-snippets.md`.
- `python KIT/scripts/record_html.py page.html out.gif --w W --h H --dur S`: record any animated
  HTML page you wrote yourself, with the same deterministic engine. `--still S` writes one PNG.
- `python KIT/tests/test_render.py`: the kit's own check.

## Rules

- **Every claim comes from the repo.** If the copy says it does something, point to the file,
  command or release that does it. A claim with no source is cut or flagged to the user.
- **Copy lives in `readme-scenes.json`, never in the templates.** Templates stay generic so the
  next render and the next project reuse them.
- **No em-dash, no hype words, no "unlock", "seamless", "supercharge", "revolutionize".**
  See the writing guide for the full list.
- **Every GIF has alt text** that describes what happens, not "demo" or "screenshot".
- **Illustrations say so.** A scene that shows a typical or sample situation carries a caption
  like "Illustration of a typical project README." Never present a drawing as a real screen.
- **Nothing is pushed without approval.** A README is public the moment it reaches the default branch.
