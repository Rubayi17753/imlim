A table comparing and integrating Qieyun 'glosses' from the databases powering the Autoderiver (<https://nk2028.shn.hk/tshet-uinh-autoderiver/>) before and after September 2024,
i.e. before and after the tool migrated from <https://nk2028.shn.hk/qieyun-autoderiver/>

The columns, from left to right, contain:
- Unicode codepoints, the characters, and a column reserved for miscellanous annotations (按) concerning the characters and/or readings.
	- The only annotation in the table as of 06.11.2004 is 少: a marker indicating readings that are relatively 'marginal' in attestation and use, e.g. for 三:心開一談去 ( > san4, saam3 ) of the collocations 三復 and 三思, vis-à-vis 心開一談去 ( > san1, saam1 ), the much more common reading. This category is based on a) frequencies approximated from frequency lists + a multicharacter Qieyun gloss table from the former database<sup>1</sup> ; b) Wiktionary glosses; and c) subjective judgement. This category is provisional and would be polished in the future with a more methodological approach; additional markers could be added to indicate if a reading is extinct in modern Sinitic, attested in some modern topolects but not others, hapax or dis only attested in one or two words, etc. 
- First 遺現 ('legacy'/'current') pair: Readings in the orthography/syntax of each database. 
	- A checkmark ✓ to the right indicates that the character-reading pair is actually attested in each of the database. 'Missing' Qieyun 'glosses' are supplied from homophonic characters with attested glosses in both databases, or, in cases where the *syllable* in question is completely absent from any one of the databases (indicated by ! or !!), constructed based on similar glosses in the database (in most cases this only involves a substitution in tone and initial).
- UPDATES:
	- An expanded, six-character representation of the glosses for use in parsing, conversion, etc.
	- TUPA and Baxter's typeable romanisations.
- Second 遺現: Cantonese Jyutping and Mandarin Pinyin romanisations generated from current (gwongzau.js/'推導廣州音') and legacy ('推導廣州音') algorithms, the latter provided only when differing from the former. The differences are scant enough in number (140) and type so as to allow for a brief summary of different Jyutping syllables resulting between the two algorithms:

|字|遺|現|數|
|------|------|------|------|
|*list of characters*|*legacy*|*current*|*character count*|
|丘丠休吸咻嗅嘼噏坅坵嬆嬜嶔庍庥廞廞忻恘惆搇撳昕朽欣欽歆歙殠泣湆溴潝炘炘烋焮熻珛糗翕翖脙脪脪臤臭舋菣菳蓲蚯螼螼衅衾訄訢貅赾邤邱釁鑫闟顉顉飍髤髹鵂齅龜㬤㱙㲃㵻㹯㽎㽲㾋㾙㾙䘆䠗䰍𠁫𤿳𦜓𦜵𧬈𧼒𧼒𨝫𩔝𩖄𩢮𪅲𪖛𣪘𩒣𤴾|h-|j-|102
|屈欻烼獝詘㗵㤜䎉䬄䬍𠦪𥄵𦱧𧌑𩘐䎀怴䬂|fat|wat|18
|爹箉打|z-|d-|3
|嗲丟厾銩|z-||4
|淲瀌彪驫髟𩖛|pau, bau|piu, biu|6
|佁䑂𦚪|-oi|-jai|3
|冷打|lang, zang|laang, daang|2
|倄|wui6|wai5|1
|縛|be|fo|1
|𩦠|fong|boeng|1

In these cases, the readings generated by the newer algorithm are closer to those actually attested in Cantonese. Most of the characters in the first row still in use in contemporary spoken and written Cantonese are read with initial j-, some with other initials, but none with an initial h-; only readings piu, biu are attested for characters in the 5th row. Google Translate returns the following readings (tones omitted) for characters of the 2nd row: 屈獝詘 wat 䎉 waat 烼㗵䬍 fat 欻 caa 㤜 kyut 䬄 syu 䎀 zyut 怴 hyut 䬂 jyut. Their frequencies notwithstanding, wat is from a diachronical perspective an irregular reading: the expected outcome for 溪合 xw- in Cantonese is f- (vs. 匣合 hw- > w-; i.e. 花 faa vs. 話 waa). The legacy autoderiver returns Jyutping romanisations with abberant z- for a few Qieyun glosses with the initial 端 /t/ for some reason not discernible from the algorithm (a bug?)

The readings 冷 laang and 打 daang result from line 145 of gwongzau.js:
```['庚韻 二等 (來母 或 端組)', 'aang'], // 唯來母「冷」向無 lang 音例，故例外，端組亦從之```

Miscellanous notes:
- !! 怎 is glossed 精一侵上 (ts im 上) in the former database, the only entry in the database with the final 一侵.
This final and the reading are no doubt fictious; 怎 derives from contraction and/or lenition of 作物 /tsɑk mut/.

<sup>1</sup> in all likelihood either forked from, or a parent of, <https://github.com/biopolyhedron/rime-middle-chinese/blob/master/zyenpheng.dict.yaml> . The data I worked with uses Qieyun glosses but contains the same set of characters and readings.
