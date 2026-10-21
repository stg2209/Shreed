# # import subprocess
# # import os

# # command = "python manage.py runserver 127.0.0.1:8000"
# # #result = subprocess.run(command, shell=True, capture_output=True, text=True)

# # os.system(command) 
# import subprocess
# import sys

# # Define the command
# command = [sys.executable, "manage.py", "runserver", "127.0.0.1:8000"]

# try:
#     # Run the command and stream output directly to the terminal
#     subprocess.run(command, check=True)
# except KeyboardInterrupt:
#     print("\nServer stopped.")
import subprocess
import time
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



cwd = "C:/Users/Shree datta/Desktop/shreedatta program/hello"
django_command = "python manage.py runserver"
process = subprocess.Popen(django_command, cwd=cwd, shell=True)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# URL you want to open
url = "http://localhost:8000"

# Open Chrome normally
subprocess.Popen([chrome_path, url])

# chrome_options = Options()
# chrome_options.add_experimental_option("useAutomationExtension", False)
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_argument("--window-size=1240,740")
# chrome_options.add_argument("--app=http://localhost:8000")  

# driver = webdriver.Chrome(options=chrome_options)

# try:
#     while True:
#         time.sleep(2)
#         driver.title
# except Exception as e:
#     driver.quit()



# for child in psutil.Process(process.pid).children(recursive=True):
#     child.terminate()

 

