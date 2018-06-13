from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np

img = ndimage.imread("test_images/lena.jpg", mode='L')
noisy = ndimage.imread("test_images/noisy.png", mode='L')


# threshold the image
def threshold(image, thresh=0):
    image = np.copy(image)
    if thresh == 0:
        thresh = ndimage.mean(image)
    else:
        thresh = thresh

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x][y] >= thresh:
                image[x][y] = 1
            else:
                image[x][y] = 0

    plt.figure("Image threshold")
    plt.imshow(image, cmap='gray')
    plt.title("Black and white images")
    plt.show()


def dither_pattern(img):
    new_img = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
    new_img[1:new_img.shape[0] - 1, 1:new_img.shape[1] - 1] = img

    t1 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    t2 = np.array([[255, 0, 0], [0, 0, 0], [0, 0, 0]])
    t3 = np.array([[255, 255, 0], [0, 0, 0], [0, 0, 0]])
    t4 = np.array([[255, 255, 255], [0, 0, 0], [0, 0, 0]])
    t5 = np.array([[255, 255, 255], [255, 0, 0], [0, 0, 0]])
    t6 = np.array([[255, 255, 255], [255, 255, 0], [0, 0, 0]])
    t7 = np.array([[255, 255, 255], [255, 255, 255], [0, 0, 0]])
    t8 = np.array([[255, 255, 255], [255, 255, 255], [255, 0, 0]])
    t9 = np.array([[255, 255, 255], [255, 255, 255], [255, 255, 0]])
    t10 = np.array([[255, 255, 255], [255, 255, 255], [255, 255, 255]])

    for r in np.arange(1, new_img.shape[0] - 1, 3):
        for c in np.arange(1, new_img.shape[1] - 1, 3):
            curr_reigion = new_img[r - 1:r + 2, c - 1:c + 2]
            average = curr_reigion.sum() // curr_reigion.size
            if average < 25:
                curr_reigion = t1
            elif 51 > average >= 25:
                curr_reigion = t2
            elif 76 > average >= 51:
                curr_reigion = t3
            elif 101 > average >= 75:
                curr_reigion = t4
            elif 126 > average >= 101:
                curr_reigion = t5
            elif 151 > average >= 126:
                curr_reigion = t6
            elif 176 > average >= 151:
                curr_reigion = t7
            elif 201 > average >= 176:
                curr_reigion = t8
            elif 226 > average >= 201:
                curr_reigion = t9
            elif 256 > average >= 226:
                curr_reigion = t10

            new_img[r - 1:r + 2, c - 1:c + 2] = curr_reigion

        final = new_img[1:new_img.shape[0] - 1, 1:new_img.shape[1] - 1]
        plt.figure("Pattern dithering")
        plt.imshow(final, cmap='gray')
        plt.title("Image with Pattern dithering")
        plt.show()


# Filter the image with mean filter
def denoise(noise, alpha=3):
    # mask region mean kernel is it's original values so it's just empty ones
    mask = np.ones([alpha, alpha])
    # image with padding
    image = np.zeros([noise.shape[0] + 2, noise.shape[1] + 2], dtype='uint8')
    image[1:image.shape[0] - 1, 1:image.shape[1] - 1] = noise
    # array of result
    result = np.zeros([image.shape[0] - 2, image.shape[1] - 2])
    # apply filter
    for row in range(image.shape[0] - (mask.shape[0] - 1)):
        for column in range(image.shape[1] - (mask.shape[0] - 1)):
            current_region = image[row:mask.shape[0] + row, column:mask.shape[1] + column]
            apply_mask = current_region * mask
            center_point = np.median(apply_mask)
            result[row][column] = center_point

    plt.figure("Improve image")
    plt.imshow(result, cmap='gray')
    plt.title("Image no noise")
    plt.show()


# floyd dithering
def dither(image, thresh=128):
    errors = []
    image = np.copy(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            old_image = np.copy(image[x][y])
            if old_image >= thresh:
                new_image = 255
            else:
                new_image = 0
            image[x][y] = new_image
            count_error = old_image - new_image
            errors.append(count_error)
            try:
                image[x][y + 1] = int(np.round(image[x][y + 1] + count_error * 7 / 16))
                image[x + 1][y - 1] = int(np.round(image[x + 1][y - 1] + count_error * 3 / 16))
                image[x + 1][y] = int(np.round(image[x + 1][y] + count_error * 5 / 16))
                image[x + 1][y + 1] = int(np.round(image[x + 1][y + 1] + count_error * 1 / 16))
            except IndexError:
                pass
    plt.figure("Floyd Dither")
    plt.imshow(image, cmap='gray')
    plt.title("Image with Floyd dithering")
    plt.show()


'''''
 Ordered Dithering example
---------------------------
matrix = np.array([[20, 75, 80, 90, 150, 113, 50, 160],
                   [150, 90, 180, 84, 155, 80, 220, 100],
                   [50, 176, 16, 200, 220, 180, 15, 130],
                   [235, 128, 190, 70, 220, 110, 220, 85]])
'''''


# apply irder dithering
def ordered_dithering(image):
    thresh_matrix = np.array([[0, 128, 32, 160],
                              [192, 64, 224, 96],
                              [48, 176, 16, 144],
                              [240, 112, 208, 80]])

    image = np.copy(image)

    ix = image.shape[0]
    iy = image.shape[1]
    n = thresh_matrix.shape[0]
    output = np.zeros((ix, iy))
    for x in range(0, ix):
        for y in range(0, iy):
            # get the current region
            i = x % n
            j = y % n
            if image[x][y] >= thresh_matrix[i][j]:
                output[x][y] = 255
            else:
                output[x][y] = 0
    plt.figure("Ordered Dither")
    plt.imshow(output, cmap='gray')
    plt.title("Image with ordered dithering")
    plt.show()
