#!/usr/bin/env python3
"""
Generate responsive card images from cards.json configuration.

Usage:
    python generate_cards.py          # Generate all cards
    python generate_cards.py void     # Generate specific card by id
"""

import json
import os
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

# 2x resolution for retina
SCALE = 2

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_font(size, bold=False):
    """Get system font at specified size."""
    if bold:
        font_paths = [
            "/System/Library/Fonts/SFNS.ttf",
            "/System/Library/Fonts/SFNSText-Bold.otf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]
    else:
        font_paths = [
            "/System/Library/Fonts/SFNS.ttf",
            "/System/Library/Fonts/SFNSText.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]

    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size * SCALE)
            except:
                continue
    return ImageFont.load_default()

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def draw_status_badge(draw, text, color, x, y, font):
    """Draw a status badge at position."""
    padding_x = 8 * SCALE
    padding_y = 4 * SCALE

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    badge_width = text_width + padding_x * 2
    badge_height = text_height + padding_y * 2

    # Draw badge background
    draw.rectangle(
        [(x, y), (x + badge_width, y + badge_height)],
        fill=hex_to_rgb(color)
    )

    # Draw text
    draw.text(
        (x + padding_x, y + padding_y - 2 * SCALE),
        text,
        fill=(255, 255, 255),
        font=font
    )

    return badge_width, badge_height

def create_static_card(card, theme):
    """Create a static PNG card."""
    width = theme['card_width'] * SCALE
    padding = theme['card_padding'] * SCALE

    # Fonts
    font_icon = get_font(18)
    font_title = get_font(16, bold=True)
    font_body = get_font(12)
    font_tagline = get_font(12, bold=True)
    font_badge = get_font(10)

    # Calculate content height
    test_img = Image.new('RGBA', (width, 1000), (0, 0, 0, 0))
    test_draw = ImageDraw.Draw(test_img)

    content_width = width - padding * 2

    # Wrap description
    desc_lines = wrap_text(card['description'], font_body, content_width, test_draw)

    # Calculate heights
    title_height = 24 * SCALE
    desc_height = len(desc_lines) * 20 * SCALE
    tagline_height = 24 * SCALE
    badge_height = 28 * SCALE

    total_height = padding + badge_height + 8 * SCALE + title_height + 12 * SCALE + desc_height + 16 * SCALE + tagline_height + padding

    # Create image
    img = Image.new('RGBA', (width, int(total_height)), hex_to_rgb(theme['background']) + (255,))
    draw = ImageDraw.Draw(img)

    y = padding

    # Status badge (top right)
    status = card['status']
    badge_bbox = draw.textbbox((0, 0), status['text'], font=font_badge)
    badge_text_width = badge_bbox[2] - badge_bbox[0]
    badge_x = width - padding - badge_text_width - 16 * SCALE
    draw_status_badge(draw, status['text'], status['color'], badge_x, y, font_badge)

    y += badge_height + 8 * SCALE

    # Icon + Title
    icon_text = card['icon']
    draw.text((padding, y), icon_text, fill=hex_to_rgb(theme['text_secondary']), font=font_icon)

    icon_bbox = draw.textbbox((0, 0), icon_text, font=font_icon)
    icon_width = icon_bbox[2] - icon_bbox[0]

    draw.text(
        (padding + icon_width + 10 * SCALE, y),
        card['title'],
        fill=hex_to_rgb(theme['text_primary']),
        font=font_title
    )

    y += title_height + 12 * SCALE

    # Description
    for line in desc_lines:
        draw.text(
            (padding, y),
            line,
            fill=hex_to_rgb(theme['text_secondary']),
            font=font_body
        )
        y += 20 * SCALE

    y += 8 * SCALE

    # Tagline
    draw.text(
        (padding, y),
        card['tagline'],
        fill=hex_to_rgb(theme['text_primary']),
        font=font_tagline
    )

    return img

def create_animated_card(card, theme):
    """Create an animated GIF card with cycling status."""
    width = theme['card_width'] * SCALE
    padding = theme['card_padding'] * SCALE

    # Fonts
    font_icon = get_font(18)
    font_title = get_font(16, bold=True)
    font_body = get_font(12)
    font_tagline = get_font(12, bold=True)
    font_badge = get_font(10)

    # Calculate content height (same as static)
    test_img = Image.new('RGBA', (width, 1000), (0, 0, 0, 0))
    test_draw = ImageDraw.Draw(test_img)
    content_width = width - padding * 2
    desc_lines = wrap_text(card['description'], font_body, content_width, test_draw)

    title_height = 24 * SCALE
    desc_height = len(desc_lines) * 20 * SCALE
    tagline_height = 24 * SCALE
    badge_height = 28 * SCALE

    total_height = padding + badge_height + 8 * SCALE + title_height + 12 * SCALE + desc_height + 16 * SCALE + tagline_height + padding

    frames = []
    durations = []

    status = card['status']
    phases = status['phases']
    dot_cycles = status.get('dot_cycles', 5)

    for phase in phases:
        phase_text = phase['text']
        phase_color = phase['color']

        # Type out the phase name
        for i in range(len(phase_text) + 1):
            img = Image.new('RGBA', (width, int(total_height)), hex_to_rgb(theme['background']) + (255,))
            draw = ImageDraw.Draw(img)

            y = padding

            # Animated badge
            display_text = phase_text[:i] + "_" if i < len(phase_text) else phase_text
            badge_bbox = draw.textbbox((0, 0), display_text, font=font_badge)
            badge_text_width = badge_bbox[2] - badge_bbox[0]
            badge_x = width - padding - badge_text_width - 16 * SCALE - 50 * SCALE  # Extra space for dots
            draw_status_badge(draw, display_text, phase_color, badge_x, y, font_badge)

            y += badge_height + 8 * SCALE

            # Rest of card (static content)
            draw_static_content(draw, card, theme, y, padding, width, font_icon, font_title, font_body, font_tagline, desc_lines)

            frames.append(img)
            durations.append(50)

        # Dot cycling for this phase
        for _ in range(dot_cycles):
            for num_dots in range(1, 4):
                img = Image.new('RGBA', (width, int(total_height)), hex_to_rgb(theme['background']) + (255,))
                draw = ImageDraw.Draw(img)

                y = padding

                dots = "." * num_dots
                display_text = phase_text + dots
                badge_bbox = draw.textbbox((0, 0), display_text, font=font_badge)
                badge_text_width = badge_bbox[2] - badge_bbox[0]
                badge_x = width - padding - badge_text_width - 16 * SCALE
                draw_status_badge(draw, display_text, phase_color, badge_x, y, font_badge)

                y += badge_height + 8 * SCALE

                draw_static_content(draw, card, theme, y, padding, width, font_icon, font_title, font_body, font_tagline, desc_lines)

                frames.append(img)
                durations.append(300)

    return frames, durations

def draw_static_content(draw, card, theme, y, padding, width, font_icon, font_title, font_body, font_tagline, desc_lines):
    """Draw the static portions of a card (icon, title, description, tagline)."""
    # Icon + Title
    icon_text = card['icon']
    draw.text((padding, y), icon_text, fill=hex_to_rgb(theme['text_secondary']), font=font_icon)

    icon_bbox = draw.textbbox((0, 0), icon_text, font=font_icon)
    icon_width = icon_bbox[2] - icon_bbox[0]

    draw.text(
        (padding + icon_width + 10 * SCALE, y),
        card['title'],
        fill=hex_to_rgb(theme['text_primary']),
        font=font_title
    )

    y += 24 * SCALE + 12 * SCALE

    # Description
    for line in desc_lines:
        draw.text(
            (padding, y),
            line,
            fill=hex_to_rgb(theme['text_secondary']),
            font=font_body
        )
        y += 20 * SCALE

    y += 8 * SCALE

    # Tagline
    draw.text(
        (padding, y),
        card['tagline'],
        fill=hex_to_rgb(theme['text_primary']),
        font=font_tagline
    )

def generate_card(card, theme, output_dir):
    """Generate a card (PNG or GIF based on status type)."""
    card_id = card['id']
    status_type = card['status']['type']

    if status_type == 'animated':
        frames, durations = create_animated_card(card, theme)
        output_path = os.path.join(output_dir, f"card-{card_id}.gif")

        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=durations,
            loop=0,
            disposal=2
        )
        print(f"  ✓ {card_id}: GIF ({len(frames)} frames)")
    else:
        img = create_static_card(card, theme)
        output_path = os.path.join(output_dir, f"card-{card_id}.png")
        img.save(output_path, 'PNG')
        print(f"  ✓ {card_id}: PNG")

    return output_path

def main():
    # Load config
    config_path = os.path.join(os.path.dirname(__file__), 'cards.json')
    with open(config_path, 'r') as f:
        config = json.load(f)

    theme = config['theme']
    cards = config['cards']

    # Output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'assets', 'cards')
    os.makedirs(output_dir, exist_ok=True)

    # Filter cards if specific ID provided
    if len(sys.argv) > 1:
        card_ids = sys.argv[1:]
        cards = [c for c in cards if c['id'] in card_ids]
        if not cards:
            print(f"No cards found with IDs: {card_ids}")
            return

    print(f"Generating {len(cards)} cards...")

    for card in cards:
        generate_card(card, theme, output_dir)

    print(f"\nCards saved to {output_dir}/")
    print("\nTo use in README (responsive layout):")
    print("```markdown")
    print('<p align="center">')
    for card in cards:
        ext = 'gif' if card['status']['type'] == 'animated' else 'png'
        print(f'<img src="assets/cards/card-{card["id"]}.{ext}" width="400"/>')
    print('</p>')
    print("```")

if __name__ == "__main__":
    main()
