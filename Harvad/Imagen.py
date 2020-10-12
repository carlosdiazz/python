from PIL import Image, ImageFilter

antes = Image.open("hey.jpg")
despues = antes.filter(ImageFilter.BLUR)
despues.save("Salida.jpg")

despues = antes.filter(ImageFilter.CONTOUR)
despues.save("Salida2.jpg")

despues = antes.filter(ImageFilter.DETAIL)
despues.save("Salida3.jpg")

despues = antes.filter(ImageFilter.EDGE_ENHANCE)
despues.save("Salida4.jpg")

despues = antes.filter(ImageFilter.EDGE_ENHANCE_MORE)
despues.save("Salida5.jpg")

despues = antes.filter(ImageFilter.EMBOSS)
despues.save("Salida6.jpg")

despues = antes.filter(ImageFilter.FIND_EDGES)
despues.save("Salida7.jpg")

despues = antes.filter(ImageFilter.SHARPEN)
despues.save("Salida8.jpg")

despues = antes.filter(ImageFilter.SMOOTH)
despues.save("Salida9.jpg")

despues = antes.filter(ImageFilter.SMOOTH_MORE)
despues.save("Salida10.jpg")

