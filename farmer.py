import pyautogui, os
from time import sleep
from random import randrange

workingDir = os.getcwd()
codeDir = "code"
codePath = os.path.join(workingDir, codeDir)

print("What language do you want to farm?")
print("Use extentions only. (py, js, any extension)")
selectedExtension = input("\n")
firstLetter = selectedExtension[0]
fileName = f"{selectedExtension}.txt"

def find_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            return file_path

    return None

codePath = os.path.join(codePath, firstLetter)
foundFile = find_file(codePath, f"{selectedExtension}.{selectedExtension}")

print(f"{workingDir}.{selectedExtension}_farmer.{selectedExtension}")

if foundFile:
    # def read_file(filePath):
    #     try:
    #         with open(filePath, 'r', encoding="utf-8") as file:
    #             file_contents = file.read()
    #             return file_contents
    #     except Exception as e:
    #         print(e)
    if not os.path.exists(f"{workingDir}\{selectedExtension}_farmer.{selectedExtension}"):
        try:
            randNumber = randrange(1000)
            with open(f"{workingDir}\{selectedExtension}_farmer{randNumber}.{selectedExtension}", "w") as file:
                pass
            print(f"Made {selectedExtension}_farmer{randNumber}, open it within 10 seconds or it will break")
            print("Each file has ~20,000 lines of code. This means it will keep running (minimum ~30 hours) until you do a KeyboardInterrupt (press Control-C on console)")
            sleep(10)
            try:
                with open(f"{codePath}\{selectedExtension}.{selectedExtension}", "r", encoding="utf-8") as file:
                    for line in file:
                        for char in line:
                            if char == "\n":
                                pyautogui.press("enter")
                            elif char == "\t":
                                pyautogui.press("\t")
                            else:
                                sleep(0.50)
                                pyautogui.typewrite(char)
            except Exception as e:
                print(e)
        except Exception as e:
            pass
    else:
        os.remove(f"{workingDir}\{selectedExtension}_farmer.{selectedExtension}")
        print(f"Deleted {selectedExtension}_farmer.{selectedExtension}, re-run the program now.")
else:
    print("File extension not supported, or did you type it right? Example: py, js, or any other EXTENSION")
