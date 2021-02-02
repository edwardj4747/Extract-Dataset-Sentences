Note this code uses Cermine (https://github.com/CeON/CERMINE) and you need to download the jar file cermine-impl-1.13-jar-with-dependencies and put it in this folder as well.

Create the following directories in this folder

failed_conversions -> pdfs that could not be converted for some reason (a few greek characters that are not recognized and cause the program to error...etc)
successful_cermfiles -> .cermzone files
successful_conversions -> pdf documents that were successfully converted
text -> resulting .txt files form the .cermzone files in successful_cermfiles
z_pdfs_to_convert -> all pdfs at the beginning

1. put all pdfs into z_pdfs_to_convert (can use zotero_to_z_pdfs.py just go into it and change directory) 
2. run convert_all_possible_pdfs.py (create .cermzones files for all pdfs that can be converted -> successful_cermfiles)
3. run cermzone_to_txt.py to create the text files (will output .txt files to 'text' folder)
4. extract_relevant_sections.py to extract only the relevant sections (ie: get rid of the introduction)

