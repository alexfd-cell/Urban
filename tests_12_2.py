import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
#--------------------------------------------------------------------------------------------

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    def test_race_1(self):
        race1_result = Tournament(90, self.run1,self.run3).start() # начинаем забег с Усейном и Ником
        self.all_results.append(race1_result)
        self.assertTrue(race1_result[max(race1_result.keys())] == 'Ник') # ожидаем увидеть вторым Ника


    def test_race_2(self):
        race2_result = Tournament(90, self.run2,self.run3).start() # начинаем забег с Андреем и Ником
        self.all_results.append(race2_result)
        self.assertTrue(race2_result[max(race2_result.keys())] == 'Ник') # ожидаем увидеть вторым Ника

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