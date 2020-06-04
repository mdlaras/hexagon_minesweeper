import turtle

class polygon_turtle(turtle.Turtle) :
    def __init__(self, *args, **kwargs):
        super(polygon_turtle,self).__init__(*args, **kwargs)
        self.relative_position = 1
        self.direction = 'right'
        self.last_polygon = 5

    def make_polygon(self, edges):
        self.right(90)
        self.forward(20)
        deg = 360/edges
        for i in range(edges-1):
            self.right(deg)
            self.forward(20)
        self.direction = 'right'
        self.last_polygon = edges

    def make_polygon_from(self, current_edges, position):
        self.jump_to(position)
        deg = 360/self.last_polygon
        if self.direction == 'right':
            self.right(deg)
            self.forward(20)
            deg = 360/current_edges
            for i in range(current_edges-1):
                self.left(deg)
                self.forward(20)
                self.relative_position = current_edges
                self.direction = 'left'
            self.last_polygon = current_edges
        else:
            self.left(deg)
            self.forward(20)
            deg = 360/current_edges
            for i in range(current_edges-1):
                self.right(deg)
                self.forward(20)
                self.relative_position = current_edges
                self.direction = 'right'
            self.last_polygon = current_edges
        

    def jump_to(self, destination):
        edges = self.last_polygon
        deg = 360/edges
        sides_to_jump = abs(self.relative_position-destination)
        if self.direction == 'right':
            for i in range(sides_to_jump):
                self.right(deg)
                self.forward(20)
            self.relative_position = (self.relative_position + sides_to_jump)%edges
        if self.direction == 'left':
            for i in range(sides_to_jump):
                self.left(deg)
                self.forward(20)
            self.relative_position = (self.relative_position - sides_to_jump)%edges

    def turn_to_neighbor(self, edges, direction):
       if edges == 6:
            if direction == 1:
                self.penup()
                self.left(60)
                self.forward(20)
                self.left(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 2:
                self.penup()
                self.left(60)
                self.forward(20)
                self.right(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 3:
                self.penup()
                self.right(60)
                self.forward(20)
                self.left(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 4:
                self.penup()
                self.right(60)
                self.forward(20)
                self.right(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 5:
                self.penup()
                self.left(180)
                self.forward(20)
                self.left(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 6:
                self.penup()
                self.left(180)
                self.forward(20)
                self.right(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()

    def determine_neighbours(self, edges, position):
        self.goto(position)
        self.setheading(0)
        if edges == 6:
            self.right(30)
            neighborhood = {}
            for i in [1,2,3,4,5,6]:
                self.penup()
                self.turn_to_neighbor(6,i)
                self.pendown()
                self.stamp()
                neighborhood[i-1] = self.pos()
                self.penup()
                self.goto(position)
                self.setheading(0)
                self.right(30)
                self.pendown()
            self.goto(position)
            self.setheading(0)
            neighborhood = list(neighborhood.values())
            return neighborhood

class raw_polygon_turtle(turtle.RawTurtle) :
    def __init__(self, *args, **kwargs):
        super(raw_polygon_turtle,self).__init__(*args, **kwargs)
        self.relative_position = 1
        self.direction = 'right'
        self.last_polygon = 5

    def make_polygon(self, edges):
        self.right(90)
        self.forward(20)
        deg = 360/edges
        for i in range(edges-1):
            self.right(deg)
            self.forward(20)
        self.direction = 'right'
        self.last_polygon = edges

    def make_polygon_from(self, current_edges, position):
        self.jump_to(position)
        deg = 360/self.last_polygon
        if self.direction == 'right':
            self.right(deg)
            self.forward(20)
            deg = 360/current_edges
            for i in range(current_edges-1):
                self.left(deg)
                self.forward(20)
                self.relative_position = current_edges
                self.direction = 'left'
            self.last_polygon = current_edges
        else:
            self.left(deg)
            self.forward(20)
            deg = 360/current_edges
            for i in range(current_edges-1):
                self.right(deg)
                self.forward(20)
                self.relative_position = current_edges
                self.direction = 'right'
            self.last_polygon = current_edges
        

    def jump_to(self, destination):
        edges = self.last_polygon
        deg = 360/edges
        sides_to_jump = abs(self.relative_position-destination)
        if self.direction == 'right':
            for i in range(sides_to_jump):
                self.right(deg)
                self.forward(20)
            self.relative_position = (self.relative_position + sides_to_jump)%edges
        if self.direction == 'left':
            for i in range(sides_to_jump):
                self.left(deg)
                self.forward(20)
            self.relative_position = (self.relative_position - sides_to_jump)%edges

    def turn_to_neighbor(self, edges, direction):
       if edges == 6:
            if direction == 1:
                self.penup()
                self.left(60)
                self.forward(20)
                self.left(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 2:
                self.penup()
                self.left(60)
                self.forward(20)
                self.right(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 3:
                self.penup()
                self.right(60)
                self.forward(20)
                self.left(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 4:
                self.penup()
                self.right(60)
                self.forward(20)
                self.right(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 5:
                self.penup()
                self.left(180)
                self.forward(20)
                self.left(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()
            elif direction == 6:
                self.penup()
                self.left(180)
                self.forward(20)
                self.right(60)
                self.forward(20)
                self.setheading(0)
                self.pendown()

    def determine_neighbours(self, edges, position):
        self.goto(position)
        self.setheading(0)
        if edges == 6:
            self.right(30)
            neighborhood = {}
            for i in [1,2,3,4,5,6]:
                self.penup()
                self.turn_to_neighbor(6,i)
                self.pendown()
                self.stamp()
                neighborhood[i-1] = self.pos()
                self.penup()
                self.goto(position)
                self.setheading(0)
                self.right(30)
                self.pendown()
            self.goto(position)
            self.setheading(0)
            neighborhood = list(neighborhood.values())
            return neighborhood
    