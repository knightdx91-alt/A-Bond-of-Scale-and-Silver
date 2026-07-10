#!/usr/bin/env python3
"""Composite the title over the clean Canva art for 'A Bond of Scale and Silver' (Post Peleos).
Final = silver-to-ember title, no blood-red (only the natural pendant gem in the art)."""
import base64, os
HERE = os.path.dirname(__file__)
FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
art   = b64(os.path.join(HERE, "front-art-nolabel.png"))   # clean Canva art, text stripped
young = b64(f"{FONT_DIR}/YoungSerif-Regular.ttf")
plex  = b64(f"{FONT_DIR}/IBMPlexSerif-Regular.ttf")

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Young';src:url(data:font/ttf;base64,{young}) format('truetype');}}
@font-face{{font-family:'Plex';src:url(data:font/ttf;base64,{plex}) format('truetype');}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1600px;height:2263px;}}
.cover{{position:relative;width:1600px;height:2263px;overflow:hidden;
  background:url(data:image/png;base64,{art}) center/cover no-repeat;font-family:'Plex',serif;}}
.scrim{{position:absolute;left:0;right:0;bottom:0;height:1000px;
  background:linear-gradient(180deg,rgba(4,6,13,0) 0%,rgba(4,6,13,.35) 34%,rgba(4,6,13,.72) 62%,rgba(4,6,13,.9) 100%);}}
.titleblock{{position:absolute;left:0;right:0;top:1470px;text-align:center;}}
.pre{{font-family:'Plex';letter-spacing:.5em;text-indent:.5em;font-size:52px;color:#c3cad6;
  text-transform:uppercase;margin-bottom:26px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.85));}}
.main{{font-family:'Young';font-size:150px;line-height:.98;text-transform:uppercase;letter-spacing:.02em;
  background:linear-gradient(180deg,#fbfcfe 0%,#dfe4ec 40%,#aab2c0 68%,#c8934a 112%,#b5762e 140%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 4px 16px rgba(0,0,0,.95));}}
.divider{{display:flex;align-items:center;justify-content:center;gap:20px;margin:40px auto 0;width:520px;}}
.divider .ln{{height:2px;flex:1;background:linear-gradient(90deg,rgba(200,210,224,0),rgba(200,210,224,.75));}}
.divider .ln.r{{background:linear-gradient(90deg,rgba(200,210,224,.75),rgba(200,210,224,0));}}
.divider .dot{{width:9px;height:9px;transform:rotate(45deg);background:#c8ceda;box-shadow:0 0 10px rgba(0,0,0,.8);}}
.author{{position:absolute;left:0;right:0;bottom:120px;text-align:center;font-family:'Plex';
  letter-spacing:.46em;text-indent:.46em;font-size:66px;color:#e6eaf1;text-transform:uppercase;
  filter:drop-shadow(0 3px 14px rgba(0,0,0,.95));}}
</style></head><body>
<div class="cover">
  <div class="scrim"></div>
  <div class="titleblock">
    <div class="pre">A Bond of</div>
    <div class="main">Scale and<br>Silver</div>
    <div class="divider"><span class="ln"></span><span class="dot"></span><span class="ln r"></span></div>
  </div>
  <div class="author">Post Peleos</div>
</div></body></html>'''
open(os.path.join(HERE, "compose.html"), "w").write(html); print("ok")
