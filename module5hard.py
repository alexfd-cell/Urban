import time
from tqdm import tqdm

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)


class Video:

    def __init__(self, title, duration, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users, videos = [], []
    curent_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.curent_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.curent_user = None

    def add(self, *args):
        for movie in args:
            self.videos.append(movie)

    def get_videos(self, world):
        list_video = []
        for video in self.videos:
            if world.lower() in video.title.lower():
                list_video.append(video.title)
        return list_video

    def watch_video(self, movie):

        if self.curent_user and self.curent_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.curent_user:
            for video in self.videos:
                if movie in video.title:
                    print('Начало видео')
                    for i in tqdm(range(1, 11)):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.curent_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')