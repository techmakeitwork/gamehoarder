#Gamehoarder v1.2
#PS2 and Xbox360 Game Fill/Search App for collectors on the go!
#The lists will be sorted as alphabetical and by absolute first letter of the title.

#Things todo
#add title option and insert into correct spot in preferred list
#work on kivy adaptation for android app
#

import math


def playstation2():
    print("You are looking at PS2 games!")
    letter = str(input ("Please enter the first letter of the game title: ")).upper()
    for fletter in ps2games:
        if fletter[0] == letter:
            print("* " + fletter)
  
def xbox360():
    print("You are looking at Xbox360 games!")
    letter = str(input ("Please enter the first letter of the game title: ")).upper()
    for fletter in xbox360games:
        if fletter[0] == letter:
            print("* " + fletter)

ps2games = [
"007 Everything or Nothing",
"Baldurs Gate : Dark Alliance",
"Ben 10 Protector of the Earth",
"Black",
"Bully",
"Call of Duty 3",
"Champions of Norrath",
"Champions of Norrath : Return to Arms",
"Civil War : The History Channel",
"Crimson Sea 2",
"Dark Cloud",
"Devil May Cry",
"Dragonball Z : Budokai 2",
"Dynasty Warriors 3",
"Enter the Matrix",
"Espn 2k5",
"Family Guy Video Game",
"Final Fantasy 10",
"Final Fantasy 12",
"Fullmetal Alchemist : And the Broken Angel",
"Gameshark 2 Grand Theft Auto 3",
"Gauntlet Dark Legacy",
"Gauntlet Seven Sorrows",
"Ghost in the Shell : Stand Alone Complex",
"GI Joe The Rise of Cobra",
"Goblin Commander : Unleash the Horde",
"God of War 2",
"Grand Theft Auto :  San Andreas",
"Grand Theft Auto 3",
"Grand Theft Auto 3 GameShark Disc",
"Gungrave Overdose",
"Hitman : Blood Money",
"Hitman 2 : Silent Assassin",
"Hitman Contracts",
"Ironman",
"Jet Li : Rise to Honor",
"Justice League Heroes",
"Kingdom Hearts",
"Lego Batman",
"Lego Star Wars",
"Lego Star Wars 2",
"Lord of the Rings Fellowship of the Ring",
"Lord of the Rings The Return of the King",
"Manhunt",
"Marvel SuperHero Squad",
"Max Payne",
"Megaman X5",
"Monsters vs Aliens",
"Naruto Uzamaki Chronicles",
"NCAA 08 Football",
"Nightmare Before Christmas",
"One Piece Pirates Carnival",
"Onimusha 2",
"Onimusha Warlords",
"Orphen : Scion of Sorcery",
"Pirates Legend of the Black Buccaneer",
"Prince of Persia : The Sands of Time",
"Puzzle Quest",
"Ratchet and Clank Going Commando",
"Rise of the Kasai",
"Samurai Warriors 2",
"Samurai Warriors 2 Empires",
"Shinobi",
"Spiderman",
"SSX Tricky",
"Star Wars Battlefront 2",
"Star Wars Bounty Hunter",
"Star Wars Episode 3",
"Summoner",
"Summoner 2",
"Tetris Worlds",
"The Getaway",
"The Incredibles",
"Tomb Raider The Angel of Darkness",
"Tom Clancy's Ghost Recon",
"Tony Hawks American Wasteland",
"Tony Hawks Pro Skater 2",
"Transformers : Revenge of the Fallen",
"Transformers the Game",
"True Crime Streets of LA",
"Unlimited Saga",
"Xmen Legends",
"Xmen Legends 2",
]

xbox360games = [
"Assasins Creed",
"Assasins Creed 2",
"Assasins Creed 3",
"Assasins Creed 4 Black flag",
"Assasins Creed Brotherhood",
"Assasins Creed Revelations",
"Batman Arkham Asylum",
"Dark Souls",
"Dead Island",
"Deadpool",
"Diablo 3 Ultimate Edition",
"Dungeon Siege 3",
"Dynasty Warriors 7",
"Dynasty Warriors 8",
"Eternal Sonata",
"Fable 2",
"Fable 3",
"Forza 2 Motorsport",
"Kingdom of fire Circle of Doom",
"Lego Marvel Super Heros",
"Lord of the rings War in the North",
"Marvel vs Capcom 3",
"Naruto Rise of a Ninja",
"Sacred 2",
"Skyrim",
"The Orange Box – Half-life 2",
"Thief",
"Tomb Raider",
"Ultimate Alliance",
"Young Justice Legacy",
]

print("GameHoarder 1.2 - You don't have them all yet!")
print("----------------------------------------------")


choice = input("Choose your system [P]S2 or [X]box360: ").lower()
#print(choice)
if choice == 'p':
    addgame = input("Would you like to [a]dd a new game or [s]earch current games?").lower()
    if addgame == 'a':
        newgame = input("Type the new game to add: ")
        print(newgame)
    elif addgame == 's': 
        playstation2()
            
    
elif choice == 'x':
    addgame = input("Would you like to [a]dd a new game or [s]earch current games?").lower()
    if addgame == 'a':
        newgame = input("Type the new game to add: ")
        print(newgame)
    elif addgame == 's': 
        xbox360()






            







    

