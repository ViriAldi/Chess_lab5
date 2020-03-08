class Piece:
    """
    Class that represents all figures in chess game
    """
    def __init__(self, color, position):
        """
        Initializes object with color and position
        :param color: str
        :param position: Position
        """
        self.color = color
        self.position = position


class King(Piece):
    """
    Class that represents figure King
    """
    def __init__(self, color, shape, position):
        """
        Initializes object with color, shape and position
        :param color: str
        :param shape: str
        :param position: Position
        """
        super().__init__(color, position)
        self.shape = shape


class Queen(Piece):
    """
    Class that represents figure Queen
    """
    def __init__(self, color, shape, position):
        """
        Initializes object with color, shape and position
        :param color: str
        :param shape: str
        :param position: Position
        """
        super().__init__(color, position)
        self.shape = shape


class Bishop(Piece):
    """
    Class that represents figure Bishop
    """
    def __init__(self, color, shape, position):
        """
        Initializes object with color, shape and position
        :param color: str
        :param shape: str
        :param position: Position
        """
        super().__init__(color, position)
        self.shape = shape


class Pawn(Piece):
    """
    Class that represents figure Pawn
    """
    def __init__(self, color, shape, position):
        """
        Initializes object with color, shape and position
        :param color: str
        :param shape: str
        :param position: Position
        """
        super().__init__(color, position)
        self.shape = shape


class Hook(Piece):
    """
    Class that represents figure Hook
    """
    def __init__(self, color, shape, position):
        """
        Initializes object with color, shape and position
        :param color: str
        :param shape: str
        :param position: Position
        """
        super().__init__(color, position)
        self.shape = shape


class Knight(Piece):
    """
    Class that represents figure Knight
    """
    def __init__(self, color, shape, position):
        """
        Initializes object with color, shape and position
        :param color: str
        :param shape: str
        :param position: Position
        """
        super().__init__(color, position)
        self.shape = shape


class Position:
    """
    Class that represents al single position in a Chess board
    """
    def __init__(self, x: int, y: str, color: str):
        """
        Initializes object with two coordinates x and y, and with color
        :param x: int
        :param y: str
        :param color: str
        """
        self.x = x
        self.y = y
        self.color = color
        self.free = True


class Board:
    """
    Class that represents a Chess board with positions
    """
    def __init__(self, positions: list):
        """
        Initializes object with list of positions
        :param positions: list of positions
        """
        self.positions = positions[:]


class ChessSet:
    """
    Class that represents a ChessSet with a board and figures
    """
    def __init__(self, board: Board, pieces: list):
        """
        Initializes object with list of figures and Board
        :param board: Board
        :param pieces: list of figures
        """
        self.pieces = pieces
        self.board = board
