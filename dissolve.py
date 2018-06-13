import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# img1 = np.array(Image.open("test_images/lena.jpg").convert('L').resize((500, 500)))
img = np.array(Image.open("test_images/baby.jpg").convert('RGB').resize((500, 500)))
# fade_img = np.array(Image.open("test_images/baby.jpg").convert('RGBA').resize((500, 500)))
plt.imshow(255-img)
plt.show()

def dither_dissolve(image1, image2):
    plt.ion()
    fig = plt.figure("Dither Dissolve")
    plt.axis('off')
    im = plt.imshow(image1, cmap='gray')
    fig.canvas.draw()
    dx, dy = image1.shape
    for x in range(dy):
        for y in range(dx):
            image1[y][x] = image2[y][x]
        im.set_data(image1)
        fig.canvas.flush_events()
        plt.show(block=False)

''''' Apply wisp '''''
# dither_dissolve(img1, img2)


def cross_dissolve(image1, image2, alpha=0.4, time=1):
    fig = plt.figure("Cross dissolve")
    plt.axis('off')
    dx, dy = image1.shape
    D = np.ones((dx, dy))
    for x in range(dy):
        for y in range(dx):
            D[x][y] = ((1 - alpha) * image1[x][y]) + alpha * image2[x][y]

    plt.imshow(image1, cmap='gray')
    plt.pause(time)
    fig.clear()
    plt.imshow(D, cmap='gray')
    plt.draw()
    plt.pause(time)
    fig.clear()
    plt.imshow(image2, cmap='gray')
    plt.draw()
    plt.show(block=True)

''''' Apply blend two images '''''
# cross_dissolve(img1 , img2, alpha=0.4,time=1)


def fade_in(in_img):
    plt.ion()
    fig = plt.figure("Fade In image effect")
    plt.axis('off')
    im = plt.imshow(in_img)
    fig.canvas.draw()
    count = 0
    for x in range(0, 255):
        in_img[:, :, 3] = count
        count += 2
        im.set_data(in_img)
        fig.canvas.flush_events()
        plt.show(block=False)

''''' Apply Fade In '''''
# fade_in(fade_img)


def fade_out(out_img):
    plt.ion()
    fig = plt.figure("Fade Out image effect")
    plt.axis('off')
    im = plt.imshow(out_img, cmap='gray')
    fig.canvas.draw()
    count = 255
    for x in range(0, 255):
        out_img[:, :, 3] = count
        count -= 2
        im.set_data(out_img)
        fig.canvas.flush_events()
        plt.show(block=False)

''''' Apply Fade Out '''''
# fade_out(fade_img)
