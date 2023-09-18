

class FloodWalker:
    def __init__(self, maze, water_amount, starting_row, starting_col):
        self.maze = maze
        
        self.water_amount = water_amount
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        
        self.starting_row = starting_row
        self.starting_col = starting_col

        self.steps_taken = 1
        self.is_out_of_water = False
        

    def solve(self, row, col):
        #step 1: mark current pos
        self.mark(row, col)

        #step 2: check if we are out of water/ if the map is full
        if self.is_flooded():
            return True
        
        #step 3: check if next position is valid if is valid

        #down
        if self.is_valid(row+1, col):
            is_flooded = self.solve(row+1,col)

            if is_flooded:
                return True
            
        #right    
        if self.is_valid(row, col+1):
            is_flooded = self.solve(row,col+1)

            if is_flooded:
                return True
            
        #left
        if self.is_valid(row, col-1):
            is_flooded = self.solve(row,col-1)

            if is_flooded:
                return True
            
        #up
        if self.is_valid(row-1, col):
            is_flooded = self.solve(row-1,col)

            if is_flooded:
                return True
        

        

    def mark(self, row, col):
        #replace empty space with ~
        line = self.maze[row]
        
        line = list(line)
        line[col] = '~'
        line = "".join(line)
        self.maze[row] = line
        #increase amount of steps taken by 1
        self.steps_taken += 1

    def is_valid(self, row, col):
        #if the row/col given is outside of the maze
        if row < 0 or row >= self.height:
            return False
        
        elif col < 0 or col >= self.width:
            return False
        else:
            line = self.maze[row]
            #if the row/col given is a wall of a space already flooded
            if line[col] == 'H' or line[col] == '~':
                return False
            else:
                return True

    def is_flooded(self):
        #if we have traversed more stpes than the amount of water, stop the flood
        if self.steps_taken > self.water_amount:
            self.is_out_of_water = True
            return True
        else:
            return False
                    

        
    def print_output(self):
        print(f"Size: {self.height}, {self.width}")
        print(f"Starting position: {self.starting_row}, {self.starting_col}")
        for row in self.maze:
            print(row)
        if self.is_out_of_water:
            print("Flood ran out of water.")
        else:
            print("Flood complete.")

