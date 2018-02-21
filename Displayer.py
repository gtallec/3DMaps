#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:54:37 2018

@author: antoine
"""

import bpy
import bmesh
import numpy as np
import colorsys

class Displayer:
    """ Sert a afficher dans la vue 3D Blender des planetes contenues
    dans un planetManager"""

    def __init__(self, planetManager):
        self.planetManager = planetManager


    # Affiche une planete dans la vue 3D Blender a partir de son id
    def displayPlanetById(self, planetId):

        # Recupere la planete et ses caracteristiques
        planet = self.planetManager.getPlanetById(planetId)
        latNb = planet.getLatNb()
        lonNb = planet.getLonNb()
        diameter = planet.getDiameter()
        altitudes = planet.getAltitudes()

        # Vide la scene
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all()
        bpy.ops.object.delete()

        bpyscene = bpy.context.scene

        # Cree l'objet et un mesh vide
        mesh = bpy.data.meshes.new('Earth')
        earth = bpy.data.objects.new("Earth", mesh)

        # Ajoute l'objet a la scene
        bpyscene.objects.link(earth)
        bpyscene.objects.active = earth
        earth.select = True

        # Construit la sphere bmesh et l'ajoute au mesh
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=lonNb, v_segments=latNb, diameter=diameter)
        bm.to_mesh(mesh)
        bm.free()
        self.mesh = mesh
        self.vertices = mesh.vertices

        # Reassigne les indices des sommets
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

        # Recopie les altitudes dans self.vertices
        ilat = 0
        while ilat < latNb-1:
            ilon = 0
            while ilon < lonNb:
                self.vertices[ilat][ilon].co += (self.vertices[ilat][ilon].normal)*altitudes[ilat][ilon]
                ilon+=1
            ilat+=1

        # Assigne les altitudes aux sommet du mesh
        ilat = 0
        while ilat < latNb-1:
            ilon = 0
            while ilon < lonNb:
                mesh.vertices[self.vertices[ilat][ilon].index].co = self.vertices[ilat][ilon].co
                ilon+=1
            ilat+=1

        # Affiche la topographie
        self.displayTopography(mesh)


    def displayTopography(self, mesh):
        for face in mesh.polygons:
            coordinates = face.center
            altitude = (((coordinates.x)**2 + (coordinates.y)**2 + (coordinates.z)**2)**0.5 - 12.5)*1000
