import scenes

class Engine(object):
    def __init__(self, start):
        #has class from map class
        self.start = start

    #run game getting class from map
    def run(self):
        #gets class from map class method
        current_scene = self.start.opening()
        last_scene = self.start.next_scene('done')

        #runs game till won or lost
        while current_scene != last_scene:
            next_scene_name = current_scene.play()
            current_scene = self.start.next_scene(next_scene_name)

        #plays class given
        current_scene.play()

class Map(object):

    #Scenes for game
    scenes = {
        'house': scenes.House(),
        'basement': scenes.Basement(),
        'attic': scenes.Attic(),
        'kitchen': scenes.Kitchen(),
        'done': scenes.Done(),
        'knockout': scenes.Knockout()
    }

    def __init__(self, start_scene):
        #this holds a string of the scene
        self.start_scene = start_scene


    def next_scene(self, scene):
        #gets the scene class from dict
        val = Map.scenes.get(scene)
        return val

    def opening(self):
        #has the class for the engine to run
        return self.next_scene(self.start_scene)
