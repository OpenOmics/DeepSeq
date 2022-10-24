#!/usr/bin/env python

mut_dict = {'c.860_863dupTCTG p.(Trp288CysfsTer12)': ['TCTCTGTCTGGCAGTG', 0], # Start Grupp 1
            'c.863_864insCATG p.(Trp288CysfsTer12)': ['TCTCTGCATGGCAGTG', 0],
            'c.863_864insCCTG p.(Trp288CysfsTer12)': ['TCTCTGCCTGGCAGTG', 0],
            'c.863_864insAGGA p.(Trp288Ter)': ['TCTCTGAGGAGCAGTG', 0],
            'c.863_864insCTTG p.(Trp288CysfsTer12)': ['TCTCTGCTTGGCAGTG', 0],
            'c.863_864insTTTG p.(Trp288CysfsTer12)': ['TCTCTGTTTGGCAGTG', 0],
            'c.863_864insCCAG p.(Trp288CysfsTer12)': ['TCTCTGCCAGGCAGTG', 0],
            'c.863_864insTCGG p.(Trp288CysfsTer12)': ['TCTCTGTCGGGCAGTG', 0],
            'c.863_864insTATG p.(Trp288CysfsTer12)': ['TCTCTGTATGGCAGTG', 0],
            'c.863_864insTTCC p.(Trp288CysfsTer12)': ['TCTCTGTTCCGCAGTG', 0],
            'c.863_864insCCGA p.(Trp288CysfsTer12)': ['TCTCTGCCGAGCAGTG', 0],
            'c.863_864insTAGG p.(Trp288CysfsTer12)': ['TCTCTGTAGGGCAGTG', 0],
            'c.863_864insCAGG p.(Trp288CysfsTer12)': ['tctctgCAGGgcagtg', 0],
            'c.863_864insCGTG p.(Trp288CysfsTer12)': ['tctctgCGTGgcagtg', 0],
            'c.863_864insCAAA p.(Trp288CysfsTer12)': ['tctctgCAAAgcagtg', 0],
            'c.863_864insCTCG p.(Trp288CysfsTer12)': ['tctctgCTCGgcagtg', 0],
            'c.863_864insCCGG p.(Trp288CysfsTer12)': ['tctctgCCGGgcagtg', 0],
            'c.863_864insTTCG p.(Trp288CysfsTer12)': ['tctctgTTCGgcagtg', 0],
            'c.863_864insCTGG p.(Trp288CysfsTer12)': ['tctctgCTGGgcagtg', 0],
            'c.863_864insCAGA p.(Trp288CysfsTer12)': ['tctctgCAGAgcagtg', 0],
            'c.863_864insTGTG p.(Trp288CysfsTer12)': ['tctctgTGTGgcagtg', 0],
            'c.863_864insTCAG p.(Trp288CysfsTer12)': ['tctctgTCAGgcagtg', 0],
            'c.863_864insTAAG p.(Trp288CysfsTer12)': ['tctctgTAAGgcagtg', 0],
            'c.865_866insCAGC p.(Gln289ProfsTer11)': ['tctctgGCCAgcagtg', 0],
            'c.863_864insCAAG p.(Trp288CysfsTer12)': ['tctctgCAAGgcagtg', 0],
            'c.864delinsCCGTT p.(Trp288CysfsTer12)': ['tctctgCCGTTcagtg', 0],
            'c.863_864insTAGC p.(Trp288CysfsTer12)': ['tctctgTAGCgcagtg', 0],
            'c.863_864insTCAT p.(Trp288CysfsTer12)': ['tctctgTCATgcagtg', 0],
            'c.863_864insCTTG p.(Trp288CysfsTer12)': ['tctctgCTTGgcagtg', 0],
            'c.863_864insTACG p.(Trp288CysfsTer12)': ['tctctgTACGgcagtg', 0],
            'c.863_864insCGGA p.(Trp288CysfsTer12)': ['tctctgCGGAgcagtg', 0],
            'c.863_864insCGCC p.(Trp288CysfsTer12)': ['tctctgCGCCgcagtg', 0],
            'c.859_860insGCTG p.(Leu287ArgfsTer13)': ['aagatcGCTGtctggc', 0],
            'c.861_862insACAA p.(Trp288ThrfsTer12)': ['gatctcACAAtggcag', 0],
            'c.861_863delinsATGC p.(Trp288CysfsTer11)': ['agatctATGCgcagtg', 0],
            # Start Grupp 2
            'c.867_868insAGGA p.(Trp290ArgfsTer10)': ['tggcagAGGAtggagg', 1],
            'c.867_868insAGAA p.(Trp290ArgfsTer10)': ['tggcagAGAAtggagg', 1],
            'c.867_868insAGAC p.(Trp290ArgfsTer10)': ['tggcagAGACtggagg', 1],
            'c.867_868insCGCT p.(Trp290ArgfsTer10)': ['tggcagCGCTtggagg', 1],
            'c.867_868insCGCT p.(Trp290ArgfsTer10)': ['tggcagCGGAtggagg', 1],
            'c.867_868insCGGC p.(Trp290ArgfsTer10)': ['tggcagCGGCtggagg', 1],
            'c.868delinsCGTTC p.(Trp290ArgfsTer10)': ['tggcagCGTTCggagg', 1],
            'c.868_869insCCAT p.(Trp290SerfsTer10)': ['tggcagTCCAtggagg', 1],
            'c.867_868insAGGC p.(Trp290ArgfsTer10)': ['TGGCAGAGGCTGGAGG', 1],
            'c.867_868insCGCA p.(Trp290ArgfsTer10)': ['TGGCAGCGCATGGAGG', 1], #added 2020-12-11
            # Start Grupp 3
            'c.869_870insTTTTTCTC p.(Trp290CysfsTer13)': ['CTGGCAGTGTTTTTCTCGAGGAAGT', 2],
            'c.869_870insCATGGCTC p.(Trp290CysfsTer13)': ['CTGGCAGTGCATGGCTCGAGGAAGT', 2],
            'c.869_873delinsCTCTTGCCC p.(Trp290SerfsTer10)': ['ctggcagtCTCTTGCCCaagtctct', 2],
            'c.869_873delinsCCCTGGAGA p.(Trp290SerfsTer10)': ['ctggcagtCCCTGGAGAaagtctct', 2],
            'c.869_873delinsCCCTCGCCC p.(Trp290SerfsTer10)': ['ctggcagtCCCTCGCCCaagtctct', 2],
            'c.870_873delinsCTTCGCC p.(Trp290_Arg291delinsCysPheAla)': ['ctggcagtGCTTCGCCaagtctctt', 2],
            'c.870_873delinsTTTTTCAA p.(Trp290CysfsTer10)': ['ctggcagtGTTTTTCAAaagtctct', 2],
            'c.869_873delinsCTCTTTCTA p.(Trp290SerfsTer10)': ['ctggcagtCTCTTTCTAaagtctct', 2],
            'c.863_873delinsCCCGGGCAGT p.(Trp288SerfsTer12)': ['atctctCCCGggcagtaagtctctt', 2], #moved 2020-09-01
            'c.869_873delinsCCCTTTCCA p.(Trp290SerfsTer10)': ['ctggcagtCCCTTTCCAaagtctct', 2],
            'c.864_875delins13 p.(Trp288CysfsTer11)': ['tctctgCCACgcagtggaggtctct', 0], #moved 2020-09-01
            'c.868_870delinsCGTTTCC p.(Trp290ArgfsTer10)': ['ctctggcagCGTTTCCaggaagtct', 2],
            'c.870_873delinsCTGCTCCC p.(Trp290CysfsTer10)': ['tggcagtgCTGCTCCCaagtctctt', 2],
            'c.869_873delinsATTTTCCC p.(Trp290LeufsTer10)': ['ctggcagtTATTTTCCCaagtctct', 2],
            'c.869_873delinsCTTTCTCCC p.(Trp290SerfsTer10)': ['ctggcagtCTTTCTCCCaagtctct', 2],
            'c.869_873delinsCTTTCTCCC p.(Trp290SerfsTer10)': ['tggcagtCTTTCGCTCACgtctctt', 2],
            'c.870_873delinsTTTTGCTC p.(Trp290CysfsTer10)': ['tggcagtgTTTTGCTCaagtctctt', 2],
            'c.870_873delinsTTTTTCCC p.(Trp290CysfsTer10)': ['tggcagtgTTTTTCCCaagtctctt', 2],
            'c.868_872delinsCGGATGGCC  p.(Trp290ArgfsTer10)': ['ctggcagCggaTGGCCgaagtctct', 2],
            'c.868_871delinsCGGATTCC p.(Trp290ArgfsTer10)': ['ctggcagCggaTTCCggaagtctct', 2],
            'c.868_871dup p.(Arg291MetfsTer9)': ['ctggcagtggaTGGAggaagtctct', 2],
            'c.866_871delinsTCCGATTTGC p.(Gln289LeufsTer11)': ['ctctggcTCCGATTTGCggaagtct', 2],
            'c.864_873delins14 p.(Trp288CysfsTer12)': ['ctctgTCAAGACTTTCTTAaagtct', 2],
            'c.864_876delins17 p.(Trp288CysfsTer12)': ['tctgTCGGAGTCTCGGCGGACtctc', 2],
            'c.868_876delins13 p.(Trp290GlyfsTer10)': ['tggcagGGGGTGGGGAATCtctctt', 2],
            'c.869_876delinsATCTGGGGGCCC p.(Trp290TyrfsTer10)': ['ctggcagtATCTGGGGGCCCtctct', 2],
            'c.867_875delins14 p.(Trp290AspfsTer12)': ['ctggcaAGATTTCTTAATTCgtctc', 2],
            'c.868_875delinsGGGTTGGCCCGG p.(Trp290GlyfsTer10)': ['CTGGCAGGGGTTGGCCCGGGTCTCT', 2], # added 190527
            'c.871delinsTTGGC p.(Arg291LeufsTer9)': ['CTGGCAGTGGTTGGCGGAAGTCTCT', 2], # added 190527
            'c.868_876delins13 p.(Trp290ArgfsTer10)': ['TGGCAGCGTTTCGGGGACATCTCTT', 2], # added 190527
            'c.869_876delinsCGGTTTCTTTGC p.(Trp290SerfsTer10)': ['CTGGCAGTCGGTTTCTTTGCTCTCTTT', 2], # added 190527
            'c.868_874delinsCGGTTCGGGGC p.(Trp290ArgfsTer10)': ['CTGGCAGCGGTTCGGGGCAGTCTCT', 2], # added 191106
            # Start Grupp 4
            'c.867_868insCTTCTCCA p.(Trp290LeufsTer13)': ['ACTCTGGCAGCTTCTCCATGGAGGA', 3],
            'c.867_868insCGGATGGC p.(Trp290ArgfsTer13)': ['CTCTGGCAGCGGATGGCTGGAGGAA', 3],
            'c.863_867delinsCCATGCTCC p.(Trp288SerfsTer12)': ['agatctcTCCATGCTCCtggaggaa', 3],
            'c.864_867delinsTACCTTCC p.(Trp288CysfsTer12)': ['agatctctgTACCTTCCtggaggaa', 3],
            'c.864_865delinsCCGCGG p.(Trp288CysfsTer12)': ['aagatctctgCCGCGGagtggagga', 3],
            'c.864_865delinsTCACCT p.(Trp288CysfsTer12)': ['AGATCTCTGTCACCTAGTGGAGGAA', 3], # added 190527
            'c.864_865delinsCAGAAA p.(Trp288CysfsTer12)': ['AGATCTCTGCAGAAAAGTGGAGGAA', 3], # added 190527
            'c.867delinsAAAAA p.(Trp290LysfsTer10)': ['ATCTCTGGCAAAAAATGGAGGAAGT', 3], # added 200714
            'c.864_867delinsCACAGTTA p.(Trp288CysfsTer12)': ['AGATCTCTGCACAGTTATGGAGGAA', 3]} # added 200714

