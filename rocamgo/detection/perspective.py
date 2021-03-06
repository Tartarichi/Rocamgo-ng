#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Rocamgo is recogniter of the go games by processing digital images with opencv.
# Copyright (C) 2012 Víctor Ramirez de la Corte <virako.9 at gmail dot com>
# Copyright (C) 2012 David Medina Velasco <cuidadoconeltecho at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from cv import GetPerspectiveTransform
from cv import WarpPerspective
from cv import CreateMat
from cv import CV_32FC1
from cv import CreateImage
from functions import get_max_edge
from functions import get_external_corners_prespective_correction


def perspective(img, corners):
    """Crea una imagen en modelo ideal del tablero dado en perspectiva.

    :Param img: imagen con el tablero en perspectiva
    :Todo: comprobar de que tipo es la imagen TODO
    :Type img: IplImage or CvMat
    :Param corners: lista de las esquinas del tablero
    :Type corners: list
    :Return: imagen en modelo ideal
    :Rtype: IplImage
    """

    corners = get_external_corners_prespective_correction(corners)
    max_edge = 480
    # The goban have a relation 15/14 height/width
    # relation = 14/15.0
    # In the sequence, the orden of corners are ul, dl, dr, ur
    corners_transf = ((0,0),(0,max_edge),(max_edge,0),(max_edge,max_edge))
    mat = CreateMat(3, 3, CV_32FC1)
    GetPerspectiveTransform( corners, corners_transf, mat)
    src = CreateImage((max_edge, max_edge), img.depth, img.nChannels)
    WarpPerspective(img, src, mat)
    return src
