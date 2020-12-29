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
    for i in range(1,9):
        a = []
        for edge in ['Top', 'Right', 'Bottom', 'Left']:
            a.append(int(get_input('Enter Piece ' + str(i) + ' ' + edge + ': ', "number")))
        pieces.append(Piece(a[0], a[1], a[2], a[3], i, i))
    return pieces
    
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
        print('\tPosition: ' + str(piece.position))
        print('\tTop: ' + str(piece.top))
        print('\tRight: ' + str(piece.right))
        print('\tBottom: ' + str(piece.bottom))
        print('\tLeft: ' + str(piece.left))
        p += 1

def sort_pieces(pieces):
    

def main():
    pieces = get_pieces()
    print_pieces(pieces)
    
main()