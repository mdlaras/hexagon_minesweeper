import polygon_turtle as pt
import lattice
import game
import random
import tkinter as tk 

def assemble_playground(canvas_name):
    canvas_name.delete("all")
    turtle_name = pt.raw_polygon_turtle(canvas=canvas_name)
    turtle_name.hideturtle()
    width = random.randint(3,6)
    field = lattice.lattice_arr(width,turtle_name)
    field.make_arrangement()
    field.draw_arr((-250,250))
    global tiles
    tiles = game.code_tiles(field)
    global character
    character = game.character(canvas_name)
    character.up()
    character.determine_startpos(tiles)
    global narrator
    narrator = game.identifier(canvas_name)
    narrator.count_danger(character,tiles)
    equip_label.configure(text=character.equipped_object)
    danger_count_label.configure(text=narrator.counter)
    status_label.configure(text=character.status)

def show_equipment(equipment):
    equip_label.configure(text=equipment)
    character.change_equipment(int(equipment))
    narrator.count_danger(character,tiles)
    danger_count_label.configure(text=narrator.counter)

def go_and_check(direction):
    character.goto_neighbor(direction,tiles)
    narrator.determine_live(character,tiles)
    status_label.configure(text=character.status)
    narrator.count_danger(character,tiles)
    danger_count_label.configure(text=narrator.counter)

def main():
    root = tk.Tk()
    root.title('Hexagon Minesweeper')
    Tcanvas = tk.Canvas(root)
    Tcanvas.configure(width = 800, height= 500)
    drew = pt.raw_polygon_turtle(canvas=Tcanvas)
    drew.hideturtle()
    start_button = tk.Button(root, text = "Start", command = lambda : assemble_playground(Tcanvas))
    goto1 = tk.Button(root,text="Up Right", width = 10, command = lambda: go_and_check(1))
    goto2 = tk.Button(root,text="Right", width = 10, command = lambda: go_and_check(2))
    goto3 = tk.Button(root,text="Down Right", width = 10, command = lambda: go_and_check(3))
    goto4 = tk.Button(root,text="Down Left", width = 10, command = lambda: go_and_check(4))
    goto5 = tk.Button(root,text="Left", width = 10, command = lambda: go_and_check(5))
    goto6 = tk.Button(root,text="Up Left", width = 10, command = lambda: go_and_check(6))
    equip1 = tk.Button(root,text="Equip 1", width = 10,command = lambda: show_equipment("1"))
    equip2 = tk.Button(root,text="Equip 2", width = 10, command = lambda: show_equipment("2"))
    equip3 = tk.Button(root,text="Equip 3", width = 10, command = lambda: show_equipment("3"))
    equip4 = tk.Button(root,text="Equip 4", width = 10, command = lambda: show_equipment("4"))
    equip5 = tk.Button(root,text="Equip 5", width = 10,command = lambda: show_equipment("5"))
    global equip_label
    equip_label = tk.Label(root, text = ' ')
    global danger_count_label 
    danger_count_label = tk.Label(root, text = '')
    global status_label
    status_label = tk.Label(root, text = " ")
    label_equip = tk.Label(root, text = "Equipped :")
    label_danger = tk.Label(root, text = "Danger count : ")
    start_button.grid(column=0, row = 0)
    goto1.grid(column=0, row = 1)
    goto2.grid(column=0, row = 2)
    goto3.grid(column=0,row = 3)
    goto4.grid(column=0,row = 4)
    goto5.grid(column=0,row = 5)
    goto6.grid(column=0,row = 6)
    equip1.grid(column=0,row = 7)
    equip2.grid(column=0,row = 8)
    equip3.grid(column=0,row = 9)
    equip4.grid(column=0,row = 10)
    equip5.grid(column=0,row = 11)
    Tcanvas.grid(column=1, row = 0, rowspan = 20)
    label_equip.grid(column = 0, row = 12)
    equip_label.grid(column = 0, row = 13)
    label_danger.grid(column = 0, row = 14)
    danger_count_label.grid(column = 0, row=15)
    status_label.grid(column=0, row=16)
    root.mainloop()
if __name__ == "__main__":
    main()
