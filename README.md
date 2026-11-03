# 🪔 Diwali Diya in Python (turtle)

A glowing Diwali diya drawn live with Python's built-in `turtle` module: a clay diya with gold zigzag and dot patterns, a flickering 3-layer flame, rangoli dots, sparkles and a "Happy Diwali" greeting.

Day 8 of my **100 Days Daily Reel Challenge** by [@hack.n.code](https://www.instagram.com/hack.n.code/).

![screenshot](screenshot.png)

## How to run

1. Install Python 3 (turtle comes with it, no `pip install` needed).
2. Download `diya.py`.
3. Run:

```bash
python diya.py
```

A window opens, the turtle draws the diya (about 8 to 10 seconds), then the flame starts flickering, the rangoli and sparkles appear and "Happy Diwali" is written on top. Close the window to stop.

**Font tip:** the greeting uses the free Google font [Pacifico](https://fonts.google.com/specimen/Pacifico). Install it for the same look, or change `"Pacifico"` in `greet()` to any font you have.

On Linux, if you get `No module named tkinter`, install it with `sudo apt install python3-tk`.

## How it works

- `bowl()` makes the half-ellipse points of the clay diya; `shape()` fills any list of points.
- The glow is 40 dots, from big and dark to small and bright.
- `draw_flame()` builds a teardrop from a sine curve, in 3 layers (orange, yellow, white).
- `animate()` runs every 60 ms with `ontimer`: it clears the flame and redraws it with a random height, width and sway, so it flickers.

Happy Diwali 🪔✨
