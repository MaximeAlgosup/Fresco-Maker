def to_face(cube, new_face):
    """
    Solves a Rubik's Cube to match a new face configuration.

    Args:
        cube (RubiksCube): The Rubik's Cube object to be solved.
        new_face (list): A list representing the stickers of the new face configuration.

    Example:
        my_cube = RubiksCube()
        new_face = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        to_face(my_cube, new_face)
        # Solves the cube to match the specified new face configuration.

    Note:
        This method aims to solve a Rubik's Cube to match a given new face configuration. It first checks if the cube is already
        complete with the new face, and if so, it returns without making any moves. If not, it proceeds to set the edges to create
        a cross on the new face, and then sets the corners to complete the face. It uses various helper methods to achieve this.
    """
    # Check if the cube is already complete with the new face
    if is_cube_complete(cube, new_face):
        return

    # Set edges to make the cross
    for i in [1, 7, 3, 5]:
        match i:
            case 1:
                # Set the top edge color
                set_top_edge_color(cube, new_face[1])
            case 3:
                # Set the left edge color
                set_left_edge_color(cube, new_face[3])
            case 5:
                # Set the right edge color
                set_right_edge_color(cube, new_face[5])
            case 7:
                # Set the bottom edge color
                set_bottom_edge_color(cube, new_face[7])

        # Check if the cube is complete after setting an edge
        if is_cube_complete(cube, new_face):
            return

    # Set corners to finish the face
    for i in [0, 2, 6, 8]:
        match i:
            case 0:
                # Set the top-left corner color
                set_top_left_corner_color(cube, new_face[0])
            case 2:
                # Set the top-right corner color
                set_top_right_corner_color(cube, new_face[2])
            case 6:
                # Set the bottom-left corner color
                set_bottom_left_corner_color(cube, new_face[6])
            case 8:
                # Set the bottom-right corner color
                set_bottom_right_corner_color(cube, new_face[8])

        # Check if the cube is complete with the new face
        if is_cube_complete(cube, new_face):
            return


