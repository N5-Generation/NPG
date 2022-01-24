from django.http import HttpResponseBadRequest
from PIL import Image, ImageDraw
import sys

def ajax_required(f):  
    def wrap(request, *args, **kwargs):

        print(request)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            return f(request, *args, **kwargs)
        return HttpResponseBadRequest()
                
    return wrap

# method from https://gist.github.com/zollinger/1722663
def get_colors(image_file, numcolors=10, resize=150):
    # Resize image to speed up processing
    img = Image.open(image_file)
    img = img.copy()
    img.thumbnail((resize, resize))

    # Reduce to palette
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=numcolors)

    # Find dominant colors
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    colors = list()
    for i in range(numcolors):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        colors.append(tuple(dominant_color))

    return colors
