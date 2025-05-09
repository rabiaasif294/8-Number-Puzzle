import copy as cp
class Node:
    def __init__(self, state, parent=None):
        # Store the node state and parent state
        self.grid = state
        self.parent = parent

    def __str__(self):
        # Implement a method to print the state of the node
        return f"{self.grid[0]}\n{self.grid[1]}\n{self.grid[2]}\n"

class PuzzleSolver:
    def __init__(self, start, goal=[[1,2,3],[4,5,6],[7,8,' ']]):
        # Initialize the puzzle with start and goal state
        self.start=Node(start)
        self.goal=Node(goal)
        if not self.is_solvable(self.start):
            print("The Puzzle in not solvable!\n")
            return
    def is_solvable (self, state):
        # Check if the puzzle state is solvable
        flatten_list=[]
        for lst in state.grid:
            flatten_list+=lst

        inversions=0
        for i in range(len(flatten_list)-1):
            for j in range(i+1,len(flatten_list)):
                if flatten_list[i]!=' ' and flatten_list[j]!=' ' and flatten_list[i]>flatten_list[j]:
                    inversions+=1
        return inversions%2==0

    def find_space(self, state):
        # Implement the method to find the position (x, y) of the empty space (' ')
        for i in range(len(state.grid)):
            for j in range(len(state.grid[0])):
                if state.grid[i][j]==' ':
                    return (i,j)

    def find_moves(self,space_pos):
        # Implement the method to generate valid moves for the empty space
        x, y  = space_pos
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def is_valid(self, move):
        # Implement the method to check if a move is within bounds of the puzzle
        if -1 in move or len(self.start.grid) in move:
            return False
        return True

    def play_move(self, state, move, space):
        # Implement the method to generate a new state after making the move
        m1,m2=move
        s1,s2=space
        new_state = cp.deepcopy(state.grid)
        new_state[m1][m2],new_state[s1][s2]=new_state[s1][s2],new_state[m1][m2]
        return Node(new_state,state)

    def generate_children(self, state):
        # Implement the method to generate all valid children from a state
        children = []
        # space = call find_space method
        space = self.find_space(state)
        # moves = call find_moves method
        moves = self.find_moves(space)

        for move in moves:
            if self.is_valid(move):
                child = self.play_move(state,move,space)
                children.append(child)
        return children


    def solve_puzzle_dfid(self,max_limit):
        # Implement the search strategy for depth-first-search with iterative deepening
        def dls ( node, depth):
            # Your code goes here
            if depth==0 and node.grid==self.goal.grid:
                return node
            if depth>0:
                if node.grid==self.goal.grid:
                    return node
                children = self.generate_children(node)
                for child in children:
                    sol= dls(child,depth-1)
                    if sol:
                        return sol
        # Call dls function iteratively and search
        for i in range(max_limit):
            res=dls(self.start,i)
            if res:
                self.disp_solution(res)
                return

        print("Solution not found! ")

    def disp_solution(self, final_state):
        # Implement the method to display the solution path

        while final_state!=None:
            print(final_state)
            print()
            final_state=final_state.parent
        return

#Run this Test-Case

def main ():
    start = [
    [1, 2, 3],
    [' ', 6, 5],
    [4, 8, 7]
]

    dfid = [
    [1, 2, 3],
    [4, ' ', 6],
    [7, 5, 8]
]


    solver = PuzzleSolver(start=dfid )
    solver.solve_puzzle_dfid(20)

main()
