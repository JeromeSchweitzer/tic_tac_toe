import numpy as np

class TicTacToe:
	def __init__(self):
		self.board = np.zeros((3,3))

	def __repr__(self):
		board_str = ""
		for row_idx, row in enumerate(self.board):
			if row_idx:
				board_str += '-----------\n'
			for col_idx, col in enumerate(row):
				if col_idx:
					board_str += ' |'
				board_str += ' ' + ('X' if col == 1 else 'O' if col == 2 else ' ')
			board_str += '\n'
		return board_str
