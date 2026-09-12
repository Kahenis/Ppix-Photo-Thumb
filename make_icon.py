"""Icone PPix Photo-thumb."""
from pathlib import Path
from PIL import Image, ImageDraw

def main() -> None:
    out = Path(__file__).resolve().parent / "icon.ico"
    sizes = [16, 24, 32, 48, 64, 128, 256]
    frames = []
    for s in sizes:
        im = Image.new("RGBA", (s, s), (22, 22, 22, 255))
        d = ImageDraw.Draw(im)
        m = max(1, s // 10)
        d.rounded_rectangle((m, m, s - m - 1, s - m - 1), radius=s // 6, fill=(229, 160, 13, 255))
        p = s // 3
        d.polygon([(p + s // 16, p), (p + s // 16, s - p), (s - p, s // 2)], fill=(22, 22, 22, 255))
        frames.append(im)
    frames[0].save(out, format="ICO", sizes=[(s, s) for s in sizes], append_images=frames[1:])
    print(out)

if __name__ == "__main__":
    main()
