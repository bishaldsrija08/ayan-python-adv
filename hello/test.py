import os
import shutil
print(os.listdir())


# Rename
os.rename('test.txt', 'hello.txt')


# Make directory
os.mkdir('testdir')

# move file
shutil.move('hello.txt', 'testdir/hello.txt')

# copy file
shutil.copy('testdir/hello.txt', 'hello2.txt')

# delete file
os.remove('testdir/hello.txt')