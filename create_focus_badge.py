#!/usr/bin/env python3
"""Generate an animated 'current activity' badge with CLI-style status messages."""

from PIL import Image, ImageDraw, ImageFont
import os
import random

# 2x resolution for retina displays
SCALE = 2
BADGE_HEIGHT = 20 * SCALE
PADDING_X = 8 * SCALE
FONT_SIZE = 11 * SCALE
CORNER_RADIUS = 0  # Square corners

# Dark terminal-style background
BG_COLOR = "#1a1a2e"
TEXT_COLOR = "#58A6FF"  # Terminal blue

# CLI-style status messages
MESSAGES = [
    "$ orchestrate --waves 3",
    "[swarm] 8 active | 2 queued",
    "compacting... 2.5x density",
    "build #284 ✓ tests passing",
    "session compacted: 73% saved",
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_font():
    """Get a monospace font for terminal feel."""
    font_paths = [
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Monaco.ttf",
        "/Library/Fonts/JetBrainsMono-Regular.ttf",
        "/System/Library/Fonts/Courier.ttc",
    ]
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, FONT_SIZE)
            except:
                continue
    return ImageFont.load_default()

def create_frame(text, width, font, text_color=TEXT_COLOR):
    """Create a single frame with terminal styling."""
    img = Image.new('RGBA', (width, BADGE_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw background
    bg_rgb = hex_to_rgb(BG_COLOR)
    draw.rectangle([(0, 0), (width - 1, BADGE_HEIGHT - 1)], fill=bg_rgb)

    # Draw text (left-aligned)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_height = bbox[3] - bbox[1]
    x = PADDING_X
    y = (BADGE_HEIGHT - text_height) // 2 - (2 * SCALE)

    text_rgb = hex_to_rgb(text_color)
    draw.text((x, y), text, fill=text_rgb, font=font)

    return img

def create_typing_frames(text, width, font):
    """Type out CLI command with cursor."""
    frames = []

    # Blinking cursor at start
    for _ in range(3):
        frames.append((create_frame("_", width, font), 200))
        frames.append((create_frame(" ", width, font), 200))

    # Type each character
    for i in range(len(text) + 1):
        partial = text[:i]
        display = partial + "_" if i < len(text) else partial
        frame = create_frame(display, width, font)
        # Faster typing for CLI feel
        delay = 40 + random.randint(-10, 15)
        frames.append((frame, max(25, delay)))

    # Hold the result
    frame = create_frame(text, width, font)
    for _ in range(12):
        frames.append((frame, 250))

    return frames

def create_processing_frames(text, width, font, cycles=3):
    """Show processing with spinner or dots."""
    frames = []
    spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    for _ in range(cycles):
        for spinner in spinners:
            display = f"{spinner} {text}"
            frame = create_frame(display, width, font)
            frames.append((frame, 80))

    return frames

def main():
    random.seed(42)
    font = get_font()

    # Calculate max width
    test_img = Image.new('RGBA', (400, BADGE_HEIGHT))
    test_draw = ImageDraw.Draw(test_img)

    max_width = 0
    for msg in MESSAGES:
        # Account for spinner prefix
        test_text = f"⠋ {msg}"
        bbox = test_draw.textbbox((0, 0), test_text, font=font)
        text_width = bbox[2] - bbox[0]
        max_width = max(max_width, text_width)

    badge_width = max_width + PADDING_X * 2

    print(f"Creating focus badge at {badge_width}x{BADGE_HEIGHT}px (2x retina)")

    all_frames = []

    for i, message in enumerate(MESSAGES):
        print(f"  Creating '{message}'...")

        # Type out command/status
        all_frames.extend(create_typing_frames(message, badge_width, font))

        # Brief processing animation between messages
        if i < len(MESSAGES) - 1:
            all_frames.extend(create_processing_frames("", badge_width, font, cycles=2))

    # Extra hold on last message
    frame = create_frame(MESSAGES[-1], badge_width, font)
    for _ in range(8):
        all_frames.append((frame, 300))

    print(f"  Total frames: {len(all_frames)}")

    frames = [f[0] for f in all_frames]
    durations = [f[1] for f in all_frames]

    total_ms = sum(durations)
    print(f"  Total duration: {total_ms/1000:.1f} seconds")

    output_path = "/Users/user/Gravicity Projects/github-profile-readme/assets/status-focus.gif"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2
    )

    print(f"Saved to {output_path}")
    size = os.path.getsize(output_path)
    print(f"File size: {size / 1024:.1f} KB")

if __name__ == "__main__":
    main()
