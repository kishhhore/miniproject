import pyautogui as py
import time
import random
#write pyauto gui command to mannaly type the git command touch hello.txt , git add . , git commit -m "added hello.txt" , git push ,git pull
def start():
    # py.hotkey('ctrl', 'alt', 't')
    ran = str(random.randint(1,100))
    f= f"hello{ran}.txt"
    time.sleep(2)
    py.write(f'touch {f}')
    py.press('enter')
    time.sleep(2)
    py.write('git add .')
    py.press('enter')
    time.sleep(2)
    py.write('git commit -m "added hello.txt"')
    py.press('enter')
    time.sleep(2)
    py.write('git push')
    py.press('enter')
    time.sleep(3)

    py.write(f'rm {f}')
    py.press('enter')
for i in range(1,10):
    start()
    time.sleep(1)
    print(f"iteration {i} completed")