

class CellCreator(object):
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.cells = []

  def create_life(self):
    for i in xrange(self.width):
      for j in xrange(self.height):
        if random.randint(0,1):
          self.cells.append(Cell(i,j))

class Cell(object):

  def __init__(self, i, j):
    self.i = i
    self.j = j

class Neighbours(object):

  def __init__(self, cell, livecells):
    self.cell = cell
    self.livecells = livecells

  def total_neighbours(self):
    total = 0
    for livecell in self.livecells:
      if abs( livecell.i - self.cell.i ) == 1 and abs(livecell.j- self.cell.j ) == 1:
        total += 1
    return total


class GenerationManager( object ):
  
  def __init__( self, livecells ):
    #self.current_generation = livecells
    self.next_generation = []

  def 

  def iterateOverCells( ):
    for livecell in self.livecells
      deadCells = self.getDeadCells

  def apply_rules(self, neighbours):
    if neighbours == 2 or neighbours == 3:
      self.next_generation.append(self.current_cell)


