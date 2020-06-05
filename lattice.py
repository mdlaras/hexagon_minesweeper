import numpy
import random
import polygon_turtle as pt

class lattice_arr():
    def __init__(self, width, turtle_name, arrmat = {}):
        self.width = width
        self.turtle = turtle_name
        self.arrmat = arrmat
        self.form = ["o", 0,0]
        self.kekule_count = 2
        self.tile_coordinates = {}

    def make_arrangement(self):
        form = random.randint(0,4) 
        if form == 0:
            height = random.randint(2,8)
            for i in range(height):
                self.arrmat[i] = (self.width,1)
            self.form = ["P", height,self.width]
        elif form == 1:
            height = random.randrange(3,9,2)
            if height == 3:
                self.arrmat = [(self.width,0),(self.width+1,1),(self.width,0)]
            elif height>3:
                for i in range(height//2):
                    if i%2 == 0:
                        self.arrmat[i] = (self.width,1)
                        self.arrmat[height-i-1] = (self.width,1)
                    else:
                        self.arrmat[i] = (self.width+1,0)
                        self.arrmat[height-i-1] = (self.width+1,0)
                self.arrmat[height//2] = (self.width,0)
            self.form = ["A", height, self.width]
        elif form == 2:
            height = random.randrange(3,9,2)
            if height == 3:
                self.arrmat = [(self.width,0),(self.width,0),(self.width,1)]
            elif height>3:
                for i in range(height//2):
                    self.arrmat[i] = (self.width+i,0)
                    self.arrmat[height-i-1] = (self.width+i,1)
                    middle = self.width+i
                self.arrmat[height//2] = (middle,0)
            self.form = ["B", height, self.width]
        elif form == 3:
            height = random.randrange(3,9,2)
            if height == 3:
                self.arrmat = [(self.width,0),(self.width+1,0),(self.width,1)]
            elif height>3:
                for i in range(height//2):
                    self.arrmat[i] = (self.width+i,0)
                    self.arrmat[height-i-1] = (self.width+i,1)
                    middle = self.width+i
                self.arrmat[height//2] = (middle+1,0)
            self.form = ["C", height, self.width]
        elif form == 4:
            l = random.randint(2,5)
            m = random.randint(2,5)
            for i in range(l):
                self.arrmat[i] = (self.width,0)
            for i in range(m):
                self.arrmat[i] = (self.width,1)
            self.form = ["CH", l , m, self.width]

    def draw_arr(self, firstposition):
        for i in range(len(self.arrmat)):
            self.tile_coordinates[i] = {}
            self.turtle.up()
            self.turtle.goto(firstposition)
            self.turtle.setheading(0)
            self.turtle.right(30)
            self.turtle.down()
            if self.arrmat[i][1] == 0:
                self.turtle.turn_to_neighbor(6,4)
            else:
                self.turtle.turn_to_neighbor(6,3)
            firstposition = self.turtle.pos()
            for j in range(self.arrmat[i][0]):
                self.turtle.make_polygon(6)
                self.turtle.up()
                self.turtle.right(120)
                self.turtle.forward(20)
                self.turtle.down()
                self.tile_coordinates[i][j] = self.turtle.pos()
                self.turtle.up()
                self.turtle.back(20)
                self.turtle.setheading(0)
                self.turtle.right(30)
                self.turtle.down()
                self.turtle.turn_to_neighbor(6,2)