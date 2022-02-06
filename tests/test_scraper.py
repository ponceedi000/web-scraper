from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_count_true_mortal_kombat():
    url = 'https://en.wikipedia.org/wiki/Reptile_(Mortal_Kombat)#Other_media'
    count = get_citations_needed_count(url)
    expected = 6
    actual = count
    assert expected == actual

def test_count_false_mortal_kombat():
    url = 'https://en.wikipedia.org/wiki/Reptile_(Mortal_Kombat)#Other_media'
    count = get_citations_needed_count(url)
    expected = 3
    actual = count
    assert expected != actual

def test_count_true_cnut():
    url = 'https://en.wikipedia.org/wiki/Cnut#Statesmanship'
    count = get_citations_needed_count(url)
    expected = 6
    actual = count
    assert expected == actual

def test_count_false_cnut():
    url = 'https://en.wikipedia.org/wiki/Cnut#Statesmanship'
    count = get_citations_needed_count(url)
    expected = 3
    actual = count
    assert expected != actual

def test_passage_mortal_kombat_paragraph1():
    paragraph = "In the original Mortal Kombat, Reptile is a mysterious hidden enemy character, unplayable and with no biography.[8][22] Hints regarding the conditions of how to unlock the fight against him are conveyed by Reptile randomly appearing prior to other matches,[9] such as \"Blocking will get you nowhere\", \"Look to La Luna\", or \"Perfection is the key\". To fight Reptile, the player must get a Double Flawless victory in single-player mode on the Pit stage and finish the match off with a Fatality, all without blocking. There must also be a silhouette flying past the moon, which will occur every sixth game. Once all conditions are met, Reptile will announce \"You have found me, now prove yourself!\". The match takes place on the spiked floor of the Pit, and defeating him with a Fatality earns the player 10,000,000 points.[citation needed]"
    url = 'https://en.wikipedia.org/wiki/Reptile_(Mortal_Kombat)#Other_media'
    passage = get_citations_needed_report(url)
    assert(paragraph in passage)

def test_passage_mortal_kombat_paragraph2():
    paragraph = "In Mortal Kombat II, Reptile returns as a playable character and a member of a reptilian race called Raptors,[23] who were pulled into Outworld and enslaved by Shao Kahn. Promised the revival of his people in turn for his loyalty, Reptile serves Kahn as Shang Tsung's bodyguard.[24] He was chosen to assist Jade in order to kill Kitana during the events of Ultimate Mortal Kombat 3,[25] he is defeated and exiled, but reappears in Mortal Kombat 4 as Shinnok's minion.[14] By Mortal Kombat: Deadly Alliance, Reptile returns to Kahn's service. He overhears Shang Tsung plotting to kill Kahn, but en route to warn his master, he meets a female vampire who offers knowledge of his race.[13] Reptile pledges his loyalties to her, though eventually realizes she is merely using him and sets out to kill her. Instead of the vampire he finds Onaga's dragon egg instead,[26] which transforms Reptile into Onaga's avatar, leading to the events of Mortal Kombat: Deception[15] and ending with his defeat at the game's conclusion.[27] Separated from Onaga as a result, Reptile returns in Mortal Kombat: Armageddon. In Konquest mode in Armageddon, he appears in the Red Dragon lair commanding Daegon's dragon Caro to close the portal but refused. Taven battles Reptile in combat and emerges victorious.[citation needed]"
    url = 'https://en.wikipedia.org/wiki/Reptile_(Mortal_Kombat)#Other_media'
    passage = get_citations_needed_report(url)
    assert(paragraph in passage)

def test_passage_cnut_paragraph1():
    paragraph = "This initial distribution of power was short-lived. The chronically treacherous Eadric was executed within a year of Cnut's accession.[42] Mercia passed to one of the leading families of the region, probably first to Leofwine, ealdorman of the Hwicce under Æthelred, but certainly soon to his son Leofric.[45] In 1021, Thorkel also fell from favour and was outlawed. Following the death of Erik in the 1020s, he was succeeded as Earl of Northumbria by Siward, whose grandmother,[citation needed] Estrid (married to Úlfr Thorgilsson), was Cnut's sister. Bernicia, the northern part of Northumbria, was theoretically part of Erik and Siward's earldom, but throughout Cnut's reign it effectively remained under the control of the English dynasty based at Bamburgh, which had dominated the area at least since the early 10th century. They served as junior Earls of Bernicia under the titular authority of the Earl of Northumbria. By the 1030s Cnut's direct administration of Wessex had come to an end, with the establishment of an earldom under Godwin, an Englishman from a powerful Sussex family. In general, after initial reliance on his Scandinavian followers in the first years of his reign, Cnut allowed those Anglo-Saxon families of the existing English nobility who had earned his trust to assume rulership of his Earldoms."
    url = 'https://en.wikipedia.org/wiki/Cnut#Statesmanship'
    passage = get_citations_needed_report(url)
    assert(paragraph in passage)

def test_passage_cnut_paragraph2():
    paragraph = "Cnut reinstituted the extant laws with a series of proclamations to assuage common grievances brought to his attention, including: On Inheritance in case of Intestacy, and On Heriots and Reliefs.[50] He also strengthened the currency, initiating a series of coins of equal weight to those being used in Denmark and other parts of Scandinavia.[citation needed] He issued the Law codes of Cnut known now as I Cnut and II Cnut, though these seem primarily to have been produced by Wulfstan of York.[51]"
    url = 'https://en.wikipedia.org/wiki/Cnut#Statesmanship'
    passage = get_citations_needed_report(url)
    assert(paragraph in passage)