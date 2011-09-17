import unittest
import gameoflife as gol

class TestGameOfLife(unittest.TestCase):
  
  def setUp(self):
    self.cells = [ gol.Cell(1,1), gol.Cell(1,2), 
                    gol.Cell(2,1), gol.Cell(2,2) ]

  def test_get_neighbours( self ):
    nbours = gol.Neighbours( gol.Cell( 0,0 ), self.cells )
    self.assertEqual( nbours.total_neighbours(), 1 )


  def test_underpopulation_rule( self ):
    cell = gol.Cell( 0, 0 )
    gen_manager = gol.GenerationManager()
    gen_manager.current_generation = self.cells
    gen_manager.apply_rules()
    self.assertNotIn( cell, gen_manager.current_generation )

  def test_get_dead_cells( self ):
    current_cell = gol.Cell( 1,1 )
    gen_manager = gol.GenerationManager()
    gen_manager.current_generation = self.cells
    gen_manager.current_cell = current_cell
    deadCells = gen_manager.getDeadCells() 
    self.assertEqual( [ gol.Cell( 0,0), gol.Cell( 0,1), gol.Cell( 0,2), gol.Cell( 1,0), gol.Cell( 2,0) ]

if __name__ == '__main__': 
  unittest.main()
