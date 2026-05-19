# /ss Skill — Claude Code Integration

## Overview

`/ss` is a screenshot skill that lets you reference screenshots during AI coding sessions.

## Installation

1. Copy `ss.py` to a location in your PATH
2. Make it executable: `chmod +x ss.py`
3. Set screenshot folder: `export SCREENSHOT_FOLDER=~/Desktop`

## Usage

```
ss 5              # Show last 5 screenshots
ss --latest       # Show most recent screenshot
ss --path        # Show paths only
ss --folder ~/Screenshots  # Custom folder
ss --ask "what UI issue do you see?"  # With question
```

## Claude Code Usage

Add to your CLAUDE.md or session:

```
When user says /ss or asks about screenshots:
1. Run: ss.py --latest
2. Show the screenshot path
3. Offer to analyze it with vision
```

## For Vision Analysis

```
# To analyze screenshots with AI vision:
ss --latest --path
# Then use the path with your vision tool
```

## Environment Variables

- `SCREENSHOT_FOLDER` — Custom screenshot folder path

## Tech Stack

- Python 3
- Pillow (for image metadata)
- Works on macOS, Linux, Windows
