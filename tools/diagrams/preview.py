import sys, glob, os, cairosvg, io
from PIL import Image
pat = sys.argv[1]; out = sys.argv[2]; cols = int(sys.argv[3]) if len(sys.argv) > 3 else 2
files = sorted(glob.glob(f"../../docs/chapters/img/{pat}*.svg"))
ims = [Image.open(io.BytesIO(cairosvg.svg2png(url=f, scale=0.9))).convert("RGB") for f in files]
w = max(i.width for i in ims); h = max(i.height for i in ims)
rows = (len(ims) + cols - 1) // cols
sheet = Image.new("RGB", (cols * w, rows * h), "white")
for k, im in enumerate(ims): sheet.paste(im, ((k % cols) * w, (k // cols) * h))
sheet.save(out); print(len(ims), "figures ->", out)
