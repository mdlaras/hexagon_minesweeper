import random
import turtle
import lattice
import numpy

def code_tiles(lattice_arr):
    container = {}
    for i in range(len(lattice_arr.arrmat)):
        container[i] = {}
        for j in range(lattice_arr.arrmat[i][0]):
            tile_property = random.randint(1,5)
            container[i][j] = (lattice_arr.tile_coordinates[i][j],tile_property)
    
    tile_code = {}
    for i in range(len(container)):
        for j in range(len(container[i])):
            coordinates = container[i][j][0]
            tile_code[coordinates] = container[i][j][1]
    return tile_code

class character(turtle.Turtle) :
    def __init__(self, *args, **kwargs):
        super(character,self).__init__(*args, **kwargs)
        self.equipped_object = None
        self.status = "alive"
        self.position = (0,0)
    
    def determine_startpos(self, tile_code):
        posrow = random.randint(0,len(tile_code))
        poscol = random.randint(0,len(tile_code[posrow]))
        self.position = (tile_code[posrow][poscol][2])

    def change_equipment(self, equipment):
        self.equipped_object = equipment
    
    def goto(self, direction):
        self.setheading(0)
        if direction == 1:
            self.left(60)
            self.forward(20)
            self.position = self.pos()
        elif direction ==2:
            self.forward(20)
            self.position = self.pos()
        elif direction == 3:
            self.right(60)
            self.forward(20)
            self.position = self.pos()
        elif direction == 4:
            self.right(120)
            self.forward(20)
            self.position = self.pos()
        elif direction == 5:
            self.right(180)
            self.forward(20)
            self.position = self.pos()
        elif direction == 6:
            self.left(120)
            self.forward(20)
            self.position = self.pos()

class identifier():
    def __init__(self):
        self.counter = 0
        self.turtle = turtle.Turtle()
        self.position = (0,0)

    def goto(self, direction):
        self.turtle.setheading(0)
        if direction == 1:
            self.turtle.left(60)
            self.turtle.forward(20)
            self.position = self.turtle.pos()
        elif direction ==2:
            self.turtle.forward(20)
            self.turtle.position = self.turtle.pos()
        elif direction == 3:
            self.turtle.right(60)
            self.turtle.forward(20)
            self.turtle.position = self.turtle.pos()
        elif direction == 4:
            self.turtle.right(120)
            self.turtle.forward(20)
            self.position = self.turtle.pos()
        elif direction == 5:
            self.turtle.right(180)
            self.turtle.forward(20)
            self.position = self.turtle.pos()
        elif direction == 6:
            self.turtle.left(120)
            self.turtle.forward(20)
            self.position = self.turtle.pos()

    def count_danger(self,character,tile_code):
        self.turtle.goto(character.position)
        for i in range(1,7):
            self.turtle.goto(i)
            temp_pos = self.turtle.pos()
            condition = tile_code[temp_pos] 
            if abs(condition%5 - character.equipped_object%5) == 1:
                self.counter = self.counter + 1

    def determine_live(self,character,tile_code):
        position = character.position
        if abs(tile_code[position]%5 - character.equipped_object%5) == 1:    
            character.status="dead"
