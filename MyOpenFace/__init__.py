from __future__ import print_function

import openface


class MyOpenFace:
    def __init__(self, dlib_path, network_model, img_dim=96):
        """

        :param dlib_path:
        :param network_model:
        :param img_dim:
        """
        self.dlib_path = dlib_path
        self.network_model = network_model
        self.img_dim = img_dim
        self.align = openface.AlignDlib(self.dlib_path)
        self.net = openface.TorchNeuralNet(self.network_model, self.img_dim)

    def face_align(self, image):
        """

        :param image:
        :return:
        """
        bounding_box = self.align.getLargestFaceBoundingBox(image)
        return self.align.align(self.img_dim, image, bounding_box)
        # landmarkIndices = openface.AlignDlib.INNER_EYES_AND_BOTTOM_LIP

    def forward(self, aligned_face):
        """

        :param aligned_face:
        :return:
        """
        return self.net.forward(aligned_face)
