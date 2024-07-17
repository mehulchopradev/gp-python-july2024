from glob import glob
# path = '/Users/mehulchopra/Desktop/Screenshot*'
path = '*.py'

file_paths = glob(pathname=path)
print(file_paths)