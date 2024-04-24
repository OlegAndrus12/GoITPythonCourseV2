import shutil

# Копіюємо файл
source_file = 'source/netflix.jpg'
destination_dir = 'target/'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = 'source/icons'
destination_dir = 'target/icons/'
shutil.copytree(source_dir, destination_dir)
