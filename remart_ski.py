__author__ = 'hongocchau'

path_count = 0
paths = []

# check if able to move west
# - if yes, return list'index of the western point
# - if no, return empty list
def canMoveLeft(input, row, col, input_size):
    current_value = input[row][col]
    if col - 1 >= 0:
        left_value = input[row][col-1]
        if current_value > left_value:
            return [row,col-1]

    return []

# check if able to move north
# - if yes, return list'index of the northern point
# - if no, return empty list
def canMoveUp(input, row, col, input_size):
    current_value = input[row][col]
    if row - 1 >= 0:
        up_value = input[row-1][col]
        if current_value > up_value:
            return [row-1,col]

    return []

# check if able to move right
# - if yes, return list'index of the eastern point
# - if no, return empty list
def canMoveRight(input, row, col, input_size):
    current_value = input[row][col]
    if col +1 < input_size:
        right_value = input[row][col+1]
        if current_value > right_value:
            return [row,col+1]

    return []

# check if able to move south
# - if yes, return list'index of the southern point
# - if no, return empty list
def canMoveDown(input, row, col, input_size):
    current_value = input[row][col]
    if row +1 < input_size:
        down_value = input[row+1][col]
        if current_value > down_value:
            return [row+1,col]

    return []

# check if the current area is the last area of the path
# it is used to determine whether the path is complete
def checkNoMove(input,row,col,input_size):
    left = canMoveLeft(input,row,col,input_size)
    up = canMoveUp(input,row,col,input_size)
    right = canMoveRight(input,row,col,input_size)
    down = canMoveDown(input,row,col,input_size)

    if len(left) == 0 and len(up) == 0 and len(right) == 0 and len(down) == 0:
        return True
    else:
        return False

# find all possible paths for one specifc area
# return is a list of paths
# each path is represent a list of area's elevation
def pathsForOneArea(input, row, col, input_size, path):
    global paths
    global path_count
    #print(input[row][col])

    # check if can move west
    # if yes - move to western point and continue
    left = canMoveLeft(input,row,col,input_size)

    if len(left) != 0:
        path.append(input[left[0]][left[1]])
        pathsForOneArea(input,left[0],left[1],input_size, path)

    # check if can move north
    # if yes - move to northern point and continue
    up = canMoveUp(input,row,col,input_size)

    if len(up) != 0:
        path.append(input[up[0]][up[1]])
        pathsForOneArea(input,up[0],up[1],input_size, path)

    # check if can move east
    # if yes - move to eastern point and continue
    right = canMoveRight(input,row,col,input_size)

    if len(right) != 0:
        path.append(input[right[0]][right[1]])
        pathsForOneArea(input,right[0],right[1],input_size, path)

    # check if can move south
    # if yes - move to southern point and continue
    down = canMoveDown(input,row,col,input_size)

    if len(down) != 0:
        path.append(input[down[0]][down[1]])
        pathsForOneArea(input,down[0],down[1],input_size, path)

    # check if this is the final area of the path
    # if yes - add current path to global array if current path longer
    #           than existing path
    if checkNoMove(input,row,col,input_size):
        # First time
        if len(paths) == 0:
            paths.append(list(path))
            path_count = len(path)
        # paths got element
        else:
            if (len(path) > path_count):
                paths = []
                paths.append(list(path))
                path_count = len(path)
            elif (len(path) == path_count):
                paths.append(list(path))
                path_count = len(path)

    # remove the last area of the path
    #if len(path) > 0:
    path.pop()

# Calculate vertical drop of a path
def calculateDrop(input):
    if len(input) == 0:
        return 0
    else:
        first = input[0]
        last = input[len(input)-1]
        return first - last

# Find path with biggest vertical drop
def findLongestPath(input):

    longestPath = [input[0]]

    for path_count in range(1,len(input)):
        if calculateDrop(input[path_count]) == calculateDrop(longestPath[0]):
            longestPath.append(input[path_count])
        elif calculateDrop(input[path_count]) > calculateDrop(longestPath[0]):
            longestPath = [input[path_count]]

    return longestPath

input = []

def main():
    # read file into list
    with open('map.txt') as f:
        file_content = f.read().split('\n')

    for line_count in range(1,1001):
        input.append(map(int,file_content[line_count].split(' ')))

    # find longest path
    for row in range(0,1000):
        for col in range(0,1000):
            pathsForOneArea(input,row,col,1000,[input[row][col]])

    return findLongestPath(paths)

# run main()
longest_path = main()
print(longest_path)



