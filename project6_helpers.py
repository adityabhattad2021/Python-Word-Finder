import os

# print(os.curdir)

# print(os.listdir('.'))

colors={
    'red':"\033[91m",
    'base':"\033[0m"
}


def get_files_path(extension='.txt'):
    files_full_path=[os.path.join('.',f) for f in os.listdir('.') if f.endswith(extension)]
    return files_full_path


def find_words_in_files(str_to_find=None):
    all_files=get_files_path()
    for file in all_files:
        with open(file,'r') as f:
            lines = f.readlines()
            x=1
            for line in lines:
                if str_to_find in line:
                    matched_line_pretteified=line.replace(str_to_find,f"{colors['red']}{str_to_find}{colors['base']}")
                    print(f"{file[2:]}-line {x} :  {matched_line_pretteified}")
                x+=1
                

            

    
