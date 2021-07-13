import os.path
import json
import time
from datetime import timedelta

website = ''
my_dict = {}

def load():
    global my_dict
    file_path = 'data.json'
    if os.path.isfile(file_path):
        file = open('data.json')
        my_dict = json.load(file)
        file.close()
    else:
        my_dict = {}

def save():
    file = open('data.json', 'w')
    json.dump( my_dict, file )
    file.close()

def get_website():
    global website
    website = input("What website are you on now? ").lower()

def record_time(start_time):
    end_time = time.time()
    my_dict[website] = my_dict.get(website, 0) + end_time - start_time

def print_dict():
    sorted_dict = sorted(my_dict, key=my_dict.get, reverse=True)
    for key in sorted_dict:
        print(key, ':', str(timedelta(seconds=round(my_dict[key], 0))))
        
def delete_prompt():
    key_to_delete = input("Type entry to delete: ")
    my_dict.pop(key_to_delete, 0)
    get_website()

def wipe():
    global my_dict
    my_dict = {}
    get_website()

def loop():
    while True:
        start_time = time.time()
        option = input("(c)hange site / (s)tat / (d)elete key / (w)ipe data / (q)uit\n")
        record_time(start_time)
        save()
        if option == 'c':
            get_website()
        elif option == 's':
            print_dict()
        elif option == 'd':
            print_dict()
            delete_prompt()
        elif option == 'w':
            wipe()
        elif option == 'q':
            print_dict()
            break
