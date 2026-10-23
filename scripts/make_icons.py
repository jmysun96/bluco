"""앱 아이콘 생성: python3 scripts/make_icons.py (Pillow 필요)."""
from pathlib import Path

from PIL import Image, ImageDraw

CORAL, NAVY, CREAM = (232, 131, 107), (58, 79, 134), (255, 248, 242)
OUT = Path(__file__).resolve().parents[1] / "icons"


def icon(size: int, maskable: bool = False) -> Image.Image:
    k = 4  # 크게 그린 뒤 줄여서 가장자리를 매끄럽게
    S = size * k
    img = Image.new("RGB", (S, S), CORAL)
    d = ImageDraw.Draw(img)
    u = S / 512
    scale = 0.78 if maskable else 1.0  # maskable은 가운데 안전 영역 안에
    cx, cy = S / 2, S / 2 + 8 * u

    def e(x, y, rx, ry, fill):
        x, y = cx + (x - 256) * u * scale, cy + (y - 256) * u * scale
        rx, ry = rx * u * scale, ry * u * scale
        d.ellipse((x - rx, y - ry, x + rx, y + ry), fill=fill)

    e(256, 256, 190, 190, CREAM)          # 바탕 원
    e(256, 300, 78, 64, NAVY)             # 발바닥
    for x, y in ((170, 210), (222, 168), (290, 168), (342, 210)):
        e(x, y, 30, 38, NAVY)             # 발가락
    hx, hy = 256, 300                      # 발바닥 위 하트
    for dx in (-14, 14):
        e(hx + dx, hy - 6, 16, 16, CORAL)
    pts = [(hx - 29, hy - 2), (hx + 29, hy - 2), (hx, hy + 30)]
    d.polygon([(cx + (px - 256) * u * scale, cy + (py - 256) * u * scale) for px, py in pts], fill=CORAL)
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    icon(192).save(OUT / "icon-192.png", optimize=True)
    icon(512).save(OUT / "icon-512.png", optimize=True)
    icon(512, maskable=True).save(OUT / "maskable-512.png", optimize=True)
    icon(180).save(OUT / "apple-touch-icon.png", optimize=True)
    icon(32).save(OUT / "favicon-32.png", optimize=True)
    print("icons written to", OUT)
