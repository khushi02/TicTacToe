game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(game_map, player=0, row=0, col=0, display=False):
    if not display:
        game_map[row][col] = player
    
    print("   0  1  2")
    for count, row in enumerate(game_map):
        print(count, row)  
        
    return game_map
        
game_board(game, 2, 1, 1)