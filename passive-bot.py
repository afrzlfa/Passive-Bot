print("""
[*] [Passive Skill BOT by Afrizal F.A]
""")

import os, pyautogui, time
from pynput import keyboard
from concurrent.futures import ThreadPoolExecutor as t

class auto_on:

    def on_press(self, key):

        if key == keyboard.Key.f1:

            self.stop = True

    def skill(self, number, second):

        while (True):

            if self.stop == False:

                if self.done == 0:

                    self.done = 1
                    print("[+] [Skill: {}] [Delay: {}]".format(number, second))
                    pyautogui.press("{}".format(number))
                    time.sleep(second - 1)

                else:

                    if int(time.time()) > self.ok + 1:

                        self.ok = int(time.time())
                        self.done = 0

            elif self.stop == True:

                break

    def execute_combo(self, combo):

        for x in combo:

            t(max_workers=100).submit(self.skill, x, int(combo[x]))

    def __init__(self):

        listener =  keyboard.Listener(on_press=self.on_press)
        listener.start()
        self.delay = ''
        self.ok = int(time.time())
        self.done = 0
        self.stop = False
        combo = {}
        input_skill = input("[*] [Skill (Example: 1|2,3|6,2|6,4|10,5|12)] : ")
        print("\n")

        for opt in input_skill.split(","):

            skill = opt.split("|")
            combo[skill[0]] = skill[1]

        self.execute_combo(combo)

auto_on() if __name__ == "__main__" else exit()
