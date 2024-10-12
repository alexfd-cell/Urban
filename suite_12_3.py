import unittest
import tests_12_1
import tests_12_2
import tests_12_3

TestST = unittest.TestSuite()

TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestST)