#Floor Plan cost
# Calculate the total cost of tile it would take to cover a floor
# plan of width and height, using a cost entered by the user.
#=======================================================

#decloare the cost of one tile

cost = 11

height = int(input("Enter the Height of the floor"))
width = int(input("Enter the Height of the floor"))

tile_height = 2
tile_width = 2
tile_area = 2*2

floor_area =  height*width

cost_area = floor_area / tile_area

print("cost of the area tileling is", cost_area*11)


