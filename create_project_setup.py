import os

cermzone_base = 'convert_using_cermzones/'
new_cermzone_directories = ['failed_conversions', 'preprocessed', 'successful_cermfiles', 'successful_conversions', 'text']

for folder in new_cermzone_directories:
    os.makedirs(os.path.join(cermzone_base, folder))

z_active = 'z_active/'
os.makedirs(os.path.join(z_active, 'preproccesd'))
os.makedirs(os.path.join(z_active, 'sentences'))