import bpy
import bmesh

# Empty the scene
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all()
bpy.ops.object.delete()

bpyscene = bpy.context.scene

# Create an empty mesh and the object.
mesh = bpy.data.meshes.new('Basic_Cube')
basic_cube = bpy.data.objects.new("Basic_Cube", mesh)

# Add the object into the scene.
bpyscene.objects.link(basic_cube)
bpyscene.objects.active = basic_cube
basic_cube.select = True

# Construct the bmesh cube and assign it to the blender mesh.
bm = bmesh.new()
bmesh.ops.create_icosphere(bm, subdivisions=4, diameter=1)
bm.to_mesh(mesh)
bm.free()

for vert in mesh.vertices:
    print( 'v %f %f %f\n' % (vert.co.x, vert.co.y, vert.co.z) )

