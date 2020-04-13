import pygame
from pygame.sprite import Sprite, Group
from pygame.rect import Rect


def load(path):
    return pygame.image.load(path).convert()


class GameSpriteGroup(Group):
    def __init__(self):
        Group.__init__(self)


class GameSprite(Sprite):
    def __init__(self, image: pygame.image, group: GameSpriteGroup):
        Sprite.__init__(self, group)
        self.image = image
        self.rect = self.image.get_rect()

def subImage(image: pygame.image, x, y, w, h):
    return image.subsurface(Rect(x, y, w, h)).convert()


def loadSpriteBank(textures: pygame.image):
    spriteBank = {}
    tilesBank = {}
    tilesBank['grass'] = subImage(textures, 177, 1, 16, 16)
    tilesBank['fullTree'] = subImage(textures, 177, 33, 16, 32)
    tilesBank['overlapTree'] = subImage(textures, 193, 1, 16, 32)

    grassPlantTiles = []
    grassPlantTiles.append(subImage(textures, 210, 18, 14, 13))
    grassPlantTiles.append(subImage(textures, 226, 17, 14, 14))
    tilesBank['grassPlant'] = grassPlantTiles

    rockTiles = []
    rockTiles.append(subImage(textures, 209, 50, 16, 14))
    rockTiles.append(subImage(textures, 225, 50, 16, 13))
    rockTiles.append(subImage(textures, 241, 49, 16, 15))
    tilesBank['rock'] = rockTiles

    grassFlowerTiles = []
    grassFlower1 = []
    grassFlower1.append(subImage(textures, 257, 33, 16, 16))
    grassFlower1.append(subImage(textures, 273, 33, 16, 16))
    grassFlower1.append(subImage(textures, 289, 33, 16, 16))
    grassFlower2 = []
    grassFlower2.append(subImage(textures, 258, 50, 16, 16))
    grassFlower2.append(subImage(textures, 274, 50, 16, 16))
    grassFlower2.append(subImage(textures, 290, 50, 16, 16))
    grassFlower3 = []
    grassFlower3.append(subImage(textures, 0, 21, 7, 4))
    grassFlower3.append(subImage(textures, 8, 21, 7, 6))
    grassFlower3.append(subImage(textures, 16, 21, 9, 8))
    grassFlowerTiles.append(grassFlower1)
    grassFlowerTiles.append(grassFlower2)
    grassFlowerTiles.append(grassFlower3)
    tilesBank['grassFlower'] = grassFlowerTiles

    grassBlocks = []
    grassBlocks.append(subImage(textures, 312, 57, 34, 37))
    grassBlocks.append(subImage(textures, 257, 55, 24, 21))
    tilesBank['grassBlock'] = grassBlocks

    # TODO
    entitiesBank = {}

    spriteBank['tiles'] = tilesBank
    spriteBank['entities'] = entitiesBank
    return spriteBank