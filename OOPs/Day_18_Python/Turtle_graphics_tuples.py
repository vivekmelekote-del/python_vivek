from turtle import Turtle, Screen
# import tkinter #tkinker colors link : https://trinket.io/docs/colors

timmy = Turtle()
class TurtleUser:
    def __init__(self):
        """Initilizes all the data"""
        self.straight = 0
        self.right = 0
        self.shape = [[3, "red", (180 - 60)], 
                 [4, "coral", (180 - 90)],
                 [5, "green", (180 - 108)],
                 [6, "blue", (180 - 120)], 
                 [7, "indigo", (180 - 128.57)],
                 [8, "white smoke", (180 - 135)],
                 [9, "purple", (180 - 140)], 
                 [10, "grey", (180 - 144)]
        ]
        self.i = 0

    def straight_call(self):
        """To move the turtle straight"""
        timmy.forward(self.straight)
        # """Get's the dashed line when turtle moves"""
        # for i in range(1, self.straight):
        #     if i % 10 == 0:
        #         timmy.forward(5)
        #         timmy.penup()
        #     else:
        #         timmy.forward(5)
        #         timmy.pendown()

    def turn(self):
        """To make turtle turn right"""
        timmy.right(self.right)

    def update_color(self):
        """Changes the colour of the turtle"""
        timmy.color(self.shape[self.i][1])

    def move_turtle(self): #Easier and simpler version of this is in try.py file
        """Move the turtle in different shapes"""
        j = 0
        change_color = False
        mooving_stop = "f"
        self.update_color()
        self.right = self.shape[0][2]
        # while(mooving_stop == 'f'):
        while(self.i <= 7):# or (mooving_stop == 'f'):
            if self.shape[self.i][0] == j:
                # self.right = self.shape[self.i][2]
                self.i += 1
                if self.i <= 7:
                    self.right = self.shape[self.i][2]
                    self.update_color()
                change_color = True
                j = 1
            else:
                j += 1
            self.straight = 100
            if self.i <= 7:
                if(self.straight != 0):
                    self.straight_call()
                if(self.right != 0):
                    self.turn()
                if(self.right == 900 or self.straight == 900):
                    mooving_stop = input("Do you want the turtle to stop mooving? T : Ture, F : False: ").lower()
                if change_color:
                    change_color = False
    
    # def move_turtle(self, straight, right):
    #     self.straight = straight
    #     self.right = right
    #     self.straight_turn()
    #     # timmy.color("red")
    #     self.right = right
    #     self.straight = straight
    #     self.semi_triangle()
    #     self.right = right
    #     self.straight = straight
    #     self.semi_triangle()
    #     self.right = right
    #     self.straight = straight
    #     self.semi_triangle()

    def create_screen_and_turtle(self):
        """Give shape to turtle"""
        timmy.shape("turtle")
        # timmy.color('#FF9500')
    
    def exitscreen(self):
        """Creates a screen and exits on click"""
        screen = Screen()
        screen.exitonclick()