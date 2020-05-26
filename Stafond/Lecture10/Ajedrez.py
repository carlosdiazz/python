
import tkinter
import time
import random

WIDTH = 800
HEIGHT = 600
SIZE = 100

def main():


    canvas=make_canvas(800,800,"Hola Mundo")

    x1 = 0
    x2 = 100
    for i in range(5):

        canvas.create_rectangle(x1,0,x2,100, fill="black")
        x1=x1+100
        x2=x2+100
    canvas.mainloop()
        #canvas.create_rectangle(200,0,300,100, fill="black")
        #canvas.create_rectangle(400,0,500,100, fill="black")
        #canvas.create_rectangle(600, 0, 700, 100, fill="black")

    #canvas.mainloop()



######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas

if __name__ == '__main__':
    main()
