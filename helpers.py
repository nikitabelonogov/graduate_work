import urllib

import cv2
import numpy as np


def url_to_image(url):
    """

    :param url:
    :return:
    """
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def stream_to_image(stream):
    """

    :param stream:
    :return:
    """
    image = np.asarray(bytearray(stream.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
