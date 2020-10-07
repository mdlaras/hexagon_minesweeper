import random
import turtle
import lattice
import numpy
import math

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

def count_distance(a,b):
    distance = math.sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2))
    return distance

class character(turtle.RawTurtle) :
    def __init__(self, *args, **kwargs):
        super(character,self).__init__(*args, **kwargs)
        self.equipped_object = 1
        self.status = "alive"
        self.position = (-100,100)
        self.shape("circle")
    
    def determine_startpos(self, tile_code):
        self.position = random.choice(list(tile_code))
        self.up()
        self.goto(self.position)
        self.down()

    def change_equipment(self, equipment):
        self.equipped_object = equipment
    
    def goto_neighbor(self, direction, tile_code):
        self.setheading(0)
        if direction == 1:
            self.left(60)
            self.up()
            self.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.pos()) < count_distance(clospos,self.pos()):
                    clospos = keys
            self.goto(clospos)
            self.down()
            self.position = clospos
        elif direction ==2:
            self.up()
            self.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.pos()) < count_distance(clospos,self.pos()):
                    clospos = keys
            self.goto(clospos)
            self.down()
            self.position = clospos
        elif direction == 3:
            self.right(60)
            self.up()
            self.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.pos()) < count_distance(clospos,self.pos()):
                    clospos = keys
            self.goto(clospos)
            self.down()
            self.position = clospos
        elif direction == 4:
            self.right(120)
            self.up()
            self.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.pos()) < count_distance(clospos,self.pos()):
                    clospos = keys
            self.goto(clospos)
            self.down()
            self.position = clospos
        elif direction == 5:
            self.right(180)
            self.up()
            self.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.pos()) < count_distance(clospos,self.pos()):
                    clospos = keys
            self.goto(clospos)
            self.down()
            self.position = clospos
        elif direction == 6:
            self.left(120)
            self.up()
            self.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.pos()) < count_distance(clospos,self.pos()):
                    clospos = keys
            self.goto(clospos)
            self.down()
            self.position = clospos

class identifier():
    def __init__(self, canvas_name):
        self.counter = 0
        self.turtle = turtle.RawTurtle(canvas_name)
        self.position = (0,0)
        self.turtle.hideturtle()
        self.turtle.up()

    def goto_neighbor(self, direction, tile_code):
        self.turtle.setheading(0)
        self.turtle.up()
        if direction == 1:
            self.turtle.up()
            self.turtle.left(60)
            self.turtle.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.turtle.pos()) < count_distance(clospos,self.turtle.pos()):
                    clospos = keys
            self.turtle.goto(clospos)
            self.turtle.down()
            self.turtle.up()
            self.turtle.position = clospos
        elif direction ==2:
            self.turtle.up()
            self.turtle.forward(38)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.turtle.pos()) < count_distance(clospos,self.turtle.pos()):
                    clospos = keys
            self.turtle.goto(clospos)
            self.turtle.down()
            self.turtle.up()
            self.turtle.position = clospos
        elif direction == 3:
            self.turtle.up()
            self.turtle.right(60)
            self.turtle.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.turtle.pos()) < count_distance(clospos,self.turtle.pos()):
                    clospos = keys
            self.turtle.goto(clospos)
            self.turtle.down()
            self.turtle.up()
            self.turtle.position = clospos
        elif direction == 4:
            self.turtle.up()
            self.turtle.right(120)
            self.turtle.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.turtle.pos()) < count_distance(clospos,self.turtle.pos()):
                    clospos = keys
            self.turtle.goto(clospos)
            self.turtle.down()
            self.turtle.up()
            self.turtle.position = clospos
        elif direction == 5:
            self.turtle.right(180)
            self.turtle.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.turtle.pos()) < count_distance(clospos,self.turtle.pos()):
                    clospos = keys
            self.turtle.goto(clospos)
            self.turtle.down()
            self.turtle.up()
            self.turtle.position = clospos
        elif direction == 6:
            self.turtle.left(120)
            self.turtle.forward(40)
            clospos = (900,900)
            for keys in tile_code.keys():
                if count_distance(keys,self.turtle.pos()) < count_distance(clospos,self.turtle.pos()):
                    clospos = keys
            self.turtle.goto(clospos)
            self.turtle.down()
            self.turtle.up()
            self.turtle.position = clospos

    def count_danger(self,character,tile_code):
        self.counter = 0
        self.turtle.up()
        self.turtle.goto(character.position)
        for i in range(1,7):
            self.goto_neighbor(i, tile_code)
            temp_pos = self.turtle.pos()
            condition = tile_code[temp_pos] 
            if (condition - character.equipped_object)%5 == 1:
                self.counter = self.counter + 1
        return self.counter

    def determine_live(self,character,tile_code):
        position = character.position
        if (tile_code[position] - character.equipped_object)%5 == 1:    
            character.status="dead"
        else :
            character.status="alive"
