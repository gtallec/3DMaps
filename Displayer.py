#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:54:37 2018

@author: antoine
"""

import bpy
import bmesh
import numpy as np

class Displayer:
    
    def __init__(self, planetManager):
        self.planetManager = planetManager
        
    def displayPlanetById(self, planetId):
        
        planet = self.planetManager.getPlanetById(planetId)
        latNb = planet.getLatNb()
        lonNb = planet.getLonNb()
        diameter = planet.getDiameter()
        altitudes = planet.getAltitudes()
        
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()
        
        bpyscene = bpy.context.scene
        
                # Create an empty mesh and the object.
        mesh = bpy.data.meshes.new('Earth')
        earth = bpy.data.objects.new("Earth", mesh)

        # Add the object into the scene.
        bpyscene.objects.link(earth)
        bpyscene.objects.active = earth
        earth.select = True

        # Construct the bmesh sphere and assign it to the blender mesh.
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=lonNb, v_segments=latNb, diameter=diameter)
        bm.to_mesh(mesh)
        bm.free()
        self.mesh = mesh
        self.vertices = mesh.vertices
        
        # Remap the vertices
        self.vertices = sorted(self.vertices, key = lambda vert: vert.co.z)
        self.vertices = np.delete(self.vertices, 0)
        self.vertices = np.delete(self.vertices, self.vertices.size-1)
        self.vertices.shape = ((latNb-1), lonNb)
        def triAngles(vert):
            if vert.co.y>=0:
                return vert.co.x
            else:
                return -vert.co.x-2
        for latitude in self.vertices:
            latitude = sorted(latitude, key = triAngles)
            
        # Copy altitudes into self.vertices
        ilat = 0
        while ilat < latNb-1:
            ilon = 0
            while ilon < lonNb:
                self.vertices[ilat][ilon].co += (self.vertices[ilat][ilon].normal)*altitudes[ilat][ilon]
                ilon+=1
            ilat+=1
        
        # Assign altitudes to the mesh
        ilat = 0
        while ilat < latNb-1:
            ilon = 0
            while ilon < lonNb:
                mesh.vertices[self.vertices[ilat][ilon].index].co = self.vertices[ilat][ilon].co
                ilon+=1
            ilat+=1