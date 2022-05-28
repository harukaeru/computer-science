import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def identity(image):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0]], np.float32)
    affine = cv2.getAffineTransform(src, src)
    return cv2.warpAffine(image, affine, (w, h))

def shift_x(image, shift):
    h, w = image.shape[:2]
    affine = np.array([
        [1.0, 0.0, 0],
        [0.0, 1.0, 0],
    ])
    affine[0, 2] += shift
    affine[1, 2] += shift / 2
    affine[0, 0] = shift / 100
    affine[1, 1] = shift / 80 * (-1 if shift // 50 % 2 == 0 else 1)
    # affine[1, 1] = -1
    # affine[1, 1] += shift / 300 * (-1 if 0 <= shift <= 100 else 1)

    return cv2.warpAffine(image, affine, (w, h))


if __name__ == "__main__":
    fig = plt.figure()
    image = cv2.imread("harukaeru.png")[:, :, ::-1]

    def update(i):
        plt.cla()
        converted = shift_x(image, i)
        plt.imshow(converted)
        plt.title(f'shift {i}')

    ani = animation.FuncAnimation(
        fig, update, np.arange(10, 400, 5), interval=1
    )

    plt.show()

    # for i in range(10, 300, 10):
    #     converted = shift_x(image, i)
    #     plt.imshow(converted)
    #     plt.title("Identity")
    #     plt.show()
