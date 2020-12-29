import time
import pickle
import random

class Piece:
    def __init__(self, top, right, bottom, left, position, id):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.position = position
        self.id = id

def rotate_piece(p):
    top = p.top
    p.top = p.left
    p.left = p.bottom
    p.bottom = p.right
    p.right = top
    
def get_pieces():
    pieces = []
    for i in range(1,10):
        a = []
        for edge in ['Top', 'Right', 'Bottom', 'Left']:
            a.append(int(get_input('Enter Piece ' + str(i) + ' ' + edge + ': ', "number")))
        pieces.append(Piece(a[0], a[1], a[2], a[3], i, i))
    save_pieces(pieces)
    return pieces
    
def save_pieces(puzzle):
    p_name = get_input('Enter Puzzle Name: ', "string")
    with open(p_name + '.p', 'wb') as f:
        pickle.dump(puzzle, f)

def load_pieces():
    with open('frogs.p', 'rb') as f:
        return pickle.load(f)
    
def get_input(msg, type):
    valid = False
    while not valid:
        if type == "number":
            inp = input(msg)
            if inp is None or not inp.isnumeric():
                continue
            else:
                return inp
        if type == "string":
            inp = input(msg)
            if inp is None:
                continue
            else:
                return inp
                
def print_pieces(pieces):
    p = 1
    for piece in pieces:
        print('Piece ' + str(p) + ':')
        print('\tPiece ID: ' + str(piece.id))
        print('\tPosition: ' + str(piece.position))
        print('\tTop: ' + str(piece.top))
        print('\tRight: ' + str(piece.right))
        print('\tBottom: ' + str(piece.bottom))
        print('\tLeft: ' + str(piece.left))
        p += 1
    print('******************************')

def sort_pieces(pieces):
    trials = 0
    for move in range(0,9):
        for a in range(0,9):
            a_rotations = 0
            p1 = pieces[a]
    #        print_pieces([p1])
            b_is_okay = True
            while a_rotations < 4:
                for b in range (0,9):
                    if b in [a]:
                        continue
                    b_rotations = 0
                    p2 = pieces[b]
                    c_is_okay = True
    #                print_pieces([p1,p2])
                    while b_rotations < 4 and c_is_okay:
                        if sides_match(p1, p2):
                            for c in range(0,9):
                                if c in [a,b]:
                                    continue
                                c_rotations = 0
                                p3 = pieces[c]
                                d_is_okay = True
    #                            print_pieces([p1,p2,p3])
                                while c_rotations < 4 and d_is_okay:
                                    if sides_match(p2, p3):
                                        for d in range(0,9):
                                            if d in [a,b,c]:
                                                continue
                                            d_rotations = 0
                                            p4 = pieces[d]
                                            e_is_okay = True
    #                                        input("Made it to p4...Continue?")
                                            while d_rotations < 4 and e_is_okay:
                                                if ends_match(p1, p4):
                                                    for e in range(0,9):
                                                        if e in [a,b,c,d]:
                                                            continue
                                                        e_rotations = 0
                                                        p5 = pieces[e]
                                                        f_is_okay = True
                                                        while e_rotations < 4 and f_is_okay:
                                                            if sides_match(p4,p5) and ends_match(p2,p5):
                                                                for f in range(0,9):
                                                                    if f in [a,b,c,d,e]:
                                                                        continue
                                                                    f_rotations = 0
                                                                    p6 = pieces[f]
                                                                    g_is_okay = True
                                                                    while f_rotations < 4 and g_is_okay:
                                                                        if sides_match(p5,p6) and ends_match(p3,p6):
                                                                            for g in range(0,9):
                                                                                if g in [a,b,c,d,e,f]:
                                                                                    continue
                                                                                g_rotations = 0
                                                                                p7 = pieces[g]
                                                                                h_is_okay = True
                                                                                while g_rotations < 4 and h_is_okay:
                                                                                    if ends_match(p4,p7):
                                                                                        for h in range(0,9):
                                                                                            if h in [a,b,c,d,e,f,g]:
                                                                                                continue
                                                                                            h_rotations = 0
                                                                                            p8 = pieces[h]
                                                                                            j_is_okay = True
                                                                                            while h_rotations < 4 and j_is_okay:
                                                                                                if sides_match(p7,p8) and ends_match(p5,p8):
                                                                                                    for j in range(0,9):
                                                                                                        if j in [a,b,c,d,e,f,g,h]:
                                                                                                            continue
                                                                                                        j_rotations = 0
                                                                                                        p9 = pieces[j]
                                                                                                        while j_rotations < 4:
                                                                                                            if sides_match(p8,p9) and ends_match(p6,p9):
                                                                                                               print('Solved after ' + str(trials) + ' tries!')
                                                                                                               solution = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
                                                                                                               return solution
                                                                                                            else:
                                                                                                                rotate_piece(p9)
                                                                                                                j_rotations += 1
                                                                                                                trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id,p4.id,p5.id,p6.id,p7.id,p8.id,p9.id)
                                                                                                    j_is_okay = False
                                                                                                else:
                                                                                                    rotate_piece(p8)
                                                                                                    h_rotations += 1
                                                                                                    trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id,p4.id,p5.id,p6.id,p7.id,p8.id)
                                                                                        h_is_okay = False
                                                                                    else:
                                                                                        rotate_piece(p7)
                                                                                        g_rotations += 1
                                                                                        trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id,p4.id,p5.id,p6.id,p7.id)
                                                                            g_is_okay = False
                                                                        else:
                                                                            rotate_piece(p6)
                                                                            f_rotations += 1
                                                                            trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id,p4.id,p5.id,p6.id)
                                                                f_is_okay = False
                                                            else:
                                                                rotate_piece(p5)
                                                                e_rotations += 1
                                                                trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id,p4.id,p5.id)
                                                    e_is_okay = False
                                                else:
                                                    rotate_piece(p4)
                                                    d_rotations += 1
                                                    trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id,p4.id)
                                        d_is_okay = False
                                    else:
                                        rotate_piece(p3)
                                        c_rotations += 1
    #                                    print_pieces([p1,p2,p3])
                                        trials = print_and_increment_trials(trials,p1.id,p2.id,p3.id)
                            c_is_okay = False
                        else:
                            rotate_piece(p2)
                            b_rotations += 1
                            trials = print_and_increment_trials(trials,p1.id,p2.id)
                rotate_piece(p1)
                a_rotations += 1
                trials = print_and_increment_trials(trials,p1.id)
            print("a is " + str(a))
        try:
            input("swapping...")
            pieces[move+1], pieces[move] = pieces[move], pieces[move+1]
        except:
            input("blah!!! " + str(trials))
            continue
        trials = print_and_increment_trials(trials)
    
