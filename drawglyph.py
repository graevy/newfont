# pinning everything to python 312 yields some build errors i won't bother with
# just nix-shell -p pkgs.python312 pkgs.python312Packages.pillow if you want to use this

from PIL import Image, ImageDraw, ImageFont

font_path = "JetBrainsMonoRegularBar.ttf"
unicode_char = "\uE005"

font = ImageFont.truetype(font_path, size=50)
image = Image.new("RGB", (100, 100), "white")
draw = ImageDraw.Draw(image)
draw.text((10, 10), unicode_char, font=font, fill="black")
image.show()
