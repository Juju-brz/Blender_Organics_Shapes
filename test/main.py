import bpy
import sys
import os
import importlib

# 1. Ajouter le dossier au path
folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(folder)

# 2. Importer jujuLib
import jujuLib
importlib.reload(jujuLib)  # recharge si modifié

# 3. Récupérer l'objet actif
obj = bpy.context.active_object

# 4. Créer le node group
node_group = jujuLib.creer_cube_geo()

# 5. Ajouter le modifier
mod = obj.modifiers.new("MonCube", type='NODES')
mod.node_group = node_group

print("✅ Done !")
