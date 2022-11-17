import unittest
import valid_parenthsis

test_array = ["{[]{()}}","[{}{})(]","((()"]

class TestValidParenthesis(unittest.TestCase):
  
  def test_balanced(self):
      self.assertEqual(valid_parenthsis.is_valid_parenthesis(test_array[0]),True)
     
    
if __name__ == "__main__":
  unittest.main()