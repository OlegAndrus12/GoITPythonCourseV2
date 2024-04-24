import shutil

# Копіюємо файл
source_file = 'source/netflix.jpg'
destination_dir = 'target/'
shutil.move(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = 'source/icons'
destination_dir = 'target/data/'
shutil.move(source_dir, destination_dir)
