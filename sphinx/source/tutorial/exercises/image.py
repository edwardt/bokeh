from __future__ import division

import numpy as np
from bokeh.plotting import *

# NOTE: if you do not have numba installed, comment out this import,
# and the 'autojit' lines below (the example will run more slowly).
from numba import autojit

# These functions generate the Mandelbrot set image. Don't worry if
# you are not familiar with them. The import thing is just to know
# that they create a 2D array of numbers that we can colormap.

@autojit
def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iters

@autojit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

# Define the bounding coordinates to generate the Mandelbrot image in. You
# can play around with these.
min_x = -2.0
max_x = 1.0
min_y = -1.0
max_y = 1.0

# Use the functions above to create a scalar image (2D array of numbers)
img = np.zeros((1024, 1536), dtype = np.uint8)
create_fractal(min_x, max_x, min_y, max_y, img, 20)

# EXERCISE: output static HTML file

# EXERCISE: Fill in the missing parameters to use the `image` renderer to
# display the Mandelbrot image 'img' with the title 'Mandelbrot', colormapped
# with the palette 'Spectral-11', and a fixed range given by (min_x, max_x)
# and (min_y, max_y).
#
# NOTE: the `image` renderer can display many images at once, so it takes
# **lists** of images, coordinates, and palettes. Remember to supply sequences
# for these parameters, even if you are just supply one.
image(image=
      x=                                     # lower left x coord
      y=                                     # lower left y coord
      dw=                                    # *data* width of image
      dh=                                    # *data* height of image
      palette=                               # palette to colormap with
      x_range = [min_x, max_y),              # fix the X range
      y_range = [min_y, max_y],              # fix the Y range
      title=                                 # give the plot a title
      tools="pan,wheel_zoom,box_zoom,reset", # add some tools
      plot_width=900,                        # set a width for the plot
      plot_height=600                        # and a height
)

# EXERCISE: create a new figure

# We can also use the `image_rgba` renderer to display RGBA images that
# we have colormapped ourselves.
N = 20
img = np.empty((N,N), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(i/N*255)
        view[i, j, 1] = 158
        view[i, j, 2] = int(j/N*255)
        view[i, j, 3] = 255

# EXERCISE: use `image_rgba` to display the image above. Use the following
# cordinates: (x0,y0) = (0,0)  and (x1,y1) = (10,10). Remember to set the
# x_range and y_range explicitly as above.

show()      # show the plot

