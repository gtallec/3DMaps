import bpy
import bmesh

# Empty the scene
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
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()