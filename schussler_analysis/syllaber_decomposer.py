# Deconstructs a syllable into Initials, Finals (or Nucleus, Coda), tonee, and Comment (anything following tonee)

import os
import re

cons = 'm̥mɱ̊ɱn̼n̥nɳ̊ɳɲ̊ɲŋ̊ŋɴ̥ɴȵpbp̪b̪t̼d̼tdʈɖcɟkɡqɢʡʔtsdzt̠ʃd̠ʒtʂdʐtɕdʑpɸbβp̪fb̪vt̪θd̪ðtɹ̝̊dɹ̝t̠ɹ̠̊˔d̠ɹ̠˔cçɟʝkxɡɣqχɢʁʡʜʡʢʔhszʃʒʂʐɕʑɸβfvθ̼ð̼θðθ̠ð̠ɹ̠̊˔ɹ̠˔ɻ̊˔ɻ˔çʝxɣχʁħʕhɦʋɹɻjɰʔ̞ⱱ̟ⱱɾ̼ɾ̥ɾɽ̊ɽɢ̆ʡ̆ʙ̥ʙr̥rɽ̊r̥ɽrʀ̥ʀʜʢtɬdɮtꞎd𝼅c𝼆ɟʎ̝k𝼄ɡʟ̝ɬɮꞎ𝼅𝼆ʎ̝𝼄ʟ̝lɭʎʟʟ̠ɺ̥ɺ𝼈̥𝼈ʎ̆ʟ̆n͡mpʼtʼʈʼcʼkʼqʼʡʼp̪fʼt̪θʼtsʼt̠ʃʼtʂʼtɕʼkxʼqχʼŋ͡mɸʼfʼθʼsʼʃʼʂʼɕʼxʼχʼtɬʼc𝼆ʼk𝼄ʼq𝼄ʼt͡pɬʼd͡bkʘkǀkǃk𝼊kǂqʘqǀqǃq𝼊qǂk͡pɡʘɡǀɡǃɡ𝼊ɡǂɡ͡bɢʘɢǀɢǃɢ𝼊ɢǂŋʘŋǀŋǃŋ𝼊ŋǂʞq͡ʡɴʘɴǀɴǃɴ𝼊ɴǂkǁq͡pqǁɡǁɢǁŋǁɴǁɓɗᶑʄɠʛʍɓ̥ɗ̥ᶑ̊ʄ̊ɠ̊ʛ̥wɧɫɠ̊͜ɓ̥ɠ͡ɓt͡pPpQqßBRbrÞCScsþDTdtÇçFVfvÐGWgwÑHXhxñJZjzðKkLlMmNnʰʳˢⁿˣᶰᶱ'
vows = 'ɿiɨɯyʉuɪʊʏeɘɤøɵoe̞əɤ̞ø̞o̞ɛεɜʌœɞɔæɐaäɑɶɒ◌aeiouAEIOUÀÁÂÃÄÅÆÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜèéêëìíîïùúûüàáâãäåæòóôõöʷʲwjɥ'
whys = 'yYÝýÿ'  # Can either be consonants/vowels, depending on orthography
nums = '1234567890'
puncs = "ˈˌːˑ̆|‖.‿↗︎↘︎̃~_-"

tags = ('C', 'V', 'V', '1', 'ː')
groups = (cons, vows, whys, nums, puncs)

# Builds a dictionary of phoneme-category assignments
phoneme_dict = {}
for tag, group in zip(tags, groups):
    for phoneme in group:
        phoneme_dict[phoneme] = tag

def deconstruct_syllable(s, decompose_final = 0):

    output_list = []

    # Converts syllable to 'skeleton'
    skeleton_list = [phoneme_dict.get(c, '?') for c in s]
    skeleton = ''.join(skeleton_list)
    
    nuc_index = skeleton.find('CV') + 1

    # Checks if closed syllable:
    if 'VC' in skeleton:
        coda_index = skeleton.find('VC') + 1
        tone_index = skeleton.find('C1') + 1 if '1' in skeleton else coda_index + 1
    elif '1' in skeleton:
        coda_index = skeleton.find('V1') + 1
        tone_index = skeleton.find('V1') + 1
    else:
        coda_index = len(s)
        tone_index = len(s)

    comment_index = re.search(r'1.', skeleton)
    comment_index = comment_index.end() if comment_index else tone_index

    if decompose_final == 0:
        indexes = (0, nuc_index, tone_index, comment_index, None)
    else:
        indexes = (0, nuc_index, coda_index, tone_index, comment_index, None)

    for i1, i2 in zip(indexes, indexes[1:]):
        output_list.append(s[i1:i2])
   
    return output_list