import pyautogui
import random
import requests

pyautogui.PAUSE = 1.5

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()

pyautogui.hotkey('alt','tab')
#pyautogui.typewrite("#!/usr/bin/env python3\nimport time\nimport os\nimport random\nimport sys\ndef clear_console():\nif sys.platform.startswith(\'win\'):\nos.system(\"cls\")\nelif sys.platform.startswith(\'linux\'):\nos.system(\"clear\")\nelse:\nprint(\"Unable to clear terminal. Your operating system is not supported.\n\r\")\ndef resize_console(rows, cols):\nif cols < 32:\ncols = 32\nif sys.platform.startswith(\'win\'):\ncommand = \"mode con: cols={0} lines={1}\".format(cols + cols, rows + 5)\nos.system(command)\nelif sys.platform.startswith(\'linux\'):\ncommand = \"\x1b[8;{rows};{cols}t\".format(rows=rows + 3, cols=cols + cols)\nsys.stdout.write(command)\nelse:\nprint(\"Unable to resize terminal. Your operating system is not supported.\n\r\")\ndef create_initial_grid(rows, cols):\ngrid = []\nfor row in range(rows):\ngrid_rows = []\nfor col in range(cols):\nif random.randint(0, 7) == 0:\ngrid_rows += [1]\nelse:\ngrid_rows += [0]\ngrid += [grid_rows]\nreturn grid\ndef print_grid(rows, cols, grid, generation):\nclear_console()\noutput_str = \"\"\noutput_str += \"Generation {0} - To exit the program early press <Ctrl-C>\n\r\".format(generation)\nfor row in range(rows):\nfor col in range(cols):\nif grid[row][col] == 0:\noutput_str += \"  \"\nelse:\noutput_str += \"# \"\noutput_str += \"\n\r\"\nprint(output_str, end=\" \")\ndef create_next_grid(rows, cols, grid, next_grid):\nfor row in range(rows):\nfor col in range(cols):\nlive_neighbors = get_live_neighbors(row, col, rows, cols, grid)\nif live_neighbors < 2 or live_neighbors > 3:\nnext_grid[row][col] = 0\nelif live_neighbors == 3 and grid[row][col] == 0:\nnext_grid[row][col] = 1\nelse:\nnext_grid[row][col] = grid[row][col]\ndef get_live_neighbors(row, col, rows, cols, grid):\nlife_sum = 0\nfor i in range(-1, 2):\nfor j in range(-1, 2):\nif not (i == 0 and j == 0):\nlife_sum += grid[((row + i) % rows)][((col + j) % cols)]\nreturn life_sum\ndef grid_changing(rows, cols, grid, next_grid):\nfor row in range(rows):\nfor col in range(cols):\nif not grid[row][col] == next_grid[row][col]:\nreturn True\nreturn False\ndef get_integer_value(prompt, low, high):\nwhile True:\ntry:\nvalue = int(input(prompt))\nexcept ValueError:\nprint(\"Input was not a valid integer value.\")\ncontinue\nif value < low or value > high:\nprint(\"Input was not inside the bounds (value <= {0} or value >= {1}).\".format(low, high))\nelse:\nbreak\nreturn value\ndef run_game():\nclear_console()\nrows = get_integer_value(\"Enter the number of rows (10-60): \", 10, 60)\ncols = get_integer_value(\"Enter the number of cols (10-118): \", 10, 118)\ngenerations = get_integer_value(\"Enter the number of generations (1-100000): \", 1, 100000)\nresize_console(rows, cols)\ncurrent_generation = create_initial_grid(rows, cols)\nnext_generation = create_initial_grid(rows, cols)\ngen = 1\nfor gen in range(1, generations + 1):\nif not grid_changing(rows, cols, current_generation, next_generation):\nbreak\nprint_grid(rows, cols, current_generation, gen)\ncreate_next_grid(rows, cols, current_generation, next_generation)\ntime.sleep(1 / 5.0)\ncurrent_generation, next_generation = next_generation, current_generation\nprint_grid(rows, cols, current_generation, gen)\ninput(\"Press <Enter> to exit.\")\nrun_game()")

for x in range(random.randint(1,9)):
    pyautogui.typewrite("from "+str(random.choice(WORDS))[2:-1]+" import "+str(random.choice(WORDS))[2:-1]+"\n")

pyautogui.typewrite("\nclass "+str(random.choice(WORDS))[2:-1]+"("+str(random.choice(WORDS))[2:-1]+"):")

def writeMethod():
    pyautogui.typewrite("\ndef "+str(random.choice(WORDS))[2:-1]+"("+str(random.choice(WORDS))[2:-1])
    for x in range(random.randint(0, 4)):
        pyautogui.typewrite(", "+str(random.choice(WORDS))[2:-1])
    pyautogui.typewrite("):\n")

writeMethod()

"""
while true:
    resultInt = random.randint(1,101)
    if(resultInt <10):
        pyautogui.typewrite("class "+str(random.choice(WORDS))[2:-1]+"("+str(random.choice(WORDS))[2:-1]+"):\n")
"""
