#Nicholas Boes - HW Grade Objects

class grades:
    def __init__(self, grade_type, name, score, total):
        self.__grade_type = grade_type
        self.__name = name
        self.__score = score
        self.__total = total
    def get_grade_type(self):
        return self.__grade_type
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def get_total(self):
        return self.__total