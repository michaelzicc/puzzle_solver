import time
import pickle
import random

#Global Variables
Trials = 0
Total_Unique_Edges = 0

class Piece:
	def __init__(self, top, right, bottom, left, id):
		self.top = top
		self.right = right
		self.bottom = bottom
		self.left = left
		self.id = id

class Puzzle:
	def __init__(self, pieces, total_unique_edges, width, height):
		self.pieces = pieces
		self.total_unique_edges = total_unique_edges
		self.width = width
		self.height = height

def rotate_piece(p):
	top = p.top
	p.top = p.left
	p.left = p.bottom
	p.bottom = p.right
	p.right = top
	
def get_puzzle():
	total_unique_edges = int(get_input('Enter Total Number of Unique Edges: ', "number"))
	width = int(get_input('Enter Width of Puzzle: ', "number"))
	height = int(get_input('Enter Height of Puzzle: ', "number"))
	pieces = []
	for i in range(1, ((width * height) + 1)):
		a = []
		for edge in ['Top', 'Right', 'Bottom', 'Left']:
			a.append(int(get_input('Enter Piece ' + str(i) + ' ' + edge + ': ', "number")))
		pieces.append(Piece(a[0], a[1], a[2], a[3], i))
	puzzle = Puzzle(pieces, total_unique_edges, width, height)
	save_puzzle(puzzle)
	return puzzle
	
def save_puzzle(puzzle):
	p_name = get_input('Enter Puzzle Name: ', "string")
	with open(p_name + '.p', 'wb') as f:
		pickle.dump(puzzle, f)

def load_puzzle():
	choice = 0
	while choice not in [1,2,3,4]:
		print('Choose Puzzle to Load:')
		print('1. Frogs')
		print('2. Hot Air Balloons')
		print('3. Flowers and Babies')
		print('4. Enter Puzzle File Manually')
		choice = int(get_input('Enter Puzzle Number: ', "number"))
	file_name = None
	if choice == 1:
		file_name = 'Frogs.p'
	elif choice == 2:
		file_name = 'HotAirBalloons.p'
	elif choice == 3:
		file_name = 'FlowerAndBabies.p'
	elif choice == 4:
		file_name = get_input('Enter Puzzle Pickle File Name (with extension): ', "string")
	
	with open(file_name, 'rb') as f:
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
		print('\tTop: ' + str(piece.top))
		print('\tRight: ' + str(piece.right))
		print('\tBottom: ' + str(piece.bottom))
		print('\tLeft: ' + str(piece.left))
		p += 1
	print('******************************')

def sort_pieces(pieces, total_number_of_pieces, width, height, x, y, prev_piece = None, curr_trial = [], curr_pieces = []):
	if not x and not y:
		print('Solved!')
		return True, curr_trial
	next_x, next_y = get_next_x_y(width, height, x, y)
	for i in range(0, total_number_of_pieces):
		rotations = 0
		piece = pieces[i]
		if piece.id in curr_pieces:
			continue
		next_piece_is_okay = True

		while next_piece_is_okay and rotations < 4:
			curr_trial.append(piece)
			curr_pieces.append(piece.id)
			match_successful = False
			
				
			if not prev_piece:
				match_successful = True
				
			if x > 1 and y > 1:
				piece_above = curr_trial[(len(curr_trial)-1)-width]
				if sides_match(prev_piece, piece) and ends_match(piece_above, piece):
					match_successful = True
				else:
					match_successful = False
			elif x > 1:
				if sides_match(prev_piece, piece):
					match_successful = True
				else:
					match_successful = False
			elif y > 1:
				piece_above = curr_trial[(len(curr_trial)-1)-width]
				if ends_match(piece_above, piece):
					match_successful = True
				else:
					match_successful = False
			else:
				print('Checked ' + str(Trials) + ' combinations so far...')
				
				
			if match_successful:
				next_piece_is_okay, curr_trial = sort_pieces(pieces, total_number_of_pieces, width, height, next_x, next_y, piece, curr_trial, curr_pieces)
				if next_piece_is_okay:
					return True, curr_trial

			curr_trial.pop()
			curr_pieces.pop()
			rotate_piece(piece)
			if not prev_piece:
				next_piece_is_okay = True
			rotations += 1
			print_and_increment_trials(curr_pieces)
	return False, curr_trial
	
def get_next_x_y(width, height, x, y):
	if x < width:
		x += 1
		return x, y
	elif y < height:
		x = 1
		y += 1
		return x, y
	else:
		return None, None
	
def sides_match(left, right):
	if left.right + right.left == Total_Unique_Edges + 1:
		return True
	else:
		return False

def write_to_file(file_path, mode, data):
	try:
		f = open(file_path, mode)
		f.write(data)
		f.close()	
	except:
		f = open(file_path, mode, encoding='utf-8')
		f.write(data)
		f.close()
		
def print_and_increment_trials(piece_ids):
	global Trials
	Trials += 1
	if time.localtime().tm_sec % 10 == 0:
		trial = str(piece_ids) + '\n'
		write_to_file('puzzle_solver_progress.txt', 'w', str(Trials))
		write_to_file('puzzle_solver_board_progress.txt', 'a+', trial)
	return

def ends_match(top, bottom):
	if top.bottom + bottom.top == 9:
		return True
	else:
		return False
		
def check_pieces(pieces):
	if sides_match(pieces[0], pieces[1]) and sides_match(pieces[1], pieces[2]) and \
	sides_match(pieces[3], pieces[4]) and sides_match(pieces[4], pieces[5]) and \
	sides_match(pieces[6], pieces[7]) and sides_match(pieces[7], pieces[8]) and \
	ends_match(pieces[0], pieces[3]) and ends_match(pieces[3], pieces[6]) and \
	ends_match(pieces[1], pieces[4]) and ends_match(pieces[4], pieces[7]) and \
	ends_match(pieces[2], pieces[5]) and ends_match(pieces[5], pieces[8]):
		print('Solution Checks Out')
		return True
	else:
		print('Solution Fails')
		return False

def main():
	choice = None
	while choice not in [1,2]:
		print('Would you like to enter a new puzzle manually or load an existing puzzle?')
		print('1. New Puzzle')
		print('2. Existing Puzzle')
		choice = int(get_input('Enter the Number of Your Choice: ', "number"))
	
	puzzle = None
	if choice == 1:
		puzzle = get_puzzle()
	if choice == 2:
		puzzle = load_puzzle()
	pieces = puzzle.pieces
	global Total_Unique_Edges 
	Total_Unique_Edges = puzzle.total_unique_edges
	#random.shuffle(pieces)
	print('Starting Board: ...')
	print_pieces(pieces)
	solution_okay = True
	solution_found, solution = sort_pieces(pieces, len(pieces), puzzle.width, puzzle.height, 1, 1)
	if solution_found:
		solution_okay = True # check_pieces(solution)
	if solution_okay:
		print('Solution Found!')
		print("Combinations Checked: " + str(Trials))
		print_pieces(solution)
	else:
		print('Solution Not Found')
	
	
main()