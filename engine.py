import scenes

class Engine(object):
    def __init__(self, start):
        self.start = start

    def run(self):
        current_scene = self.start.opening()
        last_scene = self.start.next_scene('done')
        while current_scene != last_scene:
            next_scene_name = current_scene.play()
            current_scene = self.start.next_scene(next_scene_name)
        current_scene.play()

class Map(object):
    scenes = {
        'house': scenes.House(),
        'basement': scenes.Basement(),
        'attic': scenes.Attic(),
        'kitchen': scenes.Kitchen(),
        'done': scenes.Done(),
        'knockout': scenes.Knockout()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene):
        val = Map.scenes.get(scene)
        return val

    def opening(self):
        return self.next_scene(self.start_scene)
