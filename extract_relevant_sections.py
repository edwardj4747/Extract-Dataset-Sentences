import glob
from tqdm import tqdm
import re

# text_location = 'data/cermine_results/cermzones_text/'
# output_location = 'data/cermine_results/cermzones_preprocess/'

text_location = 'convert_using_cermzones/text/'
output_location = 'convert_using_cermzones/preprocessed/'

paragraph_labels = ["Abstract", "Data", "MLS", "Aura", "Methods", "Instruments", "Measurements", "Acknowledgements"]
sections_to_avoid = ['introduction', 'references']


# file_name = 'data/cermine_results/text/Dolinar et al. - 2016 - A clear-sky radiation closure study using a one-di.txt'

for file_name in tqdm(glob.glob(text_location + '*.txt')):
    with open(file_name, encoding='utf-8') as f:

        relevant_sections = ""

        text = f.read()

        paragraphs = text.split('\n\n')
        # print(paragraphs)
        for para in paragraphs:
            split = para.split("\n")
            pg_title, pg_text = split[0], split[1:]

            # for label in paragraph_labels:
                # if label.lower() in pg_title.lower():
                #     print("HERE")

            important_section_name = any(label.lower() in pg_title.lower() for label in paragraph_labels)
            important_words_in_text = any(label.lower() in pg_text_a.lower() for label in paragraph_labels for pg_text_a in pg_text)

            pg_title = re.sub(r'[0-9]+', '', pg_title).strip()

            if important_section_name:
                relevant_sections += " ".join(pg_text) + "\n"
            elif pg_title.lower() not in sections_to_avoid and important_words_in_text:
                relevant_sections += " ".join(pg_text) + "\n"

        with open(output_location + file_name.split("\\")[-1], 'w', encoding='utf-8') as file:
            file.write(relevant_sections)