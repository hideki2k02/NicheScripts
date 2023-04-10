import os
import json

from pathlib import Path

def get_dimensions(ftb_chunks_world_folder):
    # Opens up the dimensions file and check the waypoints inside it
    with open( os.path.normpath(f"{ftb_chunks_world_folder}/dimensions.txt"), "r" ) as dimensions_file:
        output_array = []

        for dimension in dimensions_file.readlines():
            # Removes the trailing newline
            dimension = dimension.replace("\n", "")
            
            # print(dimension)

            output_array.append(dimension)

        return output_array
    
# Main code
if __name__ == "__main__":
    # Preset for testing, you can change this if you want
    ftb_chunks_world_folder = Path(
        "/mnt/Jogos/PrismMC Data/instances/All of Fabric 6 - AOF6 (1.5.1)/minecraft/local/ftbchunks/data/ca63500a-add8-4e34-b017-88565a2da36b/"
    )

    ftb_chunks_world_name = "New World"
    voxelmap_world_name = "New World"

    # Usage
    print("Example Usage:")
    print("VoxelMap World Data Folder: C:\MultiMC\Instances\AOF-6\minecraft\local\\ftbchunks\data\ca63500a-add8-4e34-b017-88565a2da36b")
    print("VoxelMap World Name: New World")
    print("The above can also be the IP for an server\n")

    # User input
    input_ftb_chunks_world_folder = input("VoxelMap World Data Folder (leave empty for default): ")
    input_voxelmap_world_name = input("VoxelMap World Name (leave empty for default): ")
    
    print("\nType DEMO to test the program without making any changes (Recommended)")
    print("Type START to run the program (will make changes)")
    operation = input("Operation: ")

    # Newline because why not?
    print("")

    # Poor man's debug
    if input_ftb_chunks_world_folder != "":
        ftb_chunks_world_folder = Path( input_ftb_chunks_world_folder ).resolve()

    if input_voxelmap_world_name != "":
        voxelmap_world_name = input_voxelmap_world_name

    # Do not touch this
    minecraft_folder = ftb_chunks_world_folder.parents[3]
    voxelmap_file_dir = f"{minecraft_folder}/voxelmap/{voxelmap_world_name}.points"

    # Code starts here
    dimensions = get_dimensions(ftb_chunks_world_folder)
    
    for dimension in dimensions:    
        # Some workarounds
        dimension_split = dimension.split(":")

        entry_dimension = dimension_split[1]
        dimension_folder = dimension.replace(":", "_")

        # Check if waypoints.json file exists for the current dimension, if so write its content to the voxelmap_file
        # Else just ignores the current dimension
        ftb_chunks_waypoints_dir = os.path.normpath(f"{ftb_chunks_world_folder}/{dimension_folder}/waypoints.json")
        if not os.path.exists(ftb_chunks_waypoints_dir):
            break

        if operation == "DEMO":
            print(f"Current Dimension: {dimension}")
            print(f"Contains waypoints.json file: {(os.path.exists(ftb_chunks_waypoints_dir))}")

        # Opens the waypoints.json and write its content to voxelmap_file
        with open(ftb_chunks_waypoints_dir) as ftb_chunks_waypoints_file:
            waypoints_json = json.load(ftb_chunks_waypoints_file)

            if operation == "DEMO":
                print(f"Total waypoints:", len(waypoints_json["waypoints"]), "\n")

            for waypoint in waypoints_json["waypoints"]:
                name = waypoint["name"]
                x = waypoint["x"]
                y = waypoint["y"]
                z = waypoint["z"]

                waypoint_entry = f"name:{name},x:{x},z:{z},y:{y},enabled:true,red:0.3928597,green:0.7754962,blue:0.66980565,suffix:,world:,dimensions:{entry_dimension}#"
                # print(waypoint_entry)

                if operation == "DEMO":
                    print(f"""Adding waypoint "{name}" to the VoxelMap file "{voxelmap_file_dir}" """)
                    print(f"Coordinate X: {x}")
                    print(f"Coordinate Y: {y}")
                    print(f"Coordinate Z: {z}\n")

                else:
                    with open( os.path.normpath(voxelmap_file_dir), "a" ) as voxelmap_file:
                        voxelmap_file.write(f"{waypoint_entry}\n")

    input("OK! Press ENTER to exit")
            

