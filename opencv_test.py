import cv2 as cv

if __name__ == '__main__':
    image = cv.imread('images/peter.png')
    # # convert to RGB
    # image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    # # convert to grayscale
    # gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    #
    # # create a binary thresholded image
    # _, binary = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
    # # show it
    # plt.imshow(binary, cmap="gray")
    # plt.show()
    #
    # # find the contours from the thresholded image
    # contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # # draw all contours
    # image = cv.drawContours(image, contours, -1, (0, 255, 0), 2)
    #
    # # show the image with the drawn contours
    # plt.imshow(image)
    # plt.show()

    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(image, contours, -1, (0, 255, 0), 3)

    for element in contours:
        print(element)

    cv.imshow('Contours', image)
    cv.waitKey(0)