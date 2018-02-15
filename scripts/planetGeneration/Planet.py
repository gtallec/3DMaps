# -*- coding: utf-8 -*-
import bpy
import bmesh

class Planet:

    def __init__(self, name, lat, lon, alts, dia):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.alts = alts
        self.dia = dia
        
    def display(self):
        bpyscene = bpy.context.scene

        # Create an empty mesh and the object.
        mesh = bpy.data.meshes.new('Earth')
        earth = bpy.data.objects.new("Earth", mesh)

        # Add the object into the scene.
        bpyscene.objects.link(earth)
        bpyscene.objects.active = earth
        earth.select = True

        # Construct the bmesh cube and assign it to the blender mesh.
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=self.lat, v_segments=self.lon, diameter=self.dia)
        bm.to_mesh(mesh)
        bm.free()
        
        # Assign altitudes to vertices
        count = 0
        for alt in self.alts:
            (mesh.vertices[count]).co += mesh.vertices[count].normal * alt
            count+=1
        
        