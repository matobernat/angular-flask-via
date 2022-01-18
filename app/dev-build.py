import os
import subprocess
import time




CURRENT_DIRECTORY = os.getcwd()
print("CURRECNT DIR: ", CURRENT_DIRECTORY)

directories = os.listdir(CURRENT_DIRECTORY)
print("LIST DIR: ", directories)
NON_ANGULAR_DIRS = ['static', 'templates', 'venv']

for directory in directories:
    if "." not in directory and directory not in NON_ANGULAR_DIRS:
        ANGULAR_PROJECT_PATH = os.path.join(CURRENT_DIRECTORY, directory)
        DIST_PATH = os.path.join(ANGULAR_PROJECT_PATH, 'dist', directory)
        print("ANGULAR PATH: ", ANGULAR_PROJECT_PATH)
        print("DIST PATH: ", DIST_PATH)

FLASK_STATIC_PATH = os.path.join(CURRENT_DIRECTORY, '../static')
FLASK_TEMPLATES_PATH = os.path.join(CURRENT_DIRECTORY, '../templates')

print(" BUILD COMMAND 0 START : ", 'cd ' + ANGULAR_PROJECT_PATH + ' && ng build --watch --base-href /static/ &')

subprocess.call(('cd ' + ANGULAR_PROJECT_PATH + ' && ng build --watch --base-href /static/ &'), shell=True)
# subprocess.call(('cd ' + ANGULAR_PROJECT_PATH + ' && ng build --watch --base-href /static/'), shell=True)
print("BUILD COMMAND 0 DONE : ", 'cd ' + ANGULAR_PROJECT_PATH + ' && ng build --watch --base-href /static/ ')



# FIRST RUN
try:

    print("FIRST RUN ******  \n ")
    # FIRST DELETE OLD FILES
    old_files = os.listdir(FLASK_STATIC_PATH)
    print("OLD FILES: ", old_files)
    old_static_files = ""
    for file in old_files:
        if '.js' in file or '.css' in file:
            old_static_files += (file + ' ')

    # THEN MOVE NEW FILES
    files = os.listdir(DIST_PATH)
    print("NEW FILES: ", files)
    static_files = ""
    html_files = ""
    for file in files:
        if '.js' in file or '.css' in file or '.ico' in file:
            static_files += (file + ' ')
        if '.html' in file:
            html_files += (file + ' ')
    if len(static_files) > 0:
        # FIRST DELETING
        if len(old_static_files) > 0:
            print("COMMAND 1.1 START: ", 'cd ' + FLASK_STATIC_PATH + ' &&' + ' rm ' + old_static_files)
            subprocess.call(('cd ' + FLASK_STATIC_PATH + ' &&' + ' rm ' + old_static_files), shell=True)
        # THEN MOVING NEW
        print("COMMAND 1 START: ", 'cd ' + DIST_PATH + ' &&' + ' mv ' + static_files + FLASK_STATIC_PATH)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' mv ' + static_files + FLASK_STATIC_PATH), shell=True)
        print("COMMAND 1 DONE: ", 'cd ' + DIST_PATH + ' &&' + ' mv ' + static_files + FLASK_STATIC_PATH)

    if len(html_files) > 0:
        print("COMMAND 2 START:", 'cd ' + DIST_PATH + ' &&' + ' mv ' + html_files + FLASK_TEMPLATES_PATH)
        subprocess.call(('cd ' + DIST_PATH + ' &&' + ' mv ' + html_files + FLASK_TEMPLATES_PATH), shell=True)
        print("COMMAND 2 DONE:", 'cd ' + DIST_PATH + ' &&' + ' mv ' + html_files + FLASK_TEMPLATES_PATH)

    print("FIRST RUN ****** END  \n ")
except Exception as e:
    dir_exists = False
    print(e)














dir_exists = True

while dir_exists:
    print("INSIDE WHILE")
    # dir_exists = False
    try:

        # FIRST DELETE OLD FILES
        old_files = os.listdir(FLASK_STATIC_PATH)
        print("OLD FILES: ", old_files)
        old_static_files = ""
        for file in old_files:
            if 'main' in file:
                old_static_files += (file + ' ')


        # THEN MOVE NEW FILES
        files = os.listdir(DIST_PATH)
        print("NEW FILES: ", files)
        static_files = ""
        html_files = ""
        for file in files:
            if '.js' in file or '.css' in file or '.ico' in file:
                static_files += (file + ' ')
            if '.html' in file:
                html_files += (file + ' ')
        if len(static_files) > 0:
            # FIRST DELETING
            if len(old_static_files) > 0:
                print("COMMAND 1.1 START: ", 'cd ' + FLASK_STATIC_PATH + ' &&' + ' rm ' + old_static_files )
                subprocess.call(('cd ' + FLASK_STATIC_PATH + ' &&' + ' rm ' + old_static_files ), shell=True)
            # THEN MOVING NEW
            print("COMMAND 1 START: ",'cd ' + DIST_PATH + ' &&' + ' mv ' + static_files + FLASK_STATIC_PATH)
            subprocess.call(('cd ' + DIST_PATH + ' &&' + ' mv ' + static_files + FLASK_STATIC_PATH), shell=True)
            print("COMMAND 1 DONE: ",'cd ' + DIST_PATH + ' &&' + ' mv ' + static_files + FLASK_STATIC_PATH)

        if len(html_files) > 0:
            print("COMMAND 2 START:", 'cd ' + DIST_PATH + ' &&' + ' mv ' + html_files + FLASK_TEMPLATES_PATH)
            subprocess.call(('cd ' + DIST_PATH + ' &&' + ' mv ' + html_files + FLASK_TEMPLATES_PATH), shell=True)
            print("COMMAND 2 DONE:", 'cd ' + DIST_PATH + ' &&' + ' mv ' + html_files + FLASK_TEMPLATES_PATH)

    except Exception as e:
        dir_exists = False
        print(e)
    time.sleep(20.0)