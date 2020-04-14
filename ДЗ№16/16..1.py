from glob import glob
import os
import shutil
from pathlib import Path

# creating new directory
os.makedirs('C:/Users/User/Desktop/my_new_dir', exist_ok=True)
p = Path('C:/Users/User/Desktop/my_new_dir')
p.mkdir(parents=True, exist_ok=True)

# moving 'Lord_of_a_Thousand_Suns
shutil.move("C:/Users/User/Downloads/Lord_of_a_Thousand_Suns.txt", 'C:/Users/User/Desktop/my_new_dir/Lord_of_a_Thousand_Suns.txt')
Path("C:/Users/User/Downloads/Lord_of_a_Thousand_Suns.txt").rename('C:/Users/User/Desktop/my_new_dir/Lord_of_a_Thousand_Suns.txt')

# copy with some patterns
need_to_copy = Path('C:/Users/User/PycharmProjects').glob("**/*.txt")
for i in need_to_copy:
    shutil.copy(str(i), 'C:/Users/User/Desktop/my_new_dir/')

path = glob('C:/Users/User/PycharmProjects/**/*.txt')
for i in path:
    shutil.copy(i, 'C:/Users/User/Desktop/my_new_dir/')

# rename
my_path = Path('C:/Users/User/Desktop/my_new_dir/2430AD.txt')
my_path.rename('C:/Users/User/Desktop/my_new_dir/re_modul.txt')
shutil.move('C:/Users/User/Desktop/my_new_dir/data1.txt', 'C:/Users/User/Desktop/my_new_dir/my_data.txt')
my_path.with_suffix('.py')

# print
print(glob('C:/Users/User/Desktop/my_new_dir/**'))
os.listdir('C:/Users/User/Desktop/my_new_dir')

# remove
shutil.rmtree('C:/Users/User/Desktop/my_new_dir')
for i in os.listdir('C:/Users/User/Desktop/my_new_dir'):
    os.remove(i)
Path.rmdir(Path('C:/Users/User/Desktop/my_new_dir'))