def set_top_edge_color(cube, color):
    """
    Sets the top edge sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the top edge sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_top_edge_color(my_cube, 'R')
        # Sets the top edge sticker to red.

    Note:
        The method checks if the color of the top edge sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for an edge sticker with the specified color on the top crown and executes the required moves.
    """
    if cube.get_matrix_cube()[2][1] == color:
        return True
    top_edges = cube.get_top_crown_edges()
    for edge in top_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_bottom_edge_color(cube, color):
    """
    Sets the bottom edge sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the bottom edge sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_bottom_edge_color(my_cube, 'B')
        # Sets the bottom edge sticker to blue.

    Note:
        The method checks if the color of the bottom edge sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for an edge sticker with the specified color on the bottom crown and executes the required moves.
    """
    if cube.get_matrix_cube()[2][7] == color:
        return True
    bottom_edges = cube.get_bottom_crown_edges()
    for edge in bottom_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_left_edge_color(cube, color):
    """
    Sets the left edge sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the left edge sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_left_edge_color(my_cube, 'G')
        # Sets the left edge sticker to green.

    Note:
        The method checks if the color of the left edge sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for an edge sticker with the specified color on the left crown and executes the required moves.
    """
    if cube.get_matrix_cube()[2][3] == color:
        return True
    left_edges = cube.get_left_crown_edges()
    for edge in left_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_right_edge_color(cube, color):
    """
    Sets the right edge sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the right edge sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_right_edge_color(my_cube, 'W')
        # Sets the right edge sticker to white.

    Note:
        The method checks if the color of the right edge sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for an edge sticker with the specified color on the right crown and executes the required moves.
    """
    if cube.get_matrix_cube()[2][5] == color:
        return True
    right_edges = cube.get_right_crown_edges()
    for edge in right_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_top_left_corner_color(cube, color):
    """
    Sets the color of the top-left corner sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the top-left corner sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_top_left_corner_color(my_cube, 'R')
        # Sets the top-left corner sticker to red.

    Note:
        The method checks if the color of the top-left corner sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for a corner sticker with the specified color on the top layer and executes the required moves.
    """
    if cube.get_matrix_cube()[2][0] == color:
        return True
    top_left_corners = cube.get_top_left_corners()
    for corner in top_left_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def set_top_right_corner_color(cube, color):
    """
    Sets the color of the top-right corner sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the top-right corner sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_top_right_corner_color(my_cube, 'G')
        # Sets the top-right corner sticker to green.

    Note:
        The method checks if the color of the top-right corner sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for a corner sticker with the specified color on the top layer and executes the required moves.
    """
    if cube.get_matrix_cube()[2][2] == color:
        return True
    top_right_corners = cube.get_top_right_corners()
    for corner in top_right_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def set_bottom_left_corner_color(cube, color):
    """
    Sets the color of the bottom-left corner sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the bottom-left corner sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_bottom_left_corner_color(my_cube, 'B')
        # Sets the bottom-left corner sticker to blue.

    Note:
        The method checks if the color of the bottom-left corner sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for a corner sticker with the specified color on the bottom layer and executes the required moves.
    """
    if cube.get_matrix_cube()[2][6] == color:
        return True
    bottom_left_corners = cube.get_bottom_left_corners()
    for corner in bottom_left_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def set_bottom_right_corner_color(cube, color):
    """
    Sets the color of the bottom-right corner sticker to the specified color.

    Args:
        cube (RubiksCube): The Rubik's Cube object.
        color (str): The color to set the bottom-right corner sticker to.

    Returns:
        bool: True if the sticker is successfully set to the specified color, False otherwise.

    Example:
        my_cube = RubiksCube()
        set_bottom_right_corner_color(my_cube, 'W')
        # Sets the bottom-right corner sticker to white.

    Note:
        The method checks if the color of the bottom-right corner sticker on the current cube matches the specified color.
        If they match, no moves are executed, and the method returns True.
        Otherwise, it searches for a corner sticker with the specified color on the bottom layer and executes the required moves.
    """
    if cube.get_matrix_cube()[2][8] == color:
        return True
    bottom_right_corners = cube.get_bottom_right_corners()
    for corner in bottom_right_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def is_cube_complete(cube, new_face):
    """
    Checks if the Rubik's Cube is completely solved and all stickers match the new face.

    Args:
        cube (RubiksCube): The Rubik's Cube object to check for completion.
        new_face (list): A list representing the stickers of a solved face (e.g., ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']).

    Returns:
        bool: True if the cube is complete and all stickers match the new face, False otherwise.

    Example:
        my_cube = RubiksCube()
        new_face = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
        is_complete = is_cube_complete(my_cube, new_face)
        # Checks if the cube is completely solved with a red face.

    Note:
        The method compares each sticker on the front face of the cube with the corresponding sticker in the 'new_face' list.
        If all stickers match, it returns True, indicating that the cube is solved.
    """
    return all(cube.get_matrix_cube()[2][i] == new_face[i] for i in range(9))


def moves_executor(cube, moves):
    """
    Executes a sequence of moves on a Rubik's Cube.

    Args:
        cube (RubiksCube): The Rubik's Cube object to perform the moves on.
        moves (list): A list of move commands with optional repetition count (e.g., [("U", 2), "F'", "R"]).

    Example:
        my_cube = RubiksCube()
        moves_to_execute = [("U", 2), "F'", "R"]
        moves_executor(my_cube, moves_to_execute)
        # Executes the specified sequence of moves on the cube.

    Note:
        The method takes a list of move commands as input, where each command is a tuple consisting of the move and an optional repetition count.
        It interprets and executes the moves according to the Rubik's Cube notation:
        - "U" and "U'" for the upper face and its reverse.
        - "D" and "D'" for the lower face and its reverse.
        - "L" and "L'" for the left face and its reverse.
        - "R" and "R'" for the right face and its reverse.
        - "F" and "F'" for the front face and its reverse.
        - "B" and "B'" for the back face and its reverse.
    """
    for move in moves:
        match move[0]:
            case "U":
                cube.move_u(move[1])
            case "U'":
                cube.move_u_p(move[1])
            case "D":
                cube.move_d(move[1])
            case "D'":
                cube.move_d_p(move[1])
            case "L":
                cube.move_l(move[1])
            case "L'":
                cube.move_l_p(move[1])
            case "R":
                cube.move_r(move[1])
            case "R'":
                cube.move_r_p(move[1])
            case "F":
                cube.move_f(move[1])
            case "F'":
                cube.move_f_p(move[1])
            case "B":
                cube.move_b(move[1])
            case "B'":
                cube.move_b_p(move[1])
