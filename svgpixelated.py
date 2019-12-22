from PIL import Image

# 
# get dominant color in an area
def getDominantColor(img, startx, endx, starty, endy):
  totr = 0
  totg = 0
  totb = 0
  tot = 0
  for x in range(startx, endx):
    for y in range(starty, endy):
      r, g, b = img.getpixel((x, y))
      totr += r
      totg += g
      totb += b
      tot = tot + 1

  return (int(totr/tot), int(totg/tot), int(totb/tot))

#
# Main
#

img = Image.open('image.png')
width, height = img.size
radius = 7
diameter = radius * 2
stroke_w = 1

html = open("image.html","w+")

html.write('<!DOCTYPE html>' + "\n")
html.write('<html>' + "\n")
html.write('<body>' + "\n")
html.write('<h1>SVGPixelated art</h1>' + "\n")
html.write('<svg width="' + str(width) + '" height="' + str(height) + '">' + "\n")

for x in range(radius, width, diameter):
  for y in range(radius, height, diameter):
    mycolor = getDominantColor(img, x - radius, min(x + radius, width), y - radius, min(y + radius, height))
    html_color = "#{:02x}{:02x}{:02x}".format(mycolor[0], mycolor[1], mycolor[2]) 

    cx = x + stroke_w
    cy = y + stroke_w
    html.write('   <circle cx="' + str(cx) + '" cy="' + str(cy) + '" r="' + str(radius) + '" stroke="black" stroke-width="' + str(stroke_w) + '" fill="' + str(html_color) + '" />' + "\n")

html.write('   Sorry, your browser does not support inline SVG.' + "\n")
html.write('</svg>' + "\n")
html.write('</body>' + "\n")
html.write('</html>' + "\n")
html.close()