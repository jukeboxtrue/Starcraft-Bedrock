from pyexpat import model
from turtle import position
from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from perlin_noise import PerlinNoise
from numpy import floor

app = Ursina()

jukebox = FirstPersonController()

boxes = []

def input(key):
    if key == "escape":
        exit()

noise = PerlinNoise(octaves=1, seed = 333)

# Sky(texture="end")

# for z in range(20):
    # for x in range(20):
    #       box = Button(model = "cube",
    #       position = (x,100,z),
    #       color = color.white10,
    #       texture = "glass",
    #       highlight_color = color.white,
    #       parent = scene)
    #       boxes.append(box) 
    #       Collider="none"

# for z in range(20):
#     for x in range(20):
#           box = Button(model = "cube",
#           position = (x,-80,z),
#           color = color.white,
#           texture = "bedrock",
#           highlight_color = color.white,
#           parent = scene)
#           boxes.append(box)  
#           collider=False
 
Sky_texture = load_texture("end")

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "cube",
            texture = Sky_texture,
            scale = 1000,
            double_sided = True,
            collider = 'cube'
            )

# tree
endstone = Entity(model="cube", color=color.white,texture="endstone",collider = "cube", x = 10, z = 7, y = 0)
ewood = Entity(model="cube", color=color.white,texture="ender wood",collider = "cube", x = 10, z = 7, y = 1)
ewood = Entity(model="cube", color=color.white,texture="ender wood", collider = "cube", x = 10, z = 7, y = 2)
ewood = Entity(model="cube", color=color.white,texture="ender wood", collider = "cube", x = 10, z = 7, y = 3)
ewood = Entity(model="cube", color=color.white,texture="ender wood", collider = "cube", x = 10, z = 7, y = 4)
ewood = Entity(model="cube", color=color.white,texture="ender wood", collider = "cube", x = 10, z = 7, y = 5)
ewood = Entity(model="cube", color=color.white,texture="ender wood", collider = "cube", x = 10, z = 7, y = 6)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 10, z = 7, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 11, z = 7, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 9, z = 7, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 10, z = 8, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 10, z = 6, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 10, z = 7, y = 8)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 11, z = 8, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 9, z = 6, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 11, z = 6, y = 7)
eleaves = Entity(model="cube", color=color.white,texture="end leaves", collider = "cube", x = 9, z = 8, y = 7)

# chorus
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 16, z = 12, y = 1, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 16, z = 12, y = 1.7, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 16, z = 12, y = 2.4, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 16, z = 12, y = 3.1, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 16, z = 12, y = 3.8, scale = 0.7)
chorus_flower = Entity(model="cube", color=color.white,texture="chorus_flower", collider = "cube", x = 16, z = 12, y = 4.6)

chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 20, z = 12, y = 1, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 20, z = 12, y = 1.7, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 20, z = 12, y = 2.4, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 20, z = 12, y = 3.1, scale = 0.7)
chorus = Entity(model="cube", color=color.white,texture="chorus", collider = "cube", x = 20, z = 12, y = 3.8, scale = 0.7)
chorus_flower = Entity(model="cube", color=color.white,texture="chorus_flower", collider = "cube", x = 20, z = 12, y = 4.6)

# ores
enderite = Entity(model="cube", color=color.white,texture="enderite ore", collider = "cube", x = 5, z = 4, y = 0)
enderite = Entity(model="cube", color=color.white,texture="enderite ore", collider = "cube", x = 5, z = 3, y = 1)
enderite = Entity(model="cube", color=color.white,texture="enderite ore", collider = "cube", x = 5, z = 5, y = 2)
enderite = Entity(model="cube", color=color.white,texture="enderite ore", collider = "cube", x = 1, z = 2, y = 3)

boxW = 30

freq = 20
amp = 5

for i in range(boxW*boxW):
    t = Entity(model="cube", color = color.white, texture = "endstone", collider="box")
    t.x = floor(i/boxW)
    t.z = floor(i%boxW)
    t.y = floor((noise([t.x/freq, t.z/freq]))*amp)

# box + boxW

window.fullscreen = True
window.title = 'Starcraft alpha'               
window.borderless = False
scene.fog_color = rgb(120, 33, 173)
scene.fog_density = 0.001
window.fps_counter.enabled = True
jukebox.cursor.visible = True
jukebox.gravity = 0.01
jukebox.jump_height = 6
jukebox.cursor.color = color.red
jukebox.cursor.model = "circle"
# jukebox.speed = 2
jukebox.y = 10
jukebox = HealthBar(20)

sky = Sky()

app.run()