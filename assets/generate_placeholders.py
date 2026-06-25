# 시안 자리표시 이미지 생성기 — 실제 이미지가 준비되기 전까지 순환 데모가 보이도록.
# 실제 이미지로 교체할 때는 같은 파일명(ig-1.svg … / a4-1.svg …)으로 덮어쓰면 됨.
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PAL = [
    ("#f7e2c9", "#e9b783"),
    ("#efe8dc", "#d2bd9a"),
    ("#f8dcc2", "#e7a06f"),
    ("#ece5d7", "#c7b288"),
    ("#f4e4d0", "#dcbd8f"),
]
FONT = "-apple-system,'Apple SD Gothic Neo','Malgun Gothic','Segoe UI',sans-serif"


def baguette(cx, cy, rx, ry, rot):
    return f'''<g transform="translate({cx} {cy}) rotate({rot})">
    <ellipse cx="0" cy="0" rx="{rx}" ry="{ry}" fill="#e8b676" stroke="#b9803f" stroke-width="{ry*0.06:.0f}"/>
    <g stroke="#9c6328" stroke-width="{ry*0.09:.0f}" stroke-linecap="round" opacity="0.8">
      <line x1="{-rx*0.5:.0f}" y1="{-ry*0.42:.0f}" x2="{-rx*0.37:.0f}" y2="{-ry*0.02:.0f}"/>
      <line x1="{-rx*0.13:.0f}" y1="{-ry*0.48:.0f}" x2="{0:.0f}" y2="{-ry*0.08:.0f}"/>
      <line x1="{rx*0.23:.0f}" y1="{-ry*0.46:.0f}" x2="{rx*0.37:.0f}" y2="{-ry*0.06:.0f}"/>
    </g>
  </g>'''


def ig_svg(n, c1, c2):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
    <radialGradient id="vig" cx="0.5" cy="0.4" r="0.75"><stop offset="0.55" stop-color="#ffffff" stop-opacity="0"/><stop offset="1" stop-color="#5a3a18" stop-opacity="0.12"/></radialGradient>
  </defs>
  <rect width="1080" height="1350" fill="url(#bg)"/>
  <rect width="1080" height="1350" fill="url(#vig)"/>
  <text x="540" y="455" text-anchor="middle" font-size="170" font-weight="800" fill="#8a5a28" fill-opacity="0.14">시안 {n}</text>
  {baguette(540, 705, 300, 96, -18)}
  <text x="540" y="1145" text-anchor="middle" font-size="54" font-weight="700" fill="#7a4f22">AI 생성 시안 #{n}</text>
  <text x="540" y="1210" text-anchor="middle" font-size="36" fill="#7a4f22" fill-opacity="0.7">바게트 · 오늘만 20% · @oven_mangwon</text>
</svg>
'''


def a4_svg(n, c1, c2):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
    <radialGradient id="vig" cx="0.5" cy="0.42" r="0.8"><stop offset="0.55" stop-color="#ffffff" stop-opacity="0"/><stop offset="1" stop-color="#5a3a18" stop-opacity="0.12"/></radialGradient>
  </defs>
  <rect width="800" height="500" fill="url(#bg)"/>
  <rect width="800" height="500" fill="url(#vig)"/>
  <text x="400" y="205" text-anchor="middle" font-size="92" font-weight="800" fill="#8a5a28" fill-opacity="0.14">시안 {n}</text>
  {baguette(400, 270, 220, 64, -14)}
  <text x="400" y="430" text-anchor="middle" font-size="30" font-weight="700" fill="#7a4f22">AI 팝카드 시안 #{n} · 바게트</text>
</svg>
'''


def main():
    for sub in ("instagram", "a4"):
        os.makedirs(os.path.join(BASE, sub), exist_ok=True)
    for i, (c1, c2) in enumerate(PAL, start=1):
        with open(os.path.join(BASE, "instagram", f"ig-{i}.svg"), "w", encoding="utf-8") as f:
            f.write(ig_svg(i, c1, c2))
        with open(os.path.join(BASE, "a4", f"a4-{i}.svg"), "w", encoding="utf-8") as f:
            f.write(a4_svg(i, c1, c2))
    print("generated 5 instagram + 5 a4 placeholder svgs")


if __name__ == "__main__":
    main()
