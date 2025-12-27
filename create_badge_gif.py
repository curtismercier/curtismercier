#!/usr/bin/env python3
"""Generate a high-quality animated badge GIF for Multi-Agent Orchestration status."""

from PIL import Image, ImageDraw, ImageFont
import os
import random

# 2x resolution for retina displays
SCALE = 2
BADGE_HEIGHT = 20 * SCALE
PADDING_X = 8 * SCALE
FONT_SIZE = 11 * SCALE
CORNER_RADIUS = 0  # Square corners

# Colors matching shields.io style
COLORS = {
    "planning": "#F59E0B",  # Amber
    "building": "#58A6FF",  # Blue
    "testing": "#8B5CF6",   # Purple
    "shipping": "#10B981",  # Green
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_font():
    """Get the best available system font."""
    font_paths = [
        "/System/Library/Fonts/SFNSText.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/SF-Pro-Text-Regular.otf",
        "/System/Library/Fonts/SF-Pro.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/LucidaGrande.ttc",
    ]
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, FONT_SIZE)
            except:
                continue
    return ImageFont.load_default()

def create_badge_frame(text, bg_color, width, font):
    """Create a single badge frame at 2x resolution."""
    img = Image.new('RGBA', (width, BADGE_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw rounded rectangle background
    rgb_color = hex_to_rgb(bg_color)
    draw.rounded_rectangle(
        [(0, 0), (width - 1, BADGE_HEIGHT - 1)],
        radius=CORNER_RADIUS,
        fill=rgb_color
    )

    # Calculate text position (left-aligned with padding)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_height = bbox[3] - bbox[1]
    x = PADDING_X  # Left-aligned
    y = (BADGE_HEIGHT - text_height) // 2 - (2 * SCALE)

    # Draw text in white
    draw.text((x, y), text, fill=(255, 255, 255), font=font)

    return img

def create_typing_frames(text, bg_color, width, font):
    """Create frames that type out text letter by letter with realistic timing."""
    frames = []

    # Type each character with slight variation
    for i in range(len(text) + 1):
        partial = text[:i]
        display = partial + "_" if i < len(text) else partial
        if not display:
            display = "_"
        frame = create_badge_frame(display, bg_color, width, font)
        # Vary typing speed: slower for first char, slight randomness
        base_delay = 80 if i == 0 else 55
        delay = base_delay + random.randint(-10, 20)
        frames.append((frame, max(30, delay)))

    # Brief pause after finishing typing (no cursor)
    frame = create_badge_frame(text, bg_color, width, font)
    frames.append((frame, 300))

    return frames

def create_working_dots(base_text, bg_color, width, font, cycles=8):
    """Create realistic 'working' dots animation - deliberate, not frantic."""
    frames = []

    for cycle in range(cycles):
        # Build up dots slowly: . → .. → ...
        for num_dots in range(1, 4):
            dots = "." * num_dots
            text = base_text + dots
            frame = create_badge_frame(text, bg_color, width, font)
            # Each dot holds for a moment - feels like "thinking"
            # Vary timing slightly per cycle for organic feel
            hold_time = 350 + random.randint(-50, 100)
            frames.append((frame, hold_time))

        # Hold on "..." a bit longer before resetting
        frames.append((create_badge_frame(base_text + "...", bg_color, width, font), 500 + random.randint(0, 200)))

    return frames

def create_hold_frames(text, bg_color, width, font, duration_ms=1500):
    """Hold on completed text."""
    frames = []
    frame = create_badge_frame(text, bg_color, width, font)
    # Single frame with the duration
    frames.append((frame, duration_ms))
    return frames

def main():
    random.seed(42)  # Reproducible "randomness"
    font = get_font()

    # Calculate max width needed (for "Shipping..." which is longest)
    test_img = Image.new('RGBA', (300, BADGE_HEIGHT))
    test_draw = ImageDraw.Draw(test_img)

    max_text = "Shipping..."
    bbox = test_draw.textbbox((0, 0), max_text, font=font)
    text_width = bbox[2] - bbox[0]
    badge_width = text_width + PADDING_X * 2

    print(f"Creating badge GIF at {badge_width}x{BADGE_HEIGHT}px (2x retina)")

    all_frames = []

    # Phase 1: Planning - type it out, hold, then show "working" dots
    print("  Creating Planning phase...")
    all_frames.extend(create_typing_frames("Planning", COLORS["planning"], badge_width, font))
    all_frames.extend(create_working_dots("Planning", COLORS["planning"], badge_width, font, cycles=3))
    all_frames.extend(create_hold_frames("Planning...", COLORS["planning"], badge_width, font, 800))

    # Phase 2: Building - the main work phase, longer dots cycling
    print("  Creating Building phase...")
    all_frames.extend(create_typing_frames("Building", COLORS["building"], badge_width, font))
    all_frames.extend(create_working_dots("Building", COLORS["building"], badge_width, font, cycles=12))
    all_frames.extend(create_hold_frames("Building...", COLORS["building"], badge_width, font, 600))

    # Phase 3: Testing - medium duration
    print("  Creating Testing phase...")
    all_frames.extend(create_typing_frames("Testing", COLORS["testing"], badge_width, font))
    all_frames.extend(create_working_dots("Testing", COLORS["testing"], badge_width, font, cycles=5))
    all_frames.extend(create_hold_frames("Testing...", COLORS["testing"], badge_width, font, 800))

    # Phase 4: Shipping - shorter, then done
    print("  Creating Shipping phase...")
    all_frames.extend(create_typing_frames("Shipping", COLORS["shipping"], badge_width, font))
    all_frames.extend(create_working_dots("Shipping", COLORS["shipping"], badge_width, font, cycles=2))
    all_frames.extend(create_hold_frames("Shipping...", COLORS["shipping"], badge_width, font, 2000))

    print(f"  Total frames: {len(all_frames)}")

    # Extract frames and durations
    frames = [f[0] for f in all_frames]
    durations = [f[1] for f in all_frames]

    # Calculate total duration
    total_ms = sum(durations)
    print(f"  Total duration: {total_ms/1000:.1f} seconds")

    # Save as animated GIF
    output_path = "/Users/user/Gravicity Projects/github-profile-readme/assets/status-orchestration.gif"
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

    # Report file size
    size = os.path.getsize(output_path)
    print(f"File size: {size / 1024:.1f} KB")

if __name__ == "__main__":
    main()
