# create a neew function who round_up de number of paint_calc
def round_up(number):
    r = round(number + 0.5)
    print(f'You will need {r} cans of paint.')
#create a function who calculate how much can you need to paint a wall
def paint_calc(height, width, cover):
    result= (height * width)/cover
    round_up(number = result)
       
#create input for height and width od the wall and keep cover constante
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
# use keyword arguments height = test_h so we van write them in any order we want
paint_calc(height= test_h, width = test_w, cover = coverage)

