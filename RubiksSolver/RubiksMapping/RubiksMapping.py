class RubiksMapping:
    
    def __init__(self, pattern):
        self.mapping = {}
        self.pattern = pattern

        # Crée un mappage pour chaque cube du Rubik's Cube
        for face in 'UDLRFB':
            for position in '123456789':
                cube_key = face + position
                self.mapping[cube_key] = []

                # Trouve les cubes correspondants sur les faces adjacentes
                if face == 'U':
                    if position == '1':
                        self.mapping[cube_key].extend(['L1', 'B3'])
                    elif position == '2':
                        self.mapping[cube_key].extend(['B2'])
                    elif position == '3':
                        self.mapping[cube_key].extend(['B1', 'R2'])
                    elif position == '4':
                        self.mapping[cube_key].extend(['L2'])
                    elif position == '5':
                        self.mapping[cube_key].extend([])
                    elif position == '6':
                        self.mapping[cube_key].extend(['R2'])
                    elif position == '7':
                        self.mapping[cube_key].extend(['L3', 'F1'])
                    elif position == '8':
                        self.mapping[cube_key].extend(['F2'])
                    elif position == '9':
                        self.mapping[cube_key].extend(['R1', 'F3'])
                elif face == 'D':
                    if position == '1':
                        self.mapping[cube_key].extend(['L9', 'F7'])
                    elif position == '2':
                        self.mapping[cube_key].extend(['F8'])
                    elif position == '3':
                        self.mapping[cube_key].extend(['R7', 'F9'])
                    elif position == '4':
                        self.mapping[cube_key].extend(['L8'])
                    elif position == '5':
                        self.mapping[cube_key].extend([])
                    elif position == '6':
                        self.mapping[cube_key].extend(['R8'])
                    elif position == '7':
                        self.mapping[cube_key].extend(['B9', 'L7'])
                    elif position == '8':
                        self.mapping[cube_key].extend(['B8'])
                    elif position == '9':
                        self.mapping[cube_key].extend(['B7', 'R9'])
                elif face == 'L':
                    if position == '1':
                        self.mapping[cube_key].extend(['U1', 'B3'])
                    elif position == '2':
                        self.mapping[cube_key].extend(['U4'])
                    elif position == '3':
                        self.mapping[cube_key].extend(['F1', 'U7'])
                    elif position == '4':
                        self.mapping[cube_key].extend(['B6'])
                    elif position == '5':
                        self.mapping[cube_key].extend([])
                    elif position == '6':
                        self.mapping[cube_key].extend(['F4'])
                    elif position == '7':
                        self.mapping[cube_key].extend(['B9', 'D7'])
                    elif position == '8':
                        self.mapping[cube_key].extend(['D4'])
                    elif position == '9':
                        self.mapping[cube_key].extend(['D1', 'F7'])
                elif face == 'R':
                    if position == '1':
                        self.mapping[cube_key].extend(['F3', 'U9'])
                    elif position == '2':
                        self.mapping[cube_key].extend(['U6'])
                    elif position == '3':
                        self.mapping[cube_key].extend(['U3', 'B1'])
                    elif position == '4':
                        self.mapping[cube_key].extend(['F6'])
                    elif position == '5':
                        self.mapping[cube_key].extend([])
                    elif position == '6':
                        self.mapping[cube_key].extend(['B4'])
                    elif position == '7':
                        self.mapping[cube_key].extend(['F9', 'D3'])
                    elif position == '8':
                        self.mapping[cube_key].extend(['D6'])
                    elif position == '9':
                        self.mapping[cube_key].extend(['D9', 'B7'])
                elif face == 'F':
                    if position == '1':
                        self.mapping[cube_key].extend(['U7', 'L3'])
                    elif position == '2':
                        self.mapping[cube_key].extend(['U8'])
                    elif position == '3':
                        self.mapping[cube_key].extend(['R1', 'U9'])
                    elif position == '4':
                        self.mapping[cube_key].extend(['L6'])
                    elif position == '5':
                        self.mapping[cube_key].extend([])
                    elif position == '6':
                        self.mapping[cube_key].extend(['R4'])
                    elif position == '7':
                        self.mapping[cube_key].extend(['F9', 'D3'])
                    elif position == '8':
                        self.mapping[cube_key].extend(['D6'])
                    elif position == '9':
                        self.mapping[cube_key].extend(['B7', 'D9'])
                elif face == 'B':
                    if position == '1':
                        self.mapping[cube_key].extend(['R3', 'U3'])
                    elif position == '2':
                        self.mapping[cube_key].extend(['U2'])
                    elif position == '3':
                        self.mapping[cube_key].extend(['U1', 'L1'])
                    elif position == '4':
                        self.mapping[cube_key].extend(['R6'])
                    elif position == '5':
                        self.mapping[cube_key].extend([])
                    elif position == '6':
                        self.mapping[cube_key].extend(['L4'])
                    elif position == '7':
                        self.mapping[cube_key].extend(['R9', 'D9'])
                    elif position == '8':
                        self.mapping[cube_key].extend(['D8'])
                    elif position == '9':
                        self.mapping[cube_key].extend(['D7', 'L7'])
       

    def get_adjacent_cubes(self, cube):
        # Retourne la liste des cubes situés sur les faces adjacentes au cube donné
        
        return self.mapping.get(cube, [])