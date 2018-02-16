# -*- coding: utf-8 -*-
import bpy
import bmesh
import numpy as np

class Planet:        
    
    def __init__(self, name, lat, lon, alts, dia):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.dia = dia
        
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
        bmesh.ops.create_uvsphere(bm, u_segments=self.lon, v_segments=self.lat, diameter=self.dia)
        bm.to_mesh(mesh)
        bm.free()
        self.mesh = mesh
        self.vertices = mesh.vertices
        
        # Remap the vertices
        self.vertices = sorted(self.vertices, key = lambda vert: vert.co.z)
        self.vertices = np.delete(self.vertices, 0)
        self.vertices = np.delete(self.vertices, self.vertices.size-1)
        self.vertices.shape = ((lat-1), lon)
        def triAngles(vert):
            if vert.co.y>=0:
                return vert.co.x
            else:
                return -vert.co.x-2
        for latitude in self.vertices:
            latitude = sorted(latitude, key = triAngles)
            
        # Copy altitudes into self.vertices
        ilat = 0
        while ilat < lat-1:
            ilon = 0
            while ilon < lon:
                print(self.vertices[ilat][ilon].normal)
                print(alts[ilat][ilon])
                self.vertices[ilat][ilon].co += (self.vertices[ilat][ilon].normal)*alts[ilat][ilon]
                ilon+=1
            ilat+=1
        
        # Assign altitudes to the mesh
        ilat = 0
        while ilat < lat-1:
            ilon = 0
            while ilon < lon:
                mesh.vertices[self.vertices[ilat][ilon].index].co = self.vertices[ilat][ilon].co
                ilon+=1
            ilat+=1