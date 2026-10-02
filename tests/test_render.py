#!/usr/bin/env python3
"""The kit's own check: the example config validates, and one scene renders to a looping GIF.

Usage: python tests/test_render.py
Needs Playwright with Chromium. Uses ffmpeg when it is on PATH, otherwise Pillow.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    cfg = json.loads((ROOT / 'readme-scenes.json').read_text(encoding='utf-8'))
    sys.path.insert(0, str(ROOT / 'scripts'))
    import render
    assert render.problems(cfg) == [], render.problems(cfg)

    bad = {'scenes': [{'name': 'x', 'template': 'hero', 'gif': 'x.gif', 'alt': 'short', 'data': {}}]}
    found = render.problems(bad)
    assert any('alt' in p for p in found) and any('title' in p for p in found), found

    with tempfile.TemporaryDirectory() as d:
        scene = dict(cfg['scenes'][2])
        scene['gif'] = 'out.gif'
        scene['seconds'] = 3
        scene['fps'] = 6
        scene.pop('still', None)
        test_cfg = Path(d) / 'readme-scenes.json'
        test_cfg.write_text(json.dumps({'scenes': [scene]}), encoding='utf-8')
        subprocess.run([sys.executable, str(ROOT / 'scripts' / 'render.py'), '--config', str(test_cfg)], check=True)
        gif = Path(d) / 'out.gif'
        head = gif.read_bytes()[:6]
        assert head in (b'GIF89a', b'GIF87a'), head
        assert gif.stat().st_size > 10_000, gif.stat().st_size
        assert (Path(d) / 'readme-snippets.md').exists()
    print('OK: config valid, bad config caught, one scene rendered to a GIF.')


if __name__ == '__main__':
    main()
