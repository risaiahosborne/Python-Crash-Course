from pathlib import Path

path = Path('Chapter 10\learning_python.txt')

#print the contents of the file two times by reading in the file once and storing its contents in a variable.

contents = path.read_text().rstrip()

lines = contents.splitlines()
for line in lines:
    print(line.replace('python', 'C++'))

python_learning = ' ' 

for line in lines:
    python_learning += line.lstrip()

print(python_learning.replace('python', 'C++'))