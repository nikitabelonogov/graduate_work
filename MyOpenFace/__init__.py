from __future__ import print_function

import openface


class MyOpenFace:
    def __init__(self, dlib_path, network_model, img_dim=96):
        self.dlib_path = dlib_path
        self.network_model = network_model
        self.img_dim = img_dim
        self.align = openface.AlignDlib(self.dlib_path)
        self.net = openface.TorchNeuralNet(self.network_model, self.img_dim)

    def face_align(self, image):
        bounding_box = self.align.getLargestFaceBoundingBox(image)
        return self.align.align(self.img_dim, image, bounding_box)
        # landmarkIndices = openface.AlignDlib.INNER_EYES_AND_BOTTOM_LIP

    def forward(self, aligned_face):
        return self.net.forward(aligned_face)

    # dlibPath = '/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
    # networkModel = '/root/openface/models/openface/nn4.small2.v1.t7'
    # imgDim = 96
    # imagePaths = ['face-01.jpg',
    #               'face-02.jpg']
    #
    # align = openface.AlignDlib(dlibPath)
    # net = openface.TorchNeuralNet(networkModel, imgDim)
    # reps = []

    # openFace = MyOpenFace('/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat',
    #                     '/root/openface/models/openface/nn4.small2.v1.t7')

    # for imagePath in imagePaths:
    #     image = cv2.imread(imagePath)
    #     bb = align.getLargestFaceBoundingBox(image)
    #     cv2.rectangle(image, (bb.left(), bb.top()), (bb.right(), bb.bottom()), (0, 255, 0), 2)
    #
    # alignedFace = align.align(imgDim, image, bb, landmarkIndices=openface.AlignDlib.INNER_EYES_AND_BOTTOM_LIP)
    #
    # cv2.imwrite(imagePath + 'result.jpg', alignedFace)
    #
    # rep = net.forward(alignedFace)
    # print(rep)
    # reps.append((imagePath, rep))

#
# for l in reps:
#     for r in reps:
#         d = l[1] - r[1]
#         distance = numpy.dot(d, d)
#         print(' '.join([l[0], 'x', r[0], str(distance)]))
