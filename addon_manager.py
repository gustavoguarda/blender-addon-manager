import bpy
import os
import sys

def backup_addons(file_path):
    enabled_addons = [addon.module for addon in bpy.context.preferences.addons]
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        for addon in enabled_addons:
            file.write(f"{addon}\n")
    print(f"Backup of enabled addons saved to {file_path}")

def restore_addons(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            addons = file.readlines()
        for addon in addons:
            addon_name = addon.strip()
            if addon_name:
                bpy.ops.preferences.addon_enable(module=addon_name)
        # Save preferences to ensure changes are applied
        bpy.ops.wm.save_userpref()
        print("Addons restored from backup.")
    else:
        print(f"Backup file not found at {file_path}")

if __name__ == "__main__":
    args = sys.argv[sys.argv.index("--") + 1:]  # Capture arguments after "--"
    
    if len(args) < 1:
        print("Usage: blender --background --python script.py -- [backup|restore] [--file <path>]")
        sys.exit(1)

    operation = args[0]
    file_path = os.path.expanduser("~/blender-addon-manager/backup_file.txt")

    if len(args) > 1 and args[1] == "--file":
        if len(args) > 2:
            file_path = args[2]
        else:
            print("No file path provided for --file option")
            sys.exit(1)

    print(f"Operation: {operation}")
    print(f"File Path: {file_path}")

    if operation == 'backup':
        backup_addons(file_path)
    elif operation == 'restore':
        restore_addons(file_path)
    else:
        print(f"Unknown operation: {operation}")
