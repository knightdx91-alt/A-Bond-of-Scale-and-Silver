#!/usr/bin/env python3
"""Front cover — 'A Bond of Scale and Silver'. Cold moon (silver) + rising dragon-scale field (scale)."""
import base64, os
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
title_font = b64(f"{FONT_DIR}/YoungSerif-Regular.ttf")
serif_font = b64(f"{FONT_DIR}/IBMPlexSerif-Regular.ttf")
serif_it   = b64(f"{FONT_DIR}/IBMPlexSerif-Italic.ttf")

# ---- dragon-scale field: overlapping domes on a curve that arcs up at centre ----
W = 1600
ROW_COLORS = ["#8c96a4","#7c8593","#6c7581","#5c6570","#4d555f","#40474f","#343941","#282d34",
              "#1e222a","#161a20","#0f1218","#0a0c12"]
def ybase(x):  # crest highest at centre (the curve of a coiled flank)
    return 1770 + 200*((x-800)/820.0)**2
sw, sh, rowH, step = 70, 54, 40, 63
scales = []
nrows = len(ROW_COLORS)
for r in range(nrows):
    col = ROW_COLORS[r]
    offset = (r % 2) * (step/2)
    x = -60 + offset
    while x < W + 60:
        y = ybase(x) + r*rowH
        # scale with a soft apex (reptilian armour, not a seat)
        d = (f"M {x-sw/2:.0f},{y:.0f} "
             f"C {x-sw/2:.0f},{y-sh:.0f} {x-sw*0.16:.0f},{y-sh*1.14:.0f} {x:.0f},{y-sh*1.14:.0f} "
             f"C {x+sw*0.16:.0f},{y-sh*1.14:.0f} {x+sw/2:.0f},{y-sh:.0f} {x+sw/2:.0f},{y:.0f} Z")
        red = (r == 2 and abs(x-800) < step*0.6)   # ONE restrained blood-red scale
        fill = "#7a1220" if red else col
        rim  = "#b53146" if red else "rgba(206,213,224,%.2f)" % max(0.04, 0.42-0.04*r)
        scales.append(f'<path d="{d}" fill="{fill}" stroke="{rim}" stroke-width="{2.0 if red else 1.1:.1f}"/>')
        x += step
scale_svg = ('<svg viewBox="0 0 1600 2560" width="1600" height="2560" '
             'xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0;z-index:1;">'
             + "\n".join(scales) + '</svg>')

html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Young';src:url(data:font/ttf;base64,{title_font}) format('truetype');}}
@font-face{{font-family:'Plex';src:url(data:font/ttf;base64,{serif_font}) format('truetype');}}
@font-face{{font-family:'PlexIt';src:url(data:font/ttf;base64,{serif_it}) format('truetype');font-style:italic;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1600px;height:2560px;}}
.cover{{position:relative;width:1600px;height:2560px;overflow:hidden;font-family:'Plex',serif;
  background:radial-gradient(120% 66% at 50% 17%, #141b2b 0%, #0b0f1b 38%, #06080f 70%, #04050b 100%);}}
.vig{{position:absolute;inset:0;box-shadow:inset 0 0 470px 130px rgba(2,3,8,.9);pointer-events:none;}}
.botfade{{position:absolute;left:0;right:0;bottom:0;height:420px;
  background:linear-gradient(180deg,rgba(4,5,11,0),rgba(4,5,11,.72));}}
.moonwrap{{position:absolute;left:50%;top:560px;transform:translate(-50%,-50%);}}
.glow{{position:absolute;left:50%;top:50%;width:1160px;height:1160px;transform:translate(-50%,-50%);
  background:radial-gradient(circle,rgba(201,207,216,.26) 0%,rgba(150,160,176,.07) 36%,rgba(0,0,0,0) 62%);}}
.moon{{position:relative;width:540px;height:540px;border-radius:50%;
  background:radial-gradient(circle at 41% 37%, #eef1f5 0%, #d6dbe3 32%, #b6bdc9 56%, #8b94a2 80%, #6b7484 100%);
  box-shadow:0 0 94px 12px rgba(201,207,216,.22), inset -48px -32px 92px rgba(52,58,72,.6),
             inset 30px 24px 70px rgba(255,255,255,.12);}}
.cr{{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(74,80,94,.4),rgba(74,80,94,0) 72%);}}
.titleblock{{position:absolute;left:0;right:0;top:1180px;text-align:center;z-index:5;}}
.pre{{font-family:'Plex';letter-spacing:.46em;font-size:50px;color:#aeb6c4;text-indent:.46em;
  text-transform:uppercase;opacity:.92;margin-bottom:30px;}}
.main{{font-family:'Young';font-size:174px;line-height:1.0;
  background:linear-gradient(180deg,#f5f7fa 0%,#d2d8e1 44%,#9aa2b1 72%,#b5762e 130%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 4px 26px rgba(0,0,0,.55));}}
.amp{{font-family:'PlexIt';font-style:italic;font-size:122px;-webkit-text-fill-color:#c2c8d3;color:#c2c8d3;}}
.rule{{width:180px;height:3px;margin:42px auto 0;background:linear-gradient(90deg,rgba(141,22,38,0),#a11d2e 50%,rgba(141,22,38,0));}}
.novel{{font-family:'PlexIt';font-style:italic;font-size:48px;color:#9aa2b0;margin-top:34px;letter-spacing:.05em;}}
.author{{position:absolute;left:0;right:0;bottom:150px;text-align:center;font-family:'Plex';z-index:5;
  letter-spacing:.44em;text-indent:.44em;font-size:54px;color:#dfe4ec;text-transform:uppercase;
  text-shadow:0 2px 18px rgba(0,0,0,.8);}}
.authorlbl{{position:absolute;left:0;right:0;bottom:112px;text-align:center;font-size:21px;z-index:5;
  letter-spacing:.3em;color:#6b7484;text-transform:uppercase;}}
</style></head><body>
<div class="cover">
  <div class="moonwrap"><div class="glow"></div>
    <div class="moon">
      <div class="cr" style="width:66px;height:66px;left:118px;top:140px;opacity:.7;"></div>
      <div class="cr" style="width:92px;height:92px;left:300px;top:322px;opacity:.6;"></div>
      <div class="cr" style="width:40px;height:40px;left:330px;top:120px;opacity:.5;"></div>
    </div></div>
  {scale_svg}
  <div style="position:absolute;left:0;right:0;top:1700px;height:300px;z-index:2;
       background:linear-gradient(180deg,#06080f 0%,rgba(6,8,15,.75) 40%,rgba(6,8,15,0) 100%);"></div>
  <div class="botfade"></div>
  <div class="titleblock">
    <div class="pre">A Bond of</div>
    <div class="main">Scale <span class="amp">&amp;</span> Silver</div>
    <div class="rule"></div>
    <div class="novel">a novel</div>
  </div>
  <div class="author">Author Name</div>
  <div class="authorlbl">— placeholder —</div>
  <div class="vig"></div>
</div></body></html>'''
open(os.path.join(os.path.dirname(__file__),"cover.html"),"w").write(html); print("ok")
