import engine

#gives start point to map
map = engine.Map('house')

#gets class from map
game = engine.Engine(map)

#runs class provided by map with a method
game.run()
