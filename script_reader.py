#Read python file to string and return the string
def read_script(file_path):
    with open(file_path, 'r') as file:
        return file.read()
