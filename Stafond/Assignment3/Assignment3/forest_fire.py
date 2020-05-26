"""
File: forestfire.py
----------------
"""

from simpleimage import SimpleImage

def buscar_fuego(filename):

    image = SimpleImage(filename)

    for pixel in (image):

        prome = (pixel.red + pixel.green + pixel.blue) // 3

        if pixel.red >= prome  :
            pixel.red=255
            pixel.green=0
            pixel.blue=0
        else:
            pixel.red=prome
            pixel.green=prome
            pixel.blue=prome

    return image

def main():

    image = ('images/greenland-fire.png')

    # Aqui Muestra la imagen original
    original_fire = SimpleImage(image)
    original_fire.show()

    # Aqui muestra la imagen Editada
    highlighted_fire = buscar_fuego(image)
    highlighted_fire.show()

if __name__ == '__main__':
    main()
