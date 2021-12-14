#Name: Nicholas Boes (nboes)
#Final Problem: 2 - Classes

class teams:
    def __init__(self, name, conf, wins, loss):
        self.__name = name
        self.__conf = conf
        self.__wins = wins
        self.__loss = loss
    def get_name(self):
        return self.__name
    def get_conf(self):
        return self.__conf
    def get_wins(self):
        return self.__wins
    def get_loss(self):
        return self.__loss
    def get_win_perc(self):
        return self.__wins / (self.__wins + self.__loss)