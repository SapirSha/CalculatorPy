class Singleton:
    classes = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.classes:
            cls.classes[cls] = object.__new__(cls)
        return cls.classes[cls]