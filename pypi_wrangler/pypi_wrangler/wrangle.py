import os
import re
import shutil

def normalize(name):
    """
    Normalizes name to be PEP 503 and PEP 426 compliant.

    URLS:
    https://peps.python.org/pep-0503/
    https://peps.python.org/pep-0426/
    """
    return re.sub(r"[-_.]+", "-", name).lower()

def get_package_name(file_name):
    package_name = ''
    spl = file_name.split('-')
    for part in spl:
        if not part[0].isdigit():
            package_name += part+'-'
        else:
            break
    # cleanup hanging -
    if package_name[-1] == '-':
        package_name = package_name[:-1]
    return package_name

def create_dist(from_path, to_path, cleanup=False):
    """
    Use this function to create a "dist" directory in "to_path" with all package files contained inside it from "from_path".
    """
    # verifying dir is good
    assert os.path.exists(from_path), f"{from_path} does not exist. Please provide a valid path where your package files exist."
    assert len(os.listdir(from_path)) > 0, f"{from_path} has NO files in it. Did you enter the correct path?"

    # removing trailing backslashes from paths
    if from_path[-1] == '/': 
        from_path = from_path[:-1]
    if to_path[-1] == '/':
        to_path = to_path[:-1]

    # verifying that there is .whl and .gz files in from_path
    file_types = []
    FILES = os.listdir(from_path)
    for file in FILES:
        file_types.append(file.split('.')[-1])
    assert 'gz' in file_types or 'whl' in file_types, f"{from_path} does NOT have any package source's (.tar.gz or .whl)."

    # making to_path if it doesn't exist
    if not os.path.exists(to_path):
        os.mkdir(to_path)

    # making /dist
    DIST = to_path+'/dist'
    if not os.path.exists(DIST):
        os.mkdir(DIST)

    # moves all package related files into dist while cleaning up if specified
    for file in FILES:
        ext = file.split('.')[-1]
        if 'gz' == ext or 'whl' == ext:
            PACKAGE_NAME = normalize(get_package_name(file))
            PACKAGE_PATH = f'{DIST}/{PACKAGE_NAME}'
            FROM_PATH = f'{from_path}/{file}'

            if not os.path.exists(PACKAGE_PATH):
                os.mkdir(PACKAGE_PATH)

            if cleanup:
                shutil.move(FROM_PATH, PACKAGE_PATH)
            else:
                shutil.copyfile(FROM_PATH, PACKAGE_PATH+f'/{file}')
    
    if cleanup:
        shutil.rmtree(from_path)