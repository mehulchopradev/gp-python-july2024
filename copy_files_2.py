'''
- take the source file from where we want to copy the contents, as user input
- take the destination folder where the copied file should be created, as user input
- validate both the source file and destination folder
- perform copying operation
'''
from pathlib import Path
from shutil import copyfile

source_file = input('enter path of file to copy: ')
destination_folder = input('enter path of destionation folder for the copied file: ')

source_file_path = Path(source_file)
destination_folder_path = Path(destination_folder)

if not source_file_path.exists() or source_file_path.is_dir():
  print('please enter proper source file path')
elif not destination_folder_path.exists() or not destination_folder_path.is_dir():
  print('Destination path must exist and must be a directory')
else:
  copyfile(src=source_file_path, dst=destination_folder_path.joinpath(source_file_path.name))
  print('Copying done!')