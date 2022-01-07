
class LightGroup:

    def __init__(self, lights):
        self.lights = lights
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.lights):
            selection = self.lights[self.index]
            self.index += 1
            return selection
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.lights[item]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.lights})'

