import __builtins__
from trees import plant_trees

crop_type="trees"
def main(crop_type):
    clear()
    if crop_type == "trees":
        plant_trees()

if __name__ == "__main__":
    main(crop_type)