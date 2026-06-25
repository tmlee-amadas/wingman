# 자리표시 이미지 생성기 (JPG) — 실제 이미지가 들어오기 전까지 데모/검증용.
# 실제 이미지로 교체: 같은 파일명(ig-1.jpg … / a4-1.jpg …)으로 덮어쓰면 됨.
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
BOLD = "C:/Windows/Fonts/malgunbd.ttf"
REG = "C:/Windows/Fonts/malgun.ttf"

IG_PAL = [
    ((247, 226, 201), (230, 179, 131)),
    ((239, 232, 220), (210, 189, 155)),
    ((248, 220, 194), (231, 164, 111)),
    ((236, 229, 215), (201, 178, 143)),
]
A4_PAL = [
    ((245, 236, 222), (228, 210, 180)),
    ((240, 235, 222), (219, 203, 168)),
]
INK = (122, 79, 34)
SUB = (150, 110, 70)


def vgrad(w, h, c1, c2):
    col = Image.new("RGB", (1, h))
    px = col.load()
    for y in range(h):
        t = y / (h - 1)
        px[0, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    return col.resize((w, h))


def ctext(d, cx, y, text, fnt, fill, anchor="mm"):
    d.text((cx, y), text, font=fnt, fill=fill, anchor=anchor)


def make(path, w, h, c1, c2, kind, n, sub):
    img = vgrad(w, h, c1, c2)
    d = ImageDraw.Draw(img)
    # soft vignette frame
    d.rounded_rectangle([w * 0.06, h * 0.06, w * 0.94, h * 0.94],
                        radius=int(w * 0.04), outline=(255, 255, 255, 120), width=max(2, w // 360))
    f_kicker = ImageFont.truetype(BOLD, int(w * 0.045))
    f_num = ImageFont.truetype(BOLD, int(w * 0.34))
    f_sub = ImageFont.truetype(BOLD, int(w * 0.05))
    f_path = ImageFont.truetype(REG, int(w * 0.033))
    ctext(d, w / 2, h * 0.22, "WINGMAN · 자리표시 시안", f_kicker, SUB)
    ctext(d, w / 2, h * 0.46, str(n), f_num, INK)
    ctext(d, w / 2, h * 0.68, sub, f_sub, INK)
    ctext(d, w / 2, h * 0.80, "여기에 실제 이미지를 넣어주세요", f_path, SUB)
    ctext(d, w / 2, h * 0.855, os.path.relpath(path, BASE).replace("\\", "/"), f_path, SUB)
    img.save(path, "JPEG", quality=86)


def main():
    for sub in ("instagram", "a4"):
        os.makedirs(os.path.join(BASE, sub), exist_ok=True)
    for i, (c1, c2) in enumerate(IG_PAL, start=1):
        make(os.path.join(BASE, "instagram", f"ig-{i}.jpg"), 1080, 1350, c1, c2, "ig", i, "인스타 시안")
    for i, (c1, c2) in enumerate(A4_PAL, start=1):
        make(os.path.join(BASE, "a4", f"a4-{i}.jpg"), 1000, 1414, c1, c2, "a4", i, "A4 팝카드 시안")
    print("generated 4 instagram + 2 a4 placeholder jpgs")


if __name__ == "__main__":
    main()
