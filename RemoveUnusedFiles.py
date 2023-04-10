import os

print("Type DEMO to do a simulation (wont change anything)")
print("Type YES to proceed\n")
choice = input("Choice: ")

# Newline because why not?
print()

excluded_files = [
    "RemoveUnusedFiles.py",
]
    
excluded_extensions = [
    "mp3"
]

for root, directories, files in os.walk("."):
    for file in files:
        # Checks for excluded extensions/files
        if file in excluded_files: break
        for excluded_extension in excluded_extensions:
            if excluded_extension in file: break

            # Removes the file if its in root
            if os.path.isfile(file):
                if choice == "DEMO":
                    print(f"File that would be deleted (root directory): {file}")

                else:
                    os.remove(file)

            # Else removes the file in its specific directory
            else:
                file_path = os.path.join(root, file)

                if choice == "DEMO":
                    print(f"File that would be deleted: {file}")

                else:
                    os.remove(file_path)

input("\nOK! Press ENTER to exit")