from RubiksSolver.RubiksSolver import RubiksSolver as RSolver

pattern = [
    'B', 'B', 'B',
    'B', 'U', 'U',
    'B', 'U', 'B'
]

if __name__ == '__main__':
    
    solver = RSolver(pattern)
    cube_to_find = solver.getCenter() + "4"
    


    

   
    # print(solver)