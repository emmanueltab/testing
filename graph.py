import matplotlib as mat
points_for_triangle = {
               # x, y
    'point_a' : [0, 10], 
    'point_b' : [0, 0],
    'point_c' : [7, 0]
}


# how the right triangle looks right now. in a graph it would be in the 1st quadrant with the hypotenuse facing east
def first_triangle():
    print('''
#
#
# a  *
#    * *
#    *  *
#    *   *
#    *    *
#    *     *
#    *      *
# 10 *       *
#    *        *
#    *         *
#    *          *
#    *           *
#    *            *
#  b * * * * * * * * c
#          7
# # # # # # # # # # # # # # 1st quadrant on a graph

''')
first_triangle()
help(mat)
options = ['y', 'x']                   # x, y
a = points_for_triangle.get('point_a') # 0, 10
b = points_for_triangle.get('point_b') # 0, 0
c = points_for_triangle.get('point_c') # 7, 0
count = 0 
while True:
    rotate_which_direction = input('reflection across y axis or x axis? (enter y or x): ')
    if rotate_which_direction in options:
        if rotate_which_direction == 'y':
            # x = 0 y = 10
            a[1] = a[1] * -1 # point a
            print(a)
        elif rotate_which_direction == 'x':
            c[0] = c[0] * -1
            print(c)

    else:
        print("that isnt an option \n-------------------")
        continue