#!/usr/bin/env python3
"""
/ss — Screenshot Skill for AI Coding Tools
==========================================
Reads screenshots from a folder and displays them with metadata.
Can be used as a Claude Code / Codex skill.
"""

import os
import sys
import glob
import argparse
from pathlib import Path
from datetime import datetime
from PIL import Image

# Default screenshot folders by OS
DEFAULT_PATHS = {
    "darwin": "~/Desktop",
    "linux": "~/Pictures/Screenshots",
    "windows": "%USERPROFILE%\\Pictures\\Screenshots"
}

def get_screenshot_folder():
    """Get the configured screenshot folder."""
    custom = os.environ.get("SCREENSHOT_FOLDER")
    if custom:
        return os.path.expanduser(custom)
    
    import platform
    system = platform.system().lower()
    if system in DEFAULT_PATHS:
        return os.path.expanduser(DEFAULT_PATHS[system])
    
    return os.path.expanduser("~/Desktop")

def get_screenshots(folder, limit=5, extension="*.png"):
    """Get N most recent screenshots from folder."""
    search_path = os.path.join(os.path.expanduser(folder), extension)
    files = glob.glob(search_path)
    
    # Also check for .jpg
    if extension == "*.png":
        jpg_path = os.path.join(os.path.expanduser(folder), "*.jpg")
        files.extend(glob.glob(jpg_path))
    
    # Sort by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    
    return files[:limit]

def display_screenshot(path):
    """Display screenshot info and open it."""
    stat = os.stat(path)
    size_kb = stat.st_size / 1024
    
    try:
        with Image.open(path) as img:
            width, height = img.size
            mode = img.mode
    except Exception:
        width, height, mode = "?", "?", "?"
    
    return {
        "path": path,
        "size_kb": round(size_kb, 1),
        "dimensions": f"{width}x{height}",
        "mode": mode,
        "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    parser = argparse.ArgumentParser(description="/ss — Screenshot Skill")
    parser.add_argument("count", nargs="?", type=int, default=5, 
                        help="Number of screenshots to show (default: 5)")
    parser.add_argument("--folder", "-f", type=str, default=None,
                        help="Screenshot folder (default: auto-detect)")
    parser.add_argument("--latest", "-l", action="store_true",
                        help="Show only the latest screenshot")
    parser.add_argument("--ask", "-a", type=str, default=None,
                        help="Ask a question about the screenshots")
    parser.add_argument("--path", "-p", action="store_true",
                        help="Show full paths only")
    
    args = parser.parse_args()
    
    folder = args.folder or get_screenshot_folder()
    
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        print(f"Set SCREENSHOT_FOLDER env var or use --folder")
        sys.exit(1)
    
    limit = 1 if args.latest else args.count
    screenshots = get_screenshots(folder, limit)
    
    if not screenshots:
        print(f"No screenshots found in: {folder}")
        print(f"Supported formats: .png, .jpg")
        sys.exit(0)
    
    print(f"\n📸 Found {len(screenshots)} screenshot(s) in {folder}\n")
    
    for i, ss_path in enumerate(screenshots, 1):
        info = display_screenshot(ss_path)
        if args.path:
            print(f"{i}. {info['path']}")
        else:
            print(f"{i}. {os.path.basename(ss_path)}")
            print(f"   Size: {info['size_kb']} KB | {info['dimensions']} | {info['mode']}")
            print(f"   Modified: {info['modified']}")
            print(f"   Path: {info['path']}")
            print()
    
    if args.ask:
        print(f"\n💬 Question: {args.ask}")
        print("(Connect to Claude/Codex to analyze these screenshots)")
    
    return screenshots

if __name__ == "__main__":
    main()
