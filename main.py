# Code for Linear Algebra Group Project
# April 2020

""" NOT RELEVANT TO LINEAR ALGEBRA, IGNORE THIS """
from numpy import array, round
from math import cos, sin, pi
def print_matrix(matrix):
    print(round(matrix, decimals=2) + 0.)

###############################################################################
#                          RELEVANT CODE STARTS HERE                          #
###############################################################################
def rotate_around_origin(vertices_matrix, theta):
    """
    Rotate the column vectors (i.e., vertices) of the vertices matrix
    by theta radians around the z-axis.
    """
    rotation_matrix = array([[cos(theta), -sin(theta), 1, 0],
                             [sin(theta), cos(theta),  0, 0],
                             [0,          0,           1, 0],
                             [0,          0,           0, 1]])

    return rotation_matrix @ vertices_matrix # '@' symbol refers to matrix multiplication

def rotate_around_point(vertices_matrix, point, theta):
    """
    Rotate the column vectors (i.e., vertices) of the vertices matrix
    around a point by using homogeneous coordinates.

    Parameters:
        - vertices_matrix: a 4xn matrix which represents the homogeneous
            coordinates of n vertices of a 3d model
        - point: a vector in R^3 which represents the location of the
            point around which to rotate

    Return:
        - a 4xn matrix which represents the homogeneous coordinates of n
            vertices after the rotation around the point
    """
    return translate(rotate_around_origin(translate(vertices_matrix, -point), theta), point)

def translate(vertices_matrix, translation_vector):
    """
    Translate the column vectors (i.e., vertices) of the vertices matrix
    by using homogeneous coordinates.

    Parameters:
        - vertices_matrix: a 4xn matrix which represents the homogeneous
            coordinates of n vertices of a 3d model
        - translation_vector: a vector in R^3

    Return:
        - a 4xn matrix which represents the homogeneous coordinates of n
            vertices after the application of the translation vector
    """
    translation_matrix = array([[1, 0, 0, translation_vector[0]],
                                [0, 1, 0, translation_vector[1]],
                                [0, 0, 1, translation_vector[2]],
                                [0, 0, 0, 1]])

    return translation_matrix @ vertices_matrix # '@' symbol refers to matrix multiplication


if __name__ == "__main__":
    tetrahedron = array([[0, 0, 1, 1],
                         [0, 1, 0, 1],
                         [0, 1, 1, 0],
                         [1, 1, 1, 1]])

    print("Original tetrahedron, in homogeneous coordinates: ")
    print_matrix(tetrahedron)

    print("\nTranslated by 3.2 units in the x-direction and -11.8 units in the z-direction: ")
    print_matrix(translate(tetrahedron, array([3.2, 0.0, -11.8])))

    print("\nThe original tetrahedron, rotated by PI/2 radians around its center: ")
    print_matrix(rotate_around_point(tetrahedron, array([0.5, 0.5, 0.0]), theta=pi/2))

###############################################################################
#                              CODE ENDS HERE                                 #
###############################################################################
