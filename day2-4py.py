# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:30:21 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
while True:
    flower=random.randrange(0,9)
    x,y,z=mc.player.getTilePos()
    
    mc.setBlock(x,y,z-1,38,flower)