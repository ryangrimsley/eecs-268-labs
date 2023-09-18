from flood_walker import FloodWalker

class Executive:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_info_from_file(self):
        file = open(self.file_name, 'r')

        maze = []
        output_list = []

        counter = 0
        for line in file:
            if counter < 2:
                line = line.strip().split(' ')
                output_list.append(line)
            else:
                new_line = ''
                for i in line:
                    if i != '\n':
                        new_line += i
                maze.append(new_line)

            counter += 1

        output_list.append(maze)
        return output_list
    
    def run(self):

        output_file = self.get_info_from_file()

        row, col = int(output_file[0][0]),int(output_file[0][1])
        my_floodwalker = FloodWalker(output_file[2],int(output_file[1][0]), row, col)

        if my_floodwalker.is_valid(row, col):
            my_floodwalker.solve(row, col)
            my_floodwalker.print_output()
            
        else:
            print("Invalid starting position")

