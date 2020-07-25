import random
import copy
import json


initiative_list = ['hero 1', 'hero 2', 'hero 3', 'hero 4', 'enemy 1', 'enemy 2', 'enemy 3', 'enemy 4']
random.shuffle(initiative_list)


class Encounter:
    def __init__(self, name='d_encounter', actions=['d_action'], number_of_entries=1):
        self.name = name
        self.actions = actions
        self.number_of_entries = number_of_entries


if __name__ == '__main__':
    # source_deck: one copy of each type of card, with a number associated with the number of duplicates
    source_deck = [Encounter('Traitor Guardsmen', ['7', '7', '5', '6']),
                   Encounter('Traitor Guardsmen', ['7', '5', '5', '6']),
                   Encounter('Traitor Guardsmen', ['8', '6', 'Debris: it costs 2 hexes of movement instead of 1 to enter a hex with a cover hexside', '4']),
                   Encounter('Traitor Guardsmen', ['8', '6', '6', '5']),
                   Encounter('Traitor Guardsmen', ['8', '6', '6', '5']),
                   Encounter('Traitor Guardsmen', ['7', '7', '5', 'Endless Hordes: Re-roll reinforcement rolls if hostile reinforcements fail to arrive']),
                   Encounter('Traitor Guardsmen', ['8', '8', '6', '5']),
                   Encounter('Traitor Guardsmen', ['7', '5', '4', '6']),
                   Encounter('Negavolt Cultists', ['4', '3', 'Loose Cabling: make an agility roll for an explorer that moves into a hex with a discovery marker. if the roll is failed, that explorer suffers a grevious wound.', '3']),
                   Encounter('Negavolt Cultists', ['4', '4', '3', 'Noxious Fumes: in the event phase, after resolvign the random event, roll the Blackstone dice for each explorer and hostile. On a 1, that explorer or hostile suffers 1 wound']),
                   Encounter('Negavolt Cultists', ['4', '3', '3', '3']),
                   Encounter('Negavolt Cultists', ['4', '3', '2', '2']),
                   Encounter('Ur-Ghuls', ['4', '3', '2', '3']),
                   Encounter('Ur-Ghuls', ['4', '3', '3', '3']),
                   Encounter('Ur-Ghuls', ['4', '3', 'Blackout: The maximum range of all attacks is 3 hexes', '2']),
                   Encounter('Ur-Ghuls', ['4', '4', '3', 'Terrifying Howls: Increase the cost of Move actions for explorers from 1+ to 2+']),
                   Encounter('Spindle Drones', ['2', '2', '1', '1']),
                   Encounter('Spindle Drones', ['2', '2', 'Major Find: When an explorer searches a discovery marker, they draw two discover cards instead of one', '1']),
                   Encounter('Spindle Drones', ['2', '2', '1', '1']),
                   Encounter('Spindle Drones', ['2', '2', '1', 'Major Find: When an explorer searches a discovery marker, they draw two discover cards instead of one']),
                   Encounter('Obsidius Mallex', ['Obsidius Mallex and 2 Chaos Marines and 4 Traitor Guardsmen', 'Obsidius Mallex and 2 Chaos Marines', 'Obsidius Mallex and 6 Traitor Guardsmen', 'Obsidius Mallex and 4 Chaos Beastmen']),
                   Encounter('Obsidius Mallex', ['Obsidius Mallex and 2 Chaos Marines and 1 Rogue Psyker', 'Obsidius Mallex and 2 Chaos Marines', 'Obsidius Mallex and 4 Chaos Beastmen', 'Obsidius Mallex and 6 Traitor Guardsmen']),
                   Encounter('Cultists', ['1 Cultist Firebrand and 7 Cultists', '1 Cultist Firebrand and 7 Cultists', '7', '7'], 4),
                   Encounter('Chaos Beastmen', ['4', '3', '2', '3']),
                   Encounter('Chaos Beastmen', ['4', '4', '3', '3']),
                   Encounter('Chaos Beastmen', ['4', '4', '3', 'Surprise Attack: In the first turn, treat any odd-numbered behaviour roll for a hostile as a Hold action']),
                   Encounter('Chaos Beastmen', ['4', '3', 'No Cover: Ignore cover hexsides in this combat', '2']),
                   Encounter('Rogue Psykers', ['2 Rogue Psykers, 6 Traitor Guardsmen', '1 Rogue Psyker, 4 Traitor Guardsmen', '2', '1'], 2),
                   Encounter('Rogue Psykers', ['2 Rogue Psykers, 4 Traitor Guardsmen', '1 Rogue Psykers, 6 Traitor Guardsmen', '1', '2'], 2),
                   Encounter('Chaos Space Marines', ['2 Chaos Marines and 4 Negavolt Cultists', '2', '1 Chaos Marines and 2 Chaos Beastmen', '1 Chaos Marines and 4 Traitor Guardsmen'], 2),
                   Encounter('Chaos Space Marines', ['2 Chaos Marines and 6 Traitor Guardsmen', '2', '1 Chaos Marines and 4 Traitor Guardsmen', '1 Chaos Marines and 2 Chaos Beastmen'], 2),
                   Encounter('Acolyte Hybrids', ['1 Acolyte Leader, 1 Specialist, 5 Acolytes', '1 Acolyte Leader, 1 Specialist, 3 Acolytes', '1 Acolyte Leader, 2 Acolytes', '3 Acolytes'], 4),
                   Encounter('Aberrants', ['3 Abberants, 5 Neophytes', '2 Abberants, 3 Acolytes','2 Abberants, 3 Neophytes','1 Abberants, 5 Brood Brothers'],2),
                   Encounter('Brood Brothers', ['1 Leader, 2 Specialists, 4 Brood Brothers', '1 Leader, 1 Specialist, 3 Brood Brothers','1 Leader, 2 Brood Brothers','3 Brood Brothers'],8),
                   Encounter('Heavy Weapons Team',['3','2','2','1'], 4),
                   Encounter('Magus', ['1 Magus, 2 Specialists, 5 Brood Brothers', '1 Magus, 1 Specialist, 3 Acolytes', '1 Magus, 1 Specialist, 3 Neophytes', '1 Magus, 5 Brood Brothers'], 2),
                   Encounter('Neophyte Hybrids',['1 Neophyte Leader, 1 Heavy & 1 Specailist, 4 Neophytes','1 Neophyte Leader, 1 Heavy & 1 Specialist, 2 Neophytes','1 Neophyte Leader, 1 Heavy OR 1 Specialist, 1 Neophytes','3 Neophytes'], 8),
                   Encounter('Genestealers', ['5','4','3','3'],4),
                   Encounter('Cult Sentinel', ['1 Cult Sentinel, 1 Heavy Weapon, 5 Brood Brothers', '1 Cult Sentinel, 1 Heavy Weapon, 3 Brood Brothers', '1 Cult Sentinel, 3 Brood Brothers', '1 Cult Sentinel'], 2),
                   Encounter('Burna Boyz', ['1 Spanner 6 Burna Boyz','1 Spanner 4 Burna Boyz','1 Spanner 2 Burna Boyz','3 Burna Boyz'],4),
                   Encounter('Nobz', ['2 Nobz, 5 Sluggas','2 Nobz, 5 Shootas','1 Nobz, 3 Burna Boyz','1 Nobz, 3 Sluggas'],2),
                   Encounter('Runtherd', ['Runtherd, 10 Gretchen','Runtherd, 7 Gretchen','Runtherd, 5 Gretchen','Runtherd, 3 Gretchen'],8),
                   Encounter('Sluggas', ['1 Boss Nobz, 1 Specialist, 5 Sluggas','1 Boss Nobz, 1 Specialist, 3 Sluggas','1 Boss Nobz, 3 Sluggas','1 Boss Nobz, 2 Sluggas'],8),
                   Encounter('Shootas', ['1 Boss Nobz, 1 Specialist, 5 Shootas','1 Boss Nobz, 1 Specialist, 3 Shootas','1 Boss Nobz, 4 Shootas','1 Boss Nobz, 2 Shootas'],8),
                   Encounter('Stormboyz', ['1 Boss Nobz, 4 Stormboyz','1 Boss Nobz, 3 Stormboyz','1 Boss Nobz, 2 Stormboyz','3 Stormboyz'],4),
                   Encounter('Warboss', ['1 Warboss, 2 Nobz, 5 Shootas','1 Warboss, 2 Nobz, 4 Sluggas','1 Warboss, 1 Nobz, 3 Shootas','1 Warboss, 1 Nobz, 2 Sluggas'],2),
                   Encounter('Weird Boy', ['1 Weird Boy, 1 Nob, 5 Sluggas','1 Weird Boy, 1 Nob, 4 Shootas','1 Weird Boy, 3 Sluggas','1 Weird Boy, 2 Shootas'],2),
                   Encounter('Killa Kan', ['1 Killa Kan, 5 Sluggas','1 Killa Kan, 5 Shootas','1 Killa Kan, 1 Spanner, 2 Burnas','1 Killa Kan'],2),]

    # copy_deck: the finished version of the deck
    copy_deck = []

    # duplicates cards based on number of entries
    for card in source_deck:
        for i in range(0, card.number_of_entries):
            copy_deck.append(copy.copy(card))

    # shuffles the deck
    print('shuffling the deck')
    random.shuffle(copy_deck)

    # prints the cards
    print('the shuffled cards')
    for i in range(0,3):
        print(i+1, copy_deck[i].name + ': ', copy_deck[i].actions[i])

    '''
    for card in copy_deck:
        print(card.name, card.actions)
    '''