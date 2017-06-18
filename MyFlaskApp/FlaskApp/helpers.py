import urllib

import cv2
import numpy as np


def url_to_image(url):
    """
    Perform a url to image transformation.
    :param url: url
    :return: image
    """
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def stream_to_image(stream):
    """
    Perform a stream to image transformation.
    :param stream: stream
    :return: image
    """
    image = np.asarray(bytearray(stream.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
