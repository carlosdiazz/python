
from simpleimage import SimpleImage

def make_reflected(image):

    imagen=SimpleImage(image)
    ancho=imagen.width
    alto=imagen.height
    espejo=SimpleImage.blank(ancho,alto*2)



    for y in range(alto):
        for x in range(ancho):

            pixel=imagen.get_pixel(x,y)

            espejo.set_pixel(x,y,pixel)

            espejo.set_pixel(x,(alto*2)-(y+1),pixel)

    return espejo

def main():

    imagen='images/mt-rainier.jpg'

    original = SimpleImage(imagen)
    original.show()



    reflected = make_reflected(imagen)
    reflected.show()


if __name__ == '__main__':
    main()
