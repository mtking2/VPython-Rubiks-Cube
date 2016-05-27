from visual import *



scene = display(title='PyCube',
                 x=0, y=0, width=800, height=800,
                 center=(0, 0, 0), background=(0, 0, 0))

def makeWalls():
    length_wall = box(material=materials.wood, pos=(0, 0, -25),
                length=55, height=25, width=5)

    floor = box(material=materials.wood, pos=(0, -15, 0),
            length=55, height=5, width=55)

    width_wall = box(material=materials.wood, pos=(-25, 0, 0),
                length=5, height=25, width=55)



def makeLights():
    scene.lights = []
    local_light(pos=(25, 15, 25), color=color.gray(0.6))
    #sphere(pos=(25, 15, 25), radius=0.5)

    local_light(pos=(-25, 15, -25), color=color.gray(0.4))
    #sphere(pos=(-15, 15, -15), radius=0.5)

    local_light(pos=(0, -12, 0), color=color.gray(0.4))
    #sphere(pos=(0, -12, 0), radius=0.5)

    local_light(pos=(0, 12, 0), color=color.gray(0.4))
    #sphere(pos=(0, 15, 0), radius=0.5)




# Map keypresses to corresponding face colors and normal vectors.
faces = {'r': (color.red, (1, 0, 0)),
         'o': (color.orange, (-1, 0, 0)),
         'y': (color.yellow, (0, 1, 0)),
         'b': ((0.2, 0.2, 0.8), (0, -1, 0)),
         'w': (color.white, (0, 0, 1)),
         'g': ((0.2, 0.8, 0.2), (0, 0, -1))}

# Create colored stickers on each face, one cubie at a time.
stickers = []
for face_color, axis in faces.values():
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            # Start with all stickers on the top face, then rotate them "down"
            # to the appropriate face.
            sticker = box(material=materials.emissive, color=face_color, pos=(x, y, 1.52),
                          length=0.9, height=0.9, width=0.03)
            cos_angle = dot((0, 0, 1), axis)
            pivot = (cross((0, 0, 1), axis) if cos_angle == 0 else (1, 0, 0))
            sticker.rotate(angle=acos(cos_angle), axis=pivot, origin=(0, 0, 0))
            stickers.append(sticker)

            back = box(color=color.gray(0.25), material=materials.plastic, pos=(x, y, 1),
                          length=1, height=1, width=1)
            back.rotate(angle=acos(cos_angle), axis=pivot, origin=(0, 0, 0))
            stickers.append(back)


#makeLights()

fps = 18

# Get keyboard moves and rotate the corresponding face.
while True:
    key = scene.kb.getkey()
    if key.lower() in faces:
        face_color, axis = faces[key.lower()]
        angle = ((pi / 2) if key.isupper() else -pi / 2)
        for r in arange(0, angle, angle / fps):
            #rate(1)
            for sticker in stickers:
                if dot(sticker.pos, axis) > 0.5:
                    sticker.rotate(angle=angle/fps, axis=axis,
                                   origin=(0, 0, 0))