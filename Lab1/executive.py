from boardgame import BoardGame

class Executive:
    def __init__(self, file_name):
        self._file_name = file_name

    def file_to_list(self):
        #returns a list of boardgame objects of every boardgame from the file
        file = open(self._file_name,'r')
        bg_list = list()
        for line in file:
            line = line.strip().split('\t')
            line[0] = line[0].replace('_'," ")
            board_game = BoardGame(line[0],float(line[1]),float(line[2]),line[3],float(line[4]),float(line[5]))
            bg_list.append(board_game)
        file.close()
        return bg_list

    def print_menu(self):
        #prints menu user will see and interact with
        print("1. Print all games highest Gibbons range to lowest")
        print("2. Print all games from a year")
        print("3. Time for a game?")
        print("4. The People VS Dr. Gibbons")
        print("5. Print based on ranking")
        print("6. Exit")

    def run(self):
        #main function to run program
        run = True

        bg_list = self.file_to_list()

        while run:
            self.print_menu()
            choice = input("Enter choice number: ")
            if choice == '1':
                bg_list.sort(reverse=True)
                for game in bg_list:
                    print(game)

            elif choice == '2':
                year = input("Enter year you would like to find games from: ")
                
                for game in bg_list:
                    if game.year == year:
                        print(game)

            elif choice == '3':
                user_time = float(input("Enter time in minutes you have to play a game: "))
                for game in bg_list:
                    if user_time >= game.max_playtime:
                        print(game)

            elif choice == '4':
                rating_difference = float(input("Enter rating difference: "))
                for game in bg_list:
                    rating_difference_abs_value = abs(game.gibbons_rating - game.public_rating)
                    if rating_difference_abs_value < rating_difference:
                        print(game)
            
            elif choice == '5':
                user_ranking = float(input("Enter ranking: "))
                for game in bg_list:
                    if game.gibbons_rating >= user_ranking:
                        print(game)

            elif choice == '6':
                run = False
            else:
                print("Invalid input")
    
