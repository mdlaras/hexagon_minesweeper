import random
import turtle

def code_tiles(lattice_arr):
    tile_code = {}
    for i in range(len(lattice_arr)):
        for j in range(lattice_arr[i][0]):
            tile_property = random.randint(1,5)
            tile_code[i][j] = (i,j,tile_property)

class character(turtle.Turtle) :
    def __init__(self, *args, **kwargs):
        super(character,self).__init__(*args, **kwargs)
        self.equipped_object = None
    
    def change_equipment(self, equipment):
        self.equipped_object = equipment
    
    def goto(self, direction):
        self.setheading(0)
        if direction == 1:
            self.left(60)
            self.forward(20)
        elif direction ==2:
            self.forward(20)
        elif direction == 3:
            self.right(60)
            self.forward(20)
        elif direction == 4:
            self.right(120)
            self.forward(20)
        elif direction == 5:
            self.right(180)
            self.forward(20)
        elif direction == 6:
            self.left(120)
            self.forward(20)
