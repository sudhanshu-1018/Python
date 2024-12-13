import shutil

shutil.copy("welcome.mp3","wel.mp3")  # copy file
shutil.copytree("data","thor")          # copy folder
shutil.move("day8", "data/day8")      # move file or folder
shutil.rmtree("data/Day9")            # delete file or folder