def sides_match(left, right):
    if left.right + right.left == 9:
        return True
    else:
        return False

def write_to_file(file_path, mode, data):
	try:
		f = open(file_path, mode)
		f.write(data)
		f.close()	
	except:
		#log('Using UTF-8', 'warn')
		f = open(file_path, mode, encoding='utf-8')
		f.write(data)
		f.close()
        
def print_and_increment_trials(trials, p1=None,p2=None,p3=None,p4=None,p5=None,p6=None,p7=None,p8=None,p9=None):
    if time.localtime().tm_sec == 0:
       # print('Checked ' + str(trials) + ' combinations so far...')
        write_to_file('puzzle_solver_progress.txt', 'w', str(trials))
        write_to_file('puzzle_solver_board_progress.txt', 'a+', str(p1) + ', ' + str(p2) + ', ' + str(p3) + ', ' + str(p4) + ', ' + str(p5) + ', ' + str(p6) + ', ' + str(p7) + ', ' + str(p8) + ', ' + str(p9) + '\n')
    return trials + 1

def ends_match(top, bottom):
    if top.bottom + bottom.top == 9:
        return True
    else:
        return False
        
#def check_pieces(pieces):
#    if sides_match(pieces[0], pieces[1]) and sides_match(pieces[1], pieces[2]) and \
#    sides_match(pieces[3], pieces[4]) and sides_match(pieces[4], pieces[5]) and \
#    sides_match(pieces[6], pieces[7]) and sides_match(pieces[7], pieces[8]) and \
#    ends_match(pieces[0], pieces[3]) and ends_match(pieces[3], pieces[6]) and \
#    ends_match(pieces[1], pieces[4]) and ends_match(pieces[4], pieces[7]) and \
#    ends_match(pieces[2], pieces[5]) and ends_match(pieces[5], pieces[8])

def main():
    #pieces = get_pieces()
    pieces = load_pieces()
    random.shuffle(pieces)
    print('Starting Board: ...')
    print_pieces(pieces)
    solution = sort_pieces(pieces)
    print('Solution Found!')
    print_pieces(solution)
    
main()