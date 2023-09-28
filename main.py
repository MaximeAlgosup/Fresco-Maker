# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# import numpy as np
#
# # Create a figure and a 3D axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Define colors for each face
# colors = ['red', 'green', 'blue', 'orange', 'white', 'yellow']
#
# # Create a 3x3x3 Rubik's Cube with different face colors
# for x in range(3):
#     for y in range(3):
#         for z in range(3):
#             # Define the vertices of each small cube
#             vertices = [
#                 [x, y, z],
#                 [x + 1, y, z],
#                 [x + 1, y + 1, z],
#                 [x, y + 1, z],
#                 [x, y, z + 1],
#                 [x + 1, y, z + 1],
#                 [x + 1, y + 1, z + 1],
#                 [x, y + 1, z + 1]
#             ]
#
#             # Define the faces of the small cube
#             faces = [
#                 [vertices[0], vertices[1], vertices[2], vertices[3]],
#                 [vertices[4], vertices[5], vertices[6], vertices[7]],
#                 [vertices[0], vertices[3], vertices[7], vertices[4]],
#                 [vertices[1], vertices[2], vertices[6], vertices[5]],
#                 [vertices[0], vertices[1], vertices[5], vertices[4]],
#                 [vertices[2], vertices[3], vertices[7], vertices[6]]
#             ]
#
#             # Create a Poly3DCollection for the small cube with the appropriate color
#             cube = Poly3DCollection(faces, facecolors=[colors[i] for i in range(6)], edgecolors='black')
#
#             # Add the small cube to the plot
#             ax.add_collection3d(cube)
#
# # Set axis limits
# ax.set_xlim(0, 3)
# ax.set_ylim(0, 3)
# ax.set_zlim(0, 3)
#
# # turn off/on axis
# plt.axis('off')
#
# # Show the plot
# plt.show()
from Rubiks3DViewer.Rubiks3DViewer import RubiksViewer as viewer

test = viewer()
test.set_new_pic("", "", "OOOOOOOOOBBBBBBBBBRRRRRRRRRWWWWWWWWWYYYYYYYYYGGGGGGGGG")