# Wildtypes: Grupp 1, Grupp 2, Grupp 3, Grupp 4 
wildtypes = ["AAGATCTCTGGCAGTG", "tctggcagtggaggaa", "TCTCTGGCAGTGGAGGAAGTCTCTT", "AAGATCTCTGGCAGTGGAGGAAGTC"]

# List of the mutation names that will be looped through
mut_list = sorted(list(mut_dict.keys()))
#mut_list = ['NPM1_Mut_A', 'NPM1_Mut_B', 'NPM1_Mut_D', 'NPM1_Mut_H', 'c.863_864insCTTG p.(Trp288CysfsTer12)', 'c.863_864insTTTG p.(Trp288CysfsTer12)', 'c.863_864insCCAG p.(Trp288CysfsTer12)', 'c.863_864insTCGG p.(Trp288CysfsTer12)', 'c.863_864insTATG p.(Trp288CysfsTer12)', 'c.863_864insTTCC p.(Trp288CysfsTer12)', 'c.863_864insCCGA p.(Trp288CysfsTer12)', 'c.863_864insTAGG p.(Trp288CysfsTer12)', 'c.859_860insGCTG p.(Leu287ArgfsTer13)', 'c.861_862insACAA p.(Trp288ThrfsTer12)', 'c.863_864insCAGG p.(Trp288CysfsTer12)', 'c.863_864insCGTG p.(Trp288CysfsTer12)', 'c.863_864insCAAA p.(Trp288CysfsTer12)', 'c.863_864insCTCG p.(Trp288CysfsTer12)', 'c.863_864insCCGG p.(Trp288CysfsTer12)', 'c.863_864insTTCG p.(Trp288CysfsTer12)', 'c.863_864insCTGG p.(Trp288CysfsTer12)', 'c.863_864insCAGA p.(Trp288CysfsTer12)', 'c.863_864insTGTG p.(Trp288CysfsTer12)', 'c.863_864insTCAG p.(Trp288CysfsTer12)', 'c.863_864insTAAG p.(Trp288CysfsTer12)', 'c.865_866insCAGC p.(Gln289ProfsTer11)', 'c.863_864insCAAG p.(Trp288CysfsTer12)', 'c.864delinsCCGTT p.(Trp288CysfsTer12)', 'c.863_864insTAGC p.(Trp288CysfsTer12)', 'c.864_875delins13 p.(Trp288CysfsTer11)', 'c.863_864insTCAT p.(Trp288CysfsTer12)', 'c.863_864insCTTG p.(Trp288CysfsTer12)', 'c.863_864insTACG p.(Trp288CysfsTer12)', 'c.863_864insCGGA p.(Trp288CysfsTer12)', 'c.863_864insCGCC p.(Trp288CysfsTer12)', 'c.863_873delinsCCCGGGCAGT p.(Trp288SerfsTer12)', 'c.861_863delinsATGC p.(Trp288CysfsTer11)', 'c.867_868insAGGA p.(Trp290ArgfsTer10)', 'c.867_868insAGAA p.(Trp290ArgfsTer10)', 'c.867_868insAGAC p.(Trp290ArgfsTer10)', 'c.867_868insCGCT p.(Trp290ArgfsTer10)', 'c.867_868insCGCT p.(Trp290ArgfsTer10)', 'c.867_868insCGGC p.(Trp290ArgfsTer10)', 'c.868delinsCGTTC p.(Trp290ArgfsTer10)', 'c.868_869insCCAT p.(Trp290SerfsTer10)', 'c.867_868insAGGC p.(Trp290ArgfsTer10)', 'c.868_870delinsCGTTTCC p.(Trp290ArgfsTer10)', 'c.868_876delins13 p.(Trp290GlyfsTer10)', 'c.869_870insTTTTTCTC p.(Trp290CysfsTer13)', 'c.869_870insCATGGCTC p.(Trp290CysfsTer13)', 'c.869_873delinsCTCTTGCCC p.(Trp290SerfsTer10)', 'c.869_873delinsCCCTGGAGA p.(Trp290SerfsTer10)', 'c.869_873delinsCCCTCGCCC p.(Trp290SerfsTer10)', 'c.870_873delinsCTTCGCC p.(Trp290_Arg291delinsCysPheAla)', 'c.870_873delinsTTTTTCAA p.(Trp290CysfsTer10)', 'c.869_873delinsCTCTTTCTA p.(Trp290SerfsTer10)', 'c.869_873delinsCCCTTTCCA p.(Trp290SerfsTer10)', 'c.869_873delinsATTTTCCC p.(Trp290LeufsTer10)', 'c.869_873delinsCTTTCTCCC p.(Trp290SerfsTer10)', 'c.870_873delinsTTTTGCTC p.(Trp290CysfsTer10)', 'c.870_873delinsTTTTTCCC p.(Trp290CysfsTer10)', 'c.870_873delinsCTGCTCCC p.(Trp290CysfsTer10)', 'c.869_873delinsCTTTCTCCC p.(Trp290SerfsTer10)', 'c.869_876delinsATCTGGGGGCCC p.(Trp290TyrfsTer10)', 'c.868_871dup p.(Arg291MetfsTer9)', 'c.868_872delinsCGGATGGCC,  p.(Trp290ArgfsTer10)', 'c.868_871delinsCGGATTCC p.(Trp290ArgfsTer10)', 'c.867_875delins14 p.(Trp290AspfsTer12)', 'c.868_875delinsGGGTTGGCCCGG p.(Trp290GlyfsTer10)', 'c.871delinsTTGGC p.(Arg291LeufsTer9)', 'c.868_876delins13 p.(Trp290ArgfsTer10)', 'c.869_876delinsCGGTTTCTTTGC p.(Trp290SerfsTer10)', 'c.866_871delinsTCCGATTTGC p.(Gln289LeufsTer11)', 'c.864_873delins14 p.(Trp288CysfsTer12)', 'c.864_876delins17 p.(Trp288CysfsTer12)', 'c.864_867delinsTACCTTCC p.(Trp288CysfsTer12)', 'c.864_865delinsCCGCGG p.(Trp288CysfsTer12)', 'c.863_867delinsCCATGCTCC p.(Trp288SerfsTer12)', 'c.867_868insCGGATGGC p.(Trp290ArgfsTer13)', 'c.867_868insCTTCTCCA p.(Trp290LeufsTer13)', 'c.864_865delinsTCACCT p.(Trp288CysfsTer12)', 'c.864_865delinsCAGAAA p.(Trp288CysfsTer12)', 'c.868_874delinsCGGTTCGGGGC p.(Trp290ArgfsTer10)', 'c.867delinsAAAAA p.(Trp290LysfsTer10)', 'c.864_867delinsCACAGTTA p.(Trp288CysfsTer12)']
