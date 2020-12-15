
class Light:

    def __init__(self, light_id, status):
        self.id = light_id
        self.name = status['name']
        self.on = status['state']['on']
        self.bri = status['state']['bri']
        self.hue = status['state']['hue']
        self.sat = status['state']['sat']
        self.xy = status['state']['bri']
        self.ct = status['state']['ct']
        self.effect = status['state']['effect']
        self.alert = status['state']['alert']
        self.colormode = status['state']['colormode']
        self.mode = status['state']['mode']
        self.reachable = status['state']['reachable']

    def __repr__(self):
        return f'<{self.__class__.__name__}("{self.name}", {self.id})>'
