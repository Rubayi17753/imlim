import os
from tqdm import tqdm

current_dir = os.path.dirname(os.path.abspath(__file__))
input_files = [f for f in os.listdir(os.path.join(current_dir, 'RIME_OC_to_integrate'))]
output_file = 'OC_integrated.tsv'

char_dict = {}
file_char_pron_dict = {}
output_list = []

for input_file in input_files:
    inputdir = os.path.join(current_dir, 'RIME_OC_to_integrate', input_file)
    with open(inputdir, 'r', encoding='utf-8') as fi:
        for line in fi:
            if '\t' in line:
                char, reading, *dump1 = line.strip('\n').split('\t')
                if '*' in reading:
                    reading = reading.split('*')[1]

                char_dict[char] = ''

                if (input_file, char) in file_char_pron_dict:
                    file_char_pron_dict[(input_file, char)].append(reading)
                else:
                    file_char_pron_dict[(input_file, char)] = [reading]

output_list.append(' ')
output_list.append('\t'.join(input_files))
output_list.append('\n')

for char in tqdm(char_dict.keys()):

    output_list.append(char)

    for input_file in input_files:
        current_pron_list = file_char_pron_dict.get((input_file, char), [])
        current_prons_string = '⸗'.join(current_pron_list)
        output_list.append(current_prons_string)

    output_list.append('\n')

outputdir = os.path.join(current_dir, output_file)
with open(outputdir, 'w', encoding='utf-8') as fo:
    fo.write('\t'.join(output_list))





