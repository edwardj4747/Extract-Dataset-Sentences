from shutil import copyfile
import glob


def cermine_files_to_directory():
    # copy all .cermxml to their own directory
    output_directory = "z_pdfs_to_convert/"
    for file in glob.glob("C:/Users/edwar/Zotero/storage/*/*.pdf"):
        print(file)
        file_name = file.split("\\")[-1]
        copyfile(file, output_directory + file_name)


cermine_files_to_directory()