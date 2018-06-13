import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage



def rgb2yuv(image):
    Wr = 0.299
    Wb = 0.114
    Wg = 0.587
    Umax = 0.436
    Vmax = 0.615
    # rgb channels
    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]
    Y = Wr * R + Wg * G + Wb * B
    U = Umax * ((B - Y) / (1 - Wb))
    V = Vmax * ((R - Y) / (1 - Wr))
    return Y, U, V


def ploting_rgb2yuv(rgb_image):
    y, u, v = rgb2yuv(rgb_image)

    ''''' Y U V plotting '''''

    plt.figure('Y U V channel plotting')
    plt.subplot(2, 3, 1)
    plt.imshow(y, cmap='gray')
    plt.title('Y channel')
    plt.subplot(2, 3, 2)
    plt.imshow(u)
    plt.title('U channel')
    plt.subplot(2, 3, 3)
    plt.imshow(v, cmap='hot')
    plt.title('V channel')
    # gray view
    plt.subplot(2, 3, 4)
    plt.imshow(y, cmap='gray')
    plt.subplot(2, 3, 5)
    plt.imshow(u, cmap='gray')
    plt.subplot(2, 3, 6)
    plt.imshow(v, cmap='gray')
    plt.show()
    return y,u,v

def yuv2rgb(Y, U, V):
    Wr = 0.299
    Wb = 0.114
    Wg = 0.587
    Umax = 0.436
    Vmax = 0.615
    R = Y + V * ((1 - Wr) / (Vmax))
    G = (Y / Wg) - U * ((Wb * (1 - Wb)) / (Umax * Wg)) - V * ((Wr * (1 - Wr)) / (Vmax * Wg))
    B = Y + U * ((1 - Wb) / Umax)

    return R, G, B


def ploting_yuv2rgb(y,u,v):
    r, g, b = yuv2rgb(y, u, v)

    ''''' R G B plotting '''''
    image = concat_rgb(r, g, b)
    plt.figure("RGB colored")
    plt.imshow(image)

    plt.figure('R G B channel plotting')
    plt.subplot(1, 3, 1)
    plt.imshow(r, cmap='gray')
    plt.title('R channel')
    plt.subplot(1, 3, 2)
    plt.imshow(g, cmap='gray')
    plt.title('G channel')
    plt.subplot(1, 3, 3)
    plt.imshow(b, cmap='gray')
    plt.title('B channel')

    plt.show()

def upsampling4_2_2(y, u, v):
    y_out = y[:, ::2]
    u_out = u[:, ::2]
    v_out = v[:, ::2]
    # convert it again to rgb
    y_rgb, u_rgb, v_rgb = yuv2rgb(y_out, u_out, v_out)
    return y_out, u_out, v_out, y_rgb, u_rgb, v_rgb


def upsampling(y,u,v):
    y_samp, u_samp, v_samp, y_rgb, u_rgb, v_rgb = upsampling4_2_2(y, u, v)
    prove = "The sampling prove: "+ str(y_samp.shape)+", "+str(y_rgb.shape)+", "+ str( y.shape)

    ''''' U V upsampling plotting '''''
    image = concat_rgb(y_rgb, u_rgb, v_rgb)
    plt.figure("RGB colored")
    plt.imshow(image)

    plt.figure('Y U V Up sampling')
    plt.subplot(1, 2, 1)
    plt.imshow(u_samp, cmap='gray')
    plt.title('U sample')
    plt.subplot(1, 2, 2)
    plt.imshow(v_samp, cmap='gray')
    plt.title('v sample')

    plt.show()

    return  prove

# concat RGB channels

def concat_rgb(r_chan, g_chan, b_chan):
    image = np.zeros((r_chan.shape[0], r_chan.shape[1], 3)).astype(np.uint8)
    image[:, :, 0] = r_chan
    image[:, :, 1] = g_chan
    image[:, :, 2] = b_chan
    return image


