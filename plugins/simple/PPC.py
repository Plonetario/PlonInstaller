import os, json, shutil
from tkinter import filedialog

while True:
    input("Press enter to continue")
    print("
" * 500)
    print("Welcome to PPC(Plonetario preference changer)")
    print()
    print("Available options:")
    print("1. Change the installation directory")
    print("2. Change the auto update option")
    print("3. Reset preferences(can cause system confusion)")
    choice = input("Insert the number of the option you want to choose: ")
    if choice == "1":
        print("Set your new installation directory with the new window")
        new_dir = filedialog.askdirectory(title="Set your new installation directory")
        if new_dir and os.path.isdir(new_dir):
            print("Select the data file")
            data_file = filedialog.askopenfile(
                mode="r+",
                title="Select the data file",
                filetypes=[("JSON files", "*.json")]
            )
            if data_file and (os.path.basename(data_file.name) == "PlonInstallerData.json"):
                data = json.load(data_file)
                data["dir"] = new_dir
                data_file.seek(0)
                json.dump(data, data_file)
                data_file.truncate()
                data_file.close()
            else:
                print("Invalid file")