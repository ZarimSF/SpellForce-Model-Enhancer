# SpellForce_Mesh-Enhancer
Just a script to (maybe) improve Spellforce 1 models.

# Disclaimer:
You need other tools to do this, namely:
- Blender
- leszekd25's [spellforce_blender_plugins](https://github.com/leszekd25/spellforce_blender_plugins)
- a tool to unpack Spellforce files like leszekd25's [spellforce_data_editor](https://github.com/leszekd25/spellforce_data_editor) or elbereth's [DragonUnPACKer](https://github.com/elbereth/DragonUnPACKer/). The first is a great tool in general, but I'd recommend second if you want to do "mass-conversion".  
  
Note: Some/many (didn't have time to view through 2000 or so meshes) models don't look better or even worse than the originals. Especially sharp edges suffer a lot, and often textures look a bit weird. Also, performance may suffer quite a bit.  
  
I am not a Python-programmer, so perhaps the code is ugly ;-)

# Setup:
Import the spellforce_blender_plugins `import_skinned_msb.py` and `export_skinned_msb.py` into blender.  
I had an issue with the original files, so I edited line 616 (import_skinned_msb) to `bl_idname = "import_scene.msb_skinned"` and line 552 (export_skinned_msb) to `bl_idname = "export_scene.msb_skinned"`.  
You will also have to modify lines 6 and 7 in `sf-enhance.py` to your desired directories. Then, copy `createDirs.bat` to your output folder and execute it (just so you don't have to create the folder-hierarchy manually).

# Usage:
Using the tool of your choice, unpack following files for each model you want to edit (for those using DragonUnPACKer, the files are located in sf1.pak, sf4.pak and sf8.pak in the game's pak-folder):
- mesh (.msb)
- animation (.bor)
- texture(s) (.dds) (many models have more than one)  
  
Place them all inside a single folder.  
  
Once the prequisites are met, run  
`"C:\Program Files\Blender Foundation\Blender 2.82\blender.exe" -b -P C:\\path\\to\\script\\sf-enhance.py`  
in command line.
Note: You may have to change the path to blender.exe. Also, this is for a Windows-Computer.  
Once execution is finished (duration depends on how many files were in in the input-folder and how fast your PC is), you should see new files in your output-folder.  
If errors occure, try to understand the error messages and check if you executed above steps correctly.  
Once this is done, you will have to copy the `animation`, `skinning` and `mesh` folders into your game directory. While backupping is always good, the original game files should stay untouched in the process.

# What it does
The script simply automates the import and export process and applies the subdivision-modifier to the models. This smoothens out surfaces and adds new polygons in the process. This reduces in-game performance.  
  
To be continued...
