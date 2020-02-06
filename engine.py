import scenes

class Engine(object):
    def __init__(self, start):
        self.start = start

    def run(self, scene):
        current_scene = self.start.opening()
        next = current_scene.enter()
        current_scene = self.start.next_scene(next)

class Map(object):
    scenes = {
        'house': scenes.House(),
        'room': scenes.Room()
    }
    def __init__(self, start_scene):
        print('1')
        self.start_scene = start_scene


    def next_scene(self, scene):
        print('2')
        val = Map.scenes.get(scene)
        return val

    def opening(self):
        print('3')
        return self.next_scene(self.start_scene)
