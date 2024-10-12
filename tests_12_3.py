import unittest
from Runner_module import Runner, Tournament
#--------------------------------------------------------------------------------------------

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj1 = Runner('Horse')
        for i in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj2 = Runner('Antelope')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj3 = Runner('Eagle')
        obj4 = Runner('Kite')
        for i in range(10):
            obj3.run()
            obj4.walk()
        self.assertNotEqual(obj3.distance,obj4.distance)

#--------------------------------------------------------------------------------------------

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_1(self):
        race1_result = Tournament(90, self.run1,self.run3).start() # начинаем забег с Усейном и Ником
        self.all_results.append(race1_result)
        self.assertTrue(race1_result[max(race1_result.keys())] == 'Ник') # ожидаем увидеть вторым Ника

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_2(self):
        race2_result = Tournament(90, self.run2,self.run3).start() # начинаем забег с Андреем и Ником
        self.all_results.append(race2_result)
        self.assertTrue(race2_result[max(race2_result.keys())] == 'Ник') # ожидаем увидеть вторым Ника

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_3(self):
        race3_result = Tournament(90, self.run1, self.run2,self.run3).start() # начинаем забег всей толпой
        self.all_results.append(race3_result)
        self.assertTrue(race3_result[max(race3_result.keys())] == 'Ник') # ожидаем увидеть последним Ника

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            total = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(total)

if __name__ == '__main__':
    unittest.main()