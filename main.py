import polygon_turtle as pt
import lattice
import game

drew = pt.polygon_turtle()
# a = lattice.lattice_arr(5,drew)
# a.make_arrangement()
# a.draw_arr()
arr = {0:(6,0),1:(6,0),2:(6,0)}
a = lattice.lattice_arr(6,drew,arr)

a.draw_arr()
b = game.code_tiles(a)
print(b)