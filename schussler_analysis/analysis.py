import os
from syllaber_decomposer import deconstruct_syllable

current_dir = os.path.dirname(os.path.abspath(__file__))
input_files = ['MC.tsv', 'OC_schuesslerLHC.dict.yaml']
output_files = ['phoneme_correspondences.tsv']
file_tags = ['MC', 'LHan']

char_catalogue = {}
char_count_dict = {}
ii_dict, ff_dict, tt_dict = {}, {}, {}

for input_file, file_tag in zip(input_files, file_tags):
    inputdir = os.path.join(current_dir, input_file)
    with open(inputdir, 'r', encoding='utf-8') as fi:
        for line in fi:
            char, reading, *dump1 = line.split('\t')
            reading = reading.split('*')[1]

            if input_file == 'MC.tsv':
                syllable_parsed = reading[0], reading[1:-2], reading[-1]
            else:
                syllable_parsed = deconstruct_syllable(reading)

            char_catalogue[char] = ''
            
            occurence_count = char_count_dict.get((file_tag, char), 0) + 1
            char_count_dict[(file_tag, char)] = occurence_count


            
            charocckey = (file_tag, char, occurence_count)
            ii_dict[charocckey], ff_dict[charocckey], tt_dict[charocckey], *dump1 = syllable_parsed

# Mix n match single-reading characters
def analysis0(output_file):

    ii_output_list, ff_output_list = [], []
    ii_corr_dict, ff_corr_dict = {}, {}

    for char in char_catalogue.keys():
        file_tag0 = file_tags[0]
        file_tag1 = file_tags[1]
        if char_count_dict.get((file_tag0, char), 0) == 1 and char_count_dict.get((file_tag1, char), 0) == 1:

            ii_match = ','.join((ii_dict[file_tag0, char, 1], ii_dict[file_tag1, char, 1]))
            ff_match = ','.join((ff_dict[file_tag0, char, 1], ff_dict[file_tag1, char, 1]))

            ii_corr_dict[ii_match] = ii_corr_dict.get(ii_match, 0) + 1
            ff_corr_dict[ff_match] = ff_corr_dict.get(ff_match, 0) + 1

    for ii_entry in ii_corr_dict.items():
        ii_output_list.append(str(ii_entry))

    for ff_entry in ff_corr_dict.items():
        ff_output_list.append(str(ff_entry))

    outputdir = os.path.join(current_dir, output_file)
    with open(outputdir, 'w', encoding='utf-8') as fo:
        fo.write('\n'.join(ii_output_list))
        fo.write('\n_______________\n')
        fo.write('\n'.join(ff_output_list))

def analysis1(output_file):

    ii_output_list, ff_output_list = [], []
    ii_corr_dict1, ff_corr_dict1 = {}, {}

    for char in char_catalogue.keys():
        file_tag0 = file_tags[0]
        file_tag1 = file_tags[1]
        if char_count_dict.get((file_tag0, char), 0) == 1 and char_count_dict.get((file_tag1, char), 0) == 1:

            ii_match = ';'.join((ii_dict[file_tag0, char, 1], ii_dict[file_tag1, char, 1]))
            ff_match = ';'.join((ff_dict[file_tag0, char, 1], ff_dict[file_tag1, char, 1]))

            if ii_match in ii_corr_dict1:
                ii_corr_dict1[ii_match].append(char) 
            else:
                ii_corr_dict1[ii_match] = [char]

            if ff_match in ff_corr_dict1:
                ff_corr_dict1[ff_match].append(char) 
            else:
                ff_corr_dict1[ff_match] = [char]

    for ii_entry in ii_corr_dict1.items():
        ii_output_list.append('\t'.join((ii_entry[0], str(ii_entry[1]))))

    for ff_entry in ff_corr_dict1.items():
        ff_output_list.append('\t'.join((ff_entry[0], str(ff_entry[1]))))

    outputdir = os.path.join(current_dir, output_file)
    with open(outputdir, 'w', encoding='utf-8') as fo:
        fo.write('\n'.join(ii_output_list))
        fo.write('\n_______________\n')
        fo.write('\n'.join(ff_output_list))

analysis1('correspondence_analysis1.txt')