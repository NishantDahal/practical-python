# bounce.py
#
# Exercise 1.5

height = 100

for i in range(10):
    new_height = 3 / 5 * height
    print(f'{i+1} {round(new_height, 4)}')
    height = new_height
