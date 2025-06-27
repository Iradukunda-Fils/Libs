from pathlib import Path
from random import randint
import os
import shutil
import sys

# print("is directory: %(dir)s or is file: %(file)s" % {"dir": Path(__file__).is_dir(), "file": Path(__file__).is_file()})
# print("path exists: %(exists)s" % {"exists": Path(__file__).exists()})

# p = Path("project/data/report.pdf")

# p.mkdir(parents = True, exist_ok = True)

# print("Name:", p.name)
# print("Stem:", p.stem)
# print("Suffix:", p.suffix if p.suffix else "no extension")
# print("Parent:", p.parent)
# print("Parent:", p.unlink())
# print("Parent:", p.rmdir())




# shutil.rmtree(p.parent.parent) 

# os.rmdir(p.parent.parent)

# print(help(os.remove))

# print(sys.argv)
# print("The length is: %s" % len(sys.argv))
# print("The system Version is: %s and the platform is: %s" % (sys.version, sys.platform))


# sys.stdout.write("This is standard output\n")
# sys.stderr.write("This is an error!\n")

# var = "hello, World"

# print("the size of %s is %s" % (sys.getsizeof(var), var))


    
    
# print("Enter lines (blank line to stop):")

# def main():
#     count = 0

#     for line in sys.stdin:
#         line = line.strip()
#         if line == "":
#             break
#         count += 1
#         sys.stdout.write(">> %s \n" % line)
    
#     # data = sys.stdin.read()
#     # print("All input:")
#     # print(data)
    
#     print (count)
        



def resolve_path(path: str) -> Path:
    try:
        path_obj = Path(path)

        # Loop while a file with the same name exists
        while path_obj.exists() and path_obj.is_file():
            suf = randint(1, 10)
            file_name = f"{path_obj.stem}_{suf}{path_obj.suffix}"
            path_obj = path_obj.parent / file_name

        # Create the parent directory if it doesn't exist
        if not path_obj.parent.exists():
            path_obj.parent.mkdir(parents=True, exist_ok=True)
            print(f"Directory created: {path_obj.parent}")

    except Exception as e:
        print(f"Error occurred while resolving path {path_obj}: {e}")

    return path_obj




# if __name__ == "__main__":
#     main()