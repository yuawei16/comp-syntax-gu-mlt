'''
    This script is intended to get the top 20 POS tag and syntactic labels counts
    from simplied Chinese and GUM English.
'''
import xml.etree.ElementTree as ET
from torch import sort

def get_pos_label(file):
    tree = ET.parse(file)
    root = tree.getroot()
    
    posList = []
    labelList = []

    # Extract tags and store them in a list
    for postag in root.iter('tag'):
        dicVal = postag.attrib.values()
        [val] = list(dicVal)
        posList.append((val, int(postag.text)))

    posList.sort(key= lambda x: x[1], reverse=True)

    # Extract labels and store them in a list
    for labelTag in root.iter('dep'):
        dicVal = labelTag.attrib.values()
        [val] = list(dicVal)
        labelList.append((val, int(labelTag.text)))

    labelList.sort(key= lambda x: x[1], reverse=True)
    
    return posList, labelList


def main():
    print("POS tags and Syntactic Labels Statistics")
    print("==========================================")
    f1 = "ch_s_stats.xml"
    f2 = "en_gum_stats.xml"
    tagsC, labelsC = get_pos_label(f1)
    tagsE, labelsE = get_pos_label(f2)

    print("------------------------------------------")
    print("Chinese: ", tagsC[:20])
    print("English: ", tagsE[:20])

    print("------------------------------------------")
    print("Chinese: ", labelsC[:20])
    print("English: ", labelsE[:20])

if __name__ == "__main__":
    main()