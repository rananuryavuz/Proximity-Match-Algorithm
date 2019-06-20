from math import sqrt

keyboard_cartesian = {'Q': {'x':0, 'y':0},
                      'W': {'x':1, 'y':0},
                      'E': {'x':2, 'y':0}, 
                      'R': {'x':3, 'y':0},
                      'T': {'x':4, 'y':0},
                      'Y': {'x':5, 'y':0},
                      'U': {'x':6, 'y':0}, 
                      'I': {'x':7, 'y':0},
                      'O': {'x':8, 'y':0},
                      'P': {'x':9, 'y':0}, 
                      'A': {'x':0, 'y':1},
                      'Z': {'x':0, 'y':2},
                      'S': {'x':1, 'y':1},
                      'x': {'x':1, 'y':2},
                      'D': {'x':2, 'y':1},
                      'C': {'x':2, 'y':2},
                      'F': {'x':3, 'y':1}, 
                      'B': {'x':4, 'y':2}, 
                      'M': {'x':5, 'y':2},
                      'J': {'x':6, 'y':1},
                      'G': {'x':4, 'y':1}, 
                      'H': {'x':5, 'y':1}, 
                      'J': {'x':6, 'y':1}, 
                      'K': {'x':7, 'y':1},
                      'L': {'x':8, 'y':1}, 
                      'V': {'x':3, 'y':2}, 
                      'N': {'x':5, 'y':2}, }

def euclidean_distance(a,b):
    X = (keyboard_cartesian[a]['x'] - keyboard_cartesian[b]['x'])**2
    Y = (keyboard_cartesian[a]['y'] - keyboard_cartesian[b]['y'])**2
    return math.sqrt(X+Y)
     
     
for i in keyboard_cartesian.keys():
    for j in keyboard_cartesian.keys():
        distance_from_i_to_j = [(i, j, euclidean_distance(i, j))]