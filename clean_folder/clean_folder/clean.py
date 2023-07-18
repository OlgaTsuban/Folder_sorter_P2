import sys
import pathlib
import os
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser(description="Clean folder program")
    parser.add_argument("folder_path", type=str, help="Path to the folder")
    args = parser.parse_args()
    folder_path = args.folder_path
    sort_folder_path_first(folder_path)
    print(files_in_the_list(folder_path)) #print list of the extensions and files
    sort_folder_path_second(folder_path)
    #delete empty dirs
    check_empty_dir(folder_path)


# this function iterates over all directories and subdirectories, in this step it normalizes files
def sort_folder_path_first(folder_path):
    p = pathlib.Path(folder_path)
    if p.is_file():
        print("You should write only dir, not a file\n")
    else:
        for i in p.iterdir():
            if i.is_file():
                normalize_files(i)
            elif i.is_dir():
                if i.name in ['images', 'audio', 'video', 'archives', 'documents']:
                    continue
                sort_folder_path_first(i)
                normalize_files(i)


# this function iterates over all directories and subdirectories, in this step checks empty directories and sorts files
def sort_folder_path_second(folder_path):
    p = pathlib.Path(folder_path)
    if p.is_file():
        print("You should write only dir, not a file\n")
    else:
        for i in p.iterdir():
            if i.is_file():
                sorting_files(i)
            elif i.is_dir():
                if i.name in ['images', 'audio', 'video', 'archives', 'documents']:
                    continue
                check_empty_dir(i)
                sort_folder_path_second(i)


# this function change the name of the file(normalizing)
def normalize_files(file):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    name = ''
    for char in file.name:
        if char.isalpha():
            char = TRANS.get(ord(char), char)
            name += char
        elif char.isdigit() or char == '.':
            name += char
        else:
            name += '_'
    new_file_path = os.path.join(file.parent, name)
    os.rename(file, new_file_path)
    return name


# this function create a list, which consists of extensions and names of files in each category
def files_in_the_list(folder_path):
    video = []
    images = []
    documents = []
    audio = []
    archives = []
    total_files = []
    unknown = []
    known = []

    p = pathlib.Path(folder_path)
    for i in p.iterdir():
        if i.is_file():
            if i.suffix in ['.png', '.jpeg', '.jpg', '.svg']:
                images.append(i.name)
                known.append(i.suffix)
            elif i.suffix in ['.avi', '.mp4', '.mov', '.mkv']:
                video.append(i.name)
                known.append(i.suffix)
            elif i.suffix in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                documents.append(i.name)
                known.append(i.suffix)
            elif i.suffix in ['.mp3', '.ogg', '.wav', '.amr']:
                audio.append(i.name)
                known.append(i.suffix)
            elif i.suffix in ['.zip', '.gz', '.tar']:
                archives.append(i.name)
                known.append(i.suffix)
            else:
                unknown.append(i.suffix)
        elif i.is_dir():
            sub_result = files_in_the_list(i)
            sub_files, sub_extensions = sub_result
            video += sub_files[0]
            images += sub_files[1]
            documents += sub_files[2]
            audio += sub_files[3]
            archives += sub_files[4]
            known += sub_extensions[0]
            unknown += sub_extensions[1]

    total_files = [video, images, documents, audio, archives]
    total_extension = [known, unknown]
    result = [total_files, total_extension]
    return result


# sorting files by the dir
def sorting_files(file):
    if file.exists():
        extension = {
            '.png': 'images',
            '.jpeg': 'images',
            '.jpg': 'images',
            '.svg': 'images',
            '.avi': 'video',
            '.mp4': 'video',
            '.mov': 'video',
            '.mkv': 'video',
            '.doc': 'documents',
            '.docx': 'documents',
            '.txt': 'documents',
            '.pdf': 'documents',
            '.xlsx': 'documents',
            '.pptx': 'documents',
            '.mp3': 'audio',
            '.ogg': 'audio',
            '.wav': 'audio',
            '.amr': 'audio',
            '.zip': 'archives',
            '.gz': 'archives',
            '.tar': 'archives'
        }
        if file.suffix in extension:
            parser = argparse.ArgumentParser(description="Clean folder program")
            parser.add_argument("folder_path", type=str, help="Path to the folder")
            args = parser.parse_args()
            folder_path = args.folder_path
            category_path = os.path.join(folder_path, extension[file.suffix])
            os.makedirs(category_path, exist_ok=True)
            if file.suffix in ['.zip', '.gz', '.tar']:
                file_name = file.stem
                new_file_path = os.path.join(category_path, file_name)
                os.makedirs(new_file_path, exist_ok=True)
                shutil.unpack_archive(file, new_file_path)
            else:
                new_file_path = os.path.join(category_path, file.name)
                shutil.move(file, new_file_path)


# this function checks the empty directories
def check_empty_dir(path):
    for i in os.listdir(path):
        p = os.path.join(path, i)
        if os.path.isdir(p):
            check_empty_dir(p)
            if not os.listdir(p):
                os.rmdir(p)


if __name__ == '__main__':
    main()
