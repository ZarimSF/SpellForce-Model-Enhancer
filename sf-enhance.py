import bpy
import os
import time

# replace with your paths
dir_in = "C:\\path\\to\\input\\folder"
dir_out = "C:\\path\\to\\output\\folder"

for fn in os.listdir(dir_in):
	if fn.endswith(".msb"):
		try:
			# clear blender
			bpy.ops.object.mode_set(mode = 'OBJECT')
			bpy.ops.object.select_all(action = 'SELECT')
			bpy.ops.object.delete(use_global = False, confirm = False)
			# import file
			bpy.ops.import_scene.msb_skinned(filepath =  dir_in + "\\" + fn)
			# select model
			bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
			# add and apply subdivision
			bpy.ops.object.modifier_add(type = 'SUBSURF')
			# uncomment if you want to go crazy (up to level 6 is possible but not recommended)
			# bpy.data.objects["modelname"].modifiers["Subdivision"].levels = 2
			bpy.ops.object.modifier_apply(apply_as = 'DATA', modifier = "Subdivision")
			# prepare for export (triangulate faces)
			bpy.ops.object.mode_set(mode = 'EDIT')
			bpy.ops.mesh.quads_convert_to_tris(quad_method = 'BEAUTY', ngon_method = 'BEAUTY')
			bpy.ops.object.mode_set(mode = 'OBJECT')
			bpy.ops.export_scene.msb_skinned(filepath = dir_out + "\\" + fn)
			print(fn + " FINISHED\n")
		except:
			# for some models exporting msbs fails
			print("IndexError for file " + fn + "\n")
		continue
	else:
		continue
		
pathS = "skinning\\b20"
pathA = "animation"
pathM = "mesh"
directory = os.fsencode(dir_out)
for file in os.listdir(directory):
	fn = os.fsdecode(file)
	if fn.endswith("_SKIN.msb") or fn.endswith(".bsi"):
		# skinning\\b20
		# file modelname_SKIN.msb must manually be renamed to modelname.msb later
		os.replace(os.path.join(dir_out, fn), os.path.join(dir_out, pathS, fn))
		continue
	elif fn.endswith(".bor"):
		# animation
		os.replace(os.path.join(dir_out, fn), os.path.join(dir_out, pathA, fn))
		continue
	elif fn.endswith(".msb"):
		# mesh
		os.replace(os.path.join(dir_out, fn), os.path.join(dir_out, pathM, fn))