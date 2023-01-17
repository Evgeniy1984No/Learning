import os
import os.path

with open("text.txt", "w") as answ:
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if file.endswith(".py"):
                answ.write(current_dir + '\n')
                break


"""
______________________________________________________________________________________________________________________
"""
# result = [cur_dir for cur_dir, dirs, files in os.walk("main") if any((fl.endswith(".py")
#     for fl in files))]
#
# with open("py_dirs.txt", "w") as w:
#     w.write("\n".join(sorted(result)))
"""
______________________________________________________________________________________________________________________
"""
