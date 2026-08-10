# Pythonic

from itertools import combinations
from collections import Counter
import numpy as np
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Non-Pythonic approach
i = 0
new_list = []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Half-Pythonic approach
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Pythonic approach
# This would be read as:
# first name -> what is being saved.
# after for -> element being iterated.
# after if -> condition that must be met for the element to be saved.
best_list = [name for name in names if len(name) >= 6]
print(best_list)

# Range()

# range(start, stop, step)
nums = range(0, 11)
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
# * unpacks the object into a list, this means it is like doing list(range(1,12,2))
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)

# Enumerate()

# enumerate(variable, start, stop, step)
letters = ['a', 'b', 'c', 'd', 'e']
indexed_letters = enumerate(letters)
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)

# Enumerate non-Pythonic approach
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Enumerate Pythonic approach
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Enumerate Pythonic approach with unpacking
print('*******************')
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

# Map()

nums = [1.5, 2.5, 3.5, 4.5, 5.5]
rnd_nums = map(round, nums)
print(list(rnd_nums))

nums = [1, 2, 3, 4, 5]
sqrd_nums = map(lambda x: x**2, nums)
print(list(sqrd_nums))

# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Unpack names_map into a list
names_uppercase = [*names_map]

print(type(names_map))
print(names_uppercase)

# NumPy


nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
nums = np.array(nums)

# Print second row of nums
print(nums[1, :])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums)

# All Together.

# Create a list of arrival times
arrival_times = [*range(10, 60, 10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]


def welcome_guest(
    guest_time): return f"Welcome {guest_time[0]}! Your table will be ready at {guest_time[1]} minutes."


# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

# Run time.

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)
# %timeit nums_list_comp = [num for num in range(51)]

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

# %timeit nums_list_comp = [num for num in range(51)]

# Zip
# zip() unifies two or more iterables into a single iterable of tuples.

# Combine names and primary_types
names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock']
secondary_types = ['Ice', np.nan, np.nan, np.nan, 'Flying']

names_type1 = [*zip(names, primary_types)]
names_types = [*zip(names, primary_types, secondary_types)]
differing_lengths = [*zip(names[:5], primary_types[:3])]

print('*******************')
print(*names_type1[:5], sep='\n')
print('*******************')
print(*names_types[:5], sep='\n')
print('*******************')
print(*differing_lengths, sep='\n')

# Collections

generations = [1, 1, 1, 5, 3, 5, 1, 6, 1, 6, 5, 5, 4, 6, 3, 4, 2, 5, 2, 5, 4, 1, 1, 2, 6, 5, 5, 6, 6, 1, 4, 5, 6, 2, 6, 1, 3, 2, 4, 1, 5, 3, 5, 5, 1, 5, 5, 5, 5, 6, 1, 3, 4, 6, 1, 4, 5, 3, 5, 5, 1, 4, 1, 1, 5, 6, 5, 1, 1, 6, 5, 5, 4, 6, 1, 1, 4, 5, 4, 5, 6, 2, 3, 5, 6, 5, 3, 4, 5, 1, 5, 6, 1, 1, 2, 3, 3, 3, 4, 4, 1, 3, 6, 3, 5, 3, 5, 3, 3, 1, 3, 6, 4, 4, 4, 5, 3, 4, 4, 3, 5, 5, 3, 5, 4, 1, 1, 3, 5, 3, 2, 5, 4, 3, 2, 4, 3, 5, 3, 1, 2, 4, 3, 5, 3, 5, 4, 1, 2, 4, 3, 5, 5, 1, 4, 6, 3, 6, 3, 4, 1, 5, 6, 1, 5, 4, 4, 3, 3, 5, 2, 3, 1, 6, 5, 1, 5, 4, 3, 6, 1, 3, 3, 6, 4, 3, 5, 4, 2, 4, 4, 1, 2, 5, 1, 3, 6, 4, 1, 1, 1, 1, 2, 4, 1, 1, 4, 4, 5, 3, 1, 4, 5, 3, 4, 1, 3, 4, 2, 5, 3, 4, 1, 1, 1, 5, 1, 4, 4, 3, 4, 3, 5, 3, 2, 3, 3, 3, 2, 4, 1, 3, 4, 2, 6, 5, 2, 5,
               5, 1, 1, 1, 5, 4, 2, 4, 2, 2, 5, 5, 5, 4, 2, 3, 3, 5, 4, 5, 6, 3, 1, 2, 4, 2, 5, 1, 4, 3, 1, 1, 1, 1, 3, 5, 1, 3, 3, 3, 3, 5, 2, 5, 4, 2, 2, 3, 6, 4, 2, 1, 2, 5, 5, 3, 1, 3, 5, 5, 5, 5, 6, 5, 1, 5, 1, 5, 5, 1, 6, 4, 3, 1, 6, 5, 1, 4, 6, 5, 1, 2, 5, 5, 3, 1, 5, 5, 3, 3, 3, 6, 1, 5, 1, 3, 3, 4, 5, 3, 1, 1, 1, 6, 3, 3, 4, 5, 3, 5, 4, 5, 1, 5, 5, 3, 5, 6, 5, 4, 5, 6, 1, 1, 4, 1, 3, 4, 1, 4, 1, 1, 5, 4, 4, 5, 5, 6, 1, 1, 2, 4, 2, 5, 2, 5, 5, 6, 1, 3, 3, 5, 6, 4, 3, 3, 1, 5, 5, 2, 3, 5, 3, 6, 3, 5, 2, 1, 2, 5, 2, 3, 3, 1, 3, 1, 1, 4, 3, 1, 3, 5, 1, 3, 6, 4, 5, 2, 2, 6, 2, 2, 5, 6, 2, 1, 3, 5, 3, 3, 5, 5, 5, 3, 5, 2, 2, 4, 4, 3, 5, 6, 1, 4, 1, 1, 4, 2, 3, 4, 5, 2, 4, 3, 3, 4, 3, 3, 3, 3, 1, 2, 3, 5, 5, 6, 4, 3, 5, 5, 5, 6, 1, 2, 3, 1, 5, 6, 2, 1, 3, 5]
primary_types = ['Water', 'Poison', 'Normal', 'Ice', 'Water', 'Bug', 'Grass', 'Normal', 'Psychic', 'Fairy', 'Rock', 'Ice', 'Grass', 'Rock', 'Steel', 'Normal', 'Normal', 'Fire', 'Grass', 'Ground', 'Psychic', 'Grass', 'Ground', 'Normal', 'Bug', 'Water', 'Water', 'Steel', 'Grass', 'Normal', 'Ground', 'Normal', 'Fire', 'Water', 'Electric', 'Rock', 'Ground', 'Normal', 'Bug', 'Fairy', 'Ground', 'Ice', 'Fighting', 'Bug', 'Ghost', 'Psychic', 'Electric', 'Grass', 'Grass', 'Fairy', 'Ground', 'Water', 'Fire', 'Rock', 'Rock', 'Ice', 'Psychic', 'Steel', 'Water', 'Normal', 'Grass', 'Normal', 'Rock', 'Normal', 'Ghost', 'Fairy', 'Grass', 'Rock', 'Electric', 'Fairy', 'Normal', 'Bug', 'Psychic', 'Fire', 'Normal', 'Water', 'Water', 'Ghost', 'Fire', 'Normal', 'Fire', 'Ice', 'Normal', 'Ground', 'Fairy', 'Normal', 'Water', 'Psychic', 'Psychic', 'Fire', 'Ground', 'Fire', 'Grass', 'Normal', 'Ice', 'Fighting', 'Fire', 'Psychic', 'Ghost', 'Bug', 'Ground', 'Water', 'Normal', 'Normal', 'Dark', 'Rock', 'Electric', 'Normal', 'Grass', 'Bug', 'Ground', 'Psychic', 'Rock', 'Water', 'Grass', 'Grass', 'Poison', 'Water', 'Electric', 'Fire', 'Fire', 'Ice', 'Psychic', 'Fire', 'Ground', 'Water', 'Water', 'Water', 'Dark', 'Ground', 'Water', 'Bug', 'Rock', 'Ice', 'Bug', 'Water', 'Grass', 'Dragon', 'Normal', 'Water', 'Ground', 'Bug', 'Steel', 'Water', 'Bug', 'Dragon', 'Electric', 'Rock', 'Ice', 'Grass', 'Bug', 'Steel', 'Normal', 'Grass', 'Electric', 'Poison', 'Psychic', 'Electric', 'Electric', 'Grass', 'Bug', 'Bug', 'Fairy', 'Fighting', 'Water', 'Poison', 'Normal', 'Water', 'Normal', 'Ghost', 'Grass', 'Fire', 'Water', 'Electric', 'Bug', 'Normal', 'Dark', 'Water', 'Dragon', 'Bug', 'Fire', 'Water', 'Grass', 'Fairy', 'Dark', 'Electric', 'Grass', 'Bug', 'Normal', 'Rock', 'Poison', 'Poison', 'Rock', 'Water', 'Fire', 'Steel', 'Water', 'Psychic', 'Electric', 'Fairy', 'Grass', 'Grass', 'Grass', 'Normal', 'Normal', 'Rock', 'Dragon', 'Bug', 'Water', 'Normal', 'Dragon', 'Poison', 'Psychic', 'Grass', 'Fire', 'Poison', 'Grass', 'Grass', 'Bug', 'Normal', 'Rock', 'Ice', 'Water', 'Water', 'Poison', 'Dragon', 'Bug', 'Grass', 'Grass', 'Normal', 'Dark', 'Ghost', 'Water', 'Steel', 'Electric', 'Psychic', 'Fighting', 'Poison', 'Normal', 'Psychic', 'Normal', 'Water', 'Bug', 'Dark', 'Normal', 'Bug', 'Fairy', 'Fighting', 'Water', 'Fire', 'Fighting',
                 'Grass', 'Bug', 'Water', 'Water', 'Normal', 'Normal', 'Normal', 'Dragon', 'Grass', 'Water', 'Normal', 'Bug', 'Water', 'Steel', 'Water', 'Ghost', 'Rock', 'Dark', 'Electric', 'Ground', 'Poison', 'Water', 'Bug', 'Grass', 'Water', 'Bug', 'Normal', 'Poison', 'Psychic', 'Bug', 'Fighting', 'Normal', 'Grass', 'Grass', 'Poison', 'Normal', 'Ground', 'Normal', 'Bug', 'Fairy', 'Bug', 'Steel', 'Rock', 'Water', 'Fire', 'Fire', 'Water', 'Grass', 'Ice', 'Dark', 'Psychic', 'Water', 'Ice', 'Psychic', 'Rock', 'Steel', 'Water', 'Water', 'Bug', 'Normal', 'Dragon', 'Water', 'Electric', 'Ground', 'Normal', 'Bug', 'Dragon', 'Fighting', 'Electric', 'Psychic', 'Fighting', 'Fairy', 'Psychic', 'Water', 'Fire', 'Rock', 'Dark', 'Poison', 'Ice', 'Dragon', 'Normal', 'Dragon', 'Grass', 'Electric', 'Water', 'Psychic', 'Ground', 'Steel', 'Ice', 'Fairy', 'Fighting', 'Water', 'Ground', 'Normal', 'Poison', 'Steel', 'Water', 'Psychic', 'Ground', 'Poison', 'Fighting', 'Psychic', 'Steel', 'Rock', 'Water', 'Psychic', 'Water', 'Ghost', 'Psychic', 'Fighting', 'Bug', 'Bug', 'Grass', 'Normal', 'Ice', 'Dragon', 'Electric', 'Electric', 'Grass', 'Fairy', 'Rock', 'Normal', 'Water', 'Fighting', 'Water', 'Bug', 'Normal', 'Normal', 'Poison', 'Electric', 'Grass', 'Dark', 'Fire', 'Steel', 'Fire', 'Poison', 'Dragon', 'Rock', 'Bug', 'Psychic', 'Grass', 'Normal', 'Bug', 'Ghost', 'Dark', 'Fighting', 'Electric', 'Dragon', 'Dark', 'Normal', 'Fighting', 'Electric', 'Rock', 'Normal', 'Normal', 'Bug', 'Fire', 'Water', 'Normal', 'Ground', 'Bug', 'Fire', 'Bug', 'Water', 'Fire', 'Bug', 'Ghost', 'Bug', 'Steel', 'Ice', 'Normal', 'Water', 'Rock', 'Bug', 'Ghost', 'Ghost', 'Bug', 'Grass', 'Psychic', 'Rock', 'Steel', 'Ghost', 'Electric', 'Electric', 'Water', 'Ground', 'Poison', 'Normal', 'Fighting', 'Dark', 'Fairy', 'Grass', 'Poison', 'Normal', 'Fighting', 'Bug', 'Normal', 'Normal', 'Bug', 'Water', 'Bug', 'Fighting', 'Psychic', 'Water', 'Poison', 'Steel', 'Fighting', 'Psychic', 'Fighting', 'Dragon', 'Bug', 'Fire', 'Psychic', 'Grass', 'Normal', 'Normal', 'Poison', 'Bug', 'Water', 'Ground', 'Bug', 'Water', 'Psychic', 'Normal', 'Steel', 'Rock', 'Dragon', 'Grass', 'Grass', 'Water', 'Fighting', 'Ground', 'Fairy', 'Normal', 'Grass', 'Electric', 'Water', 'Fighting', 'Rock', 'Fire', 'Rock', 'Rock', 'Water', 'Grass', 'Fighting', 'Water', 'Bug', 'Bug', 'Grass']
names = ['Seel', 'Nidorino', 'Fearow', 'Vanilluxe', 'Relicanth', 'Karrablast', 'Exeggutor', 'Diggersby', 'Mew', 'Flabébé', 'Archen', 'Cryogonal', 'Cherubi', 'Barbaracle', 'Jirachi', 'Lopunny', 'Sentret', 'Heatmor', 'Bellossom', 'Drilbur', 'Gallade', 'Ivysaur', 'Sandslash', 'Aipom', 'Scatterbug', 'Carracosta', 'Frillish', 'Honedge', 'Gogoat', 'Kangaskhan', 'Hippowdon', 'Lillipup', 'Braixen', 'Wooper', 'Helioptile', 'Geodude', 'Claydol', 'Furret', 'Burmy', 'Clefairy', 'Sandile', 'Walrein', 'Throh', 'Leavanny', 'Gengar', 'Solosis', 'Eelektross', 'Foongus', 'Ferroseed', 'Sylveon', 'Marowak', 'Wailord', 'Chimchar', 'Tyrunt', 'Golem', 'Mamoswine', 'Elgyem', 'Metagross', 'Panpour', 'Cinccino', 'Gloom', 'Chatot', 'Onix', 'Dodrio', 'Chandelure', 'Florges', 'Lilligant', 'Graveler', 'Raichu', 'Sylveon', 'Minccino', 'Scolipede', 'Cresselia', 'Delphox', 'Wigglytuff', 'Seadra', 'Shellos', 'Lampent', 'Infernape', 'Sawsbuck', 'Delphox', 'Delibird', 'Slaking', 'Stunfisk', 'Spritzee', 'Lillipup', 'Sharpedo', 'Gallade', 'Beheeyem', 'Charmander', 'Krookodile', 'Braixen', 'Bellsprout', 'Snorlax', 'Swinub', 'Hariyama', 'Numel', 'Gardevoir', 'Mismagius', 'WormadamTrash Cloak', 'Dugtrio', 'Wailmer', 'Diggersby', 'Castform', 'Bisharp', 'Lileep', 'Eelektross', 'Zigzagoon', 'Tropius', 'Venomoth', 'Vibrava', 'MeowsticFemale', 'Shieldon', 'Floatzel', 'Carnivine', 'Servine', 'Swalot', 'Finneon', 'Magnezone', 'Combusken', 'DarmanitanStandard Mode', 'Cryogonal', 'Wynaut', 'Emboar', 'Hippopotas', 'Krabby', 'Tentacruel', 'Ludicolo', 'Bisharp', 'Claydol', 'Corsola', 'Shelmet', 'Bastiodon', 'Snorunt', 'Yanma', 'Lumineon', 'Treecko', 'Zekrom', 'Azurill', 'Golduck', 'Phanpy', 'WormadamSandy Cloak', 'Aron', 'Panpour', 'Illumise', 'Zekrom', 'Shinx', 'Kabutops', 'Delibird', 'Carnivine', 'Beautifly', 'Klang', 'Patrat', 'Exeggutor', 'RotomWash Rotom', 'Dragalge', 'Kirlia', 'Dedenne', 'Electrike', 'Cherrim', 'Venomoth', 'Scolipede', 'Swirlix', 'Primeape', 'Simipour', 'Skuntank', 'Glameow', 'Clamperl', 'Swablu', 'Cofagrigus', 'Hoppip', 'Torchic', 'Psyduck', 'Helioptile', 'Larvesta', 'Wigglytuff', 'Mandibuzz', 'Empoleon', 'Shelgon', 'Spewpa', 'Charizard', 'Clamperl', 'Seedot', 'Spritzee', 'Darkrai', 'Electrike', 'Virizion', 'Yanmega', 'Girafarig', 'Cranidos', 'Croagunk', 'Nidoking', 'Pupitar', 'Tympole', 'Flareon', 'Lairon', 'Frogadier', 'Mime Jr.', 'Magnemite', 'Clefable', 'Gloom', 'Exeggcute', 'Bayleef', 'Staravia', 'Rattata', 'Golem', 'Gible', 'Kricketune', 'Seismitoad', 'Slakoth', 'Dragonair', 'Skuntank', 'Munna', 'Cacturne', 'Magmortar', 'Golbat', 'Shroomish', 'Leafeon', 'Ledian', 'Cinccino', 'Armaldo', 'Froslass', 'Seadra', 'Slowbro', 'Nidorino', 'KyuremBlack Kyurem', 'Venomoth', 'Carnivine', 'Abomasnow', 'Zangoose', 'Honchkrow', 'Banette', 'Panpour', 'Beldum', 'Ampharos', 'Wynaut', 'Medicham', 'Seviper', 'Blissey', 'Azelf', "Farfetch'd", 'Relicanth', 'WormadamPlant Cloak', 'Sneasel', 'Fletchling', 'Larvesta', 'Cleffa', 'Mienfoo', 'Panpour',
         'Arcanine', 'Hitmonchan', 'Tangela', 'Escavalier', 'Lumineon', 'Kingdra', 'Lickilicky', 'Noctowl', 'Blissey', 'Zekrom', 'Amoonguss', 'Carracosta', 'Staravia', 'Pineco', 'Swampert', 'Jirachi', 'Swanna', 'Drifblim', 'Roggenrola', 'Inkay', 'Electrike', 'Cubone', 'Crobat', 'Prinplup', 'Spinarak', 'Lilligant', 'Poliwhirl', 'Vespiquen', 'Loudred', 'Grimer', 'Kadabra', 'Caterpie', 'Machop', 'Slakoth', 'Foongus', 'Exeggcute', 'Gulpin', 'Delcatty', 'GroudonPrimal Groudon', 'Delcatty', 'Shelmet', 'Granbull', 'Shelmet', 'Bronzong', 'Tyranitar', 'Azumarill', 'Numel', 'Pyroar', 'Mantyke', 'Chikorita', 'Articuno', 'Umbreon', 'Musharna', 'Jellicent', 'Spheal', 'Kadabra', 'Nosepass', 'Cobalion', 'Ducklett', 'Tirtouga', 'Accelgor', 'Fletchling', 'KyuremWhite Kyurem', 'Slowbro', 'Zebstrika', 'Dugtrio', 'Stoutland', 'Shelmet', 'Dragonair', 'Hawlucha', 'RotomFrost Rotom', 'Gardevoir', 'Primeape', 'Swirlix', 'Gothita', 'Krabby', 'Chimchar', 'Aurorus', 'Mandibuzz', 'Nidoqueen', 'Delibird', 'Fraxure', 'Pidove', 'Altaria', 'Oddish', 'Blitzle', 'Ducklett', 'Ralts', 'Baltoy', 'Jirachi', 'Avalugg', 'Clefable', 'Gurdurr', 'Seel', 'Baltoy', 'Vigoroth', 'Stunky', 'Klinklang', 'Luvdisc', 'Mew', 'Sandshrew', 'Koffing', 'Pancham', 'Kirlia', 'Jirachi', 'Probopass', 'Tympole', 'Spoink', 'Basculin', 'Drifblim', 'Duosion', 'Primeape', 'Shelmet', 'Whirlipede', 'Roselia', 'Rufflet', 'Avalugg', 'Druddigon', 'Luxray', 'Eelektrik', 'Chespin', 'Clefable', 'Graveler', 'Chatot', 'Psyduck', 'Makuhita', 'Piplup', 'Pinsir', 'Lopunny', 'Tauros', 'Grimer', 'Eelektross', 'Turtwig', 'Darkrai', 'Emboar', 'Cobalion', 'Talonflame', 'Nidorino', 'Dragonair', 'Larvitar', 'WormadamSandy Cloak', 'Wobbuffet', 'Maractus', 'Teddiursa', 'Leavanny', 'Lampent', 'Yveltal', 'Primeape', 'Plusle', 'Altaria', 'Zweilous', 'Bunnelby', 'Riolu', 'Manectric', 'Lunatone', 'Wigglytuff', 'Bouffalant', 'Leavanny', 'Cyndaquil', 'Clamperl', 'Minccino', 'Groudon', 'Scatterbug', 'Torkoal', 'Scolipede', 'Slowking', 'Rapidash', 'Ledian', 'Cofagrigus', 'Ledian', 'Mawile', 'Sealeo', 'Lickitung', 'Sharpedo', 'Kabutops', 'Beedrill', 'Spiritomb', 'Dusclops', 'Venomoth', 'Nuzleaf', 'Gothita', 'Onix', 'Aron', 'Trevenant', 'Electivire', 'Blitzle', 'Feraligatr', 'Donphan', 'Skrelp', 'Ursaring', 'Hitmontop', 'Hydreigon', 'Spritzee', 'Jumpluff', 'Arbok', 'Taillow', 'Gurdurr', 'Dustox', 'Zangoose', 'Sawsbuck', 'Volcarona', 'Simipour', 'Shedinja', 'Mienfoo', 'Wobbuffet', 'Mantine', 'Croagunk', 'Bronzor', 'Meditite', 'Elgyem', 'Hawlucha', 'Dratini', 'WormadamTrash Cloak', 'Moltres', 'Mr. Mime', 'Roserade', 'Dunsparce', 'Skitty', 'Skuntank', 'Joltik', 'Slowking', 'Rhyperior', 'Beautifly', 'Kyogre', 'Gallade', 'Azurill', 'Aggron', 'Solrock', 'Salamence', 'Weepinbell', 'Skiploom', 'Marshtomp', 'Mienshao', 'Krookodile', 'Xerneas', 'Staraptor', 'Shiftry', 'Eelektross', 'Dewott', 'Throh', 'Barbaracle', 'Ninetales', 'Sudowoodo', 'Nosepass', 'Staryu', 'Snivy', 'Hawlucha', 'Suicune', 'Weedle', 'Nincada', 'Simisage']

print('*******************')
# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')
print('*******************')
# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')
print('*******************')
# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)
print('*******************')

# Combinations

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')
print('*******************')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')
print('*******************')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)
print('*******************')

# Using sets.

ash_pokedex = {'Pikachu', 'Bulbasaur', 'Koffing', 'Spearow',
               'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle'}
misty_pokedex = {'Krabby', 'Horsea', 'Slowbro', 'Tentacool',
                 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle'}
brock_pokedex = {'Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix',
                 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio'}

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)
print('*******************')
# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)
print('*******************')
# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)
print('*******************')

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)
print('*******************')

# No Loop

poke_names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola', 'Altaria', 'Amaura', 'Ambipom', 'Amoonguss', 'Ampharos', 'Anorith', 'Arbok', 'Arcanine', 'Arceus', 'Archen', 'Archeops', 'Ariados', 'Armaldo', 'Aromatisse', 'Aron', 'Articuno', 'Audino', 'Aurorus', 'Avalugg', 'Axew', 'Azelf', 'Azumarill', 'Azurill', 'Bagon', 'Baltoy', 'Banette', 'Barbaracle', 'Barboach', 'Basculin', 'Bastiodon', 'Bayleef', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem', 'Beldum', 'Bellossom', 'Bellsprout', 'Bergmite', 'Bibarel', 'Bidoof', 'Binacle', 'Bisharp', 'Blastoise', 'Blaziken', 'Blissey', 'Blitzle', 'Boldore', 'Bonsly', 'Bouffalant', 'Braixen', 'Braviary', 'Breloom', 'Bronzong', 'Bronzor', 'Budew', 'Buizel', 'Bulbasaur', 'Buneary', 'Bunnelby', 'Burmy', 'Butterfree', 'Cacnea', 'Cacturne', 'Camerupt', 'Carbink', 'Carnivine', 'Carracosta', 'Carvanha', 'Cascoon', 'Castform', 'Caterpie', 'Celebi', 'Chandelure', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Chatot', 'Cherrim', 'Cherubi', 'Chesnaught', 'Chespin', 'Chikorita', 'Chimchar', 'Chimecho', 'Chinchou', 'Chingling', 'Cinccino', 'Clamperl', 'Clauncher', 'Clawitzer', 'Claydol', 'Clefable', 'Clefairy', 'Cleffa', 'Cloyster', 'Cobalion', 'Cofagrigus', 'Combee', 'Combusken', 'Conkeldurr', 'Corphish', 'Corsola', 'Cottonee', 'Cradily', 'Cranidos', 'Crawdaunt', 'Cresselia', 'Croagunk', 'Crobat', 'Croconaw', 'Crustle', 'Cryogonal', 'Cubchoo', 'Cubone', 'Cyndaquil', 'Darkrai', 'DarmanitanStandard Mode', 'DarmanitanZen Mode', 'Darumaka', 'Dedenne', 'Deerling', 'Deino', 'Delcatty', 'Delibird', 'Delphox', 'Dewgong', 'Dewott', 'Dialga', 'Diancie', 'Diggersby', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Donphan', 'Doublade', 'Dragalge', 'Dragonair', 'Dragonite', 'Drapion', 'Dratini', 'Drifblim', 'Drifloon', 'Drilbur', 'Drowzee', 'Druddigon', 'Ducklett', 'Dugtrio', 'Dunsparce', 'Duosion', 'Durant', 'Dusclops', 'Dusknoir', 'Duskull', 'Dustox', 'Dwebble', 'Eelektrik', 'Eelektross', 'Eevee', 'Ekans', 'Electabuzz', 'Electivire', 'Electrike', 'Electrode', 'Elekid', 'Elgyem', 'Emboar', 'Emolga', 'Empoleon', 'Entei', 'Escavalier', 'Espeon', 'Espurr', 'Excadrill', 'Exeggcute', 'Exeggutor', 'Exploud', "Farfetch'd", 'Fearow', 'Feebas', 'Fennekin', 'Feraligatr', 'Ferroseed', 'Ferrothorn', 'Finneon', 'Flaaffy', 'Flabébé', 'Flareon', 'Fletchinder', 'Fletchling', 'Floatzel', 'Floette', 'Florges', 'Flygon', 'Foongus', 'Forretress', 'Fraxure', 'Frillish', 'Froakie', 'Frogadier', 'Froslass', 'Furfrou', 'Furret', 'Gabite', 'Gallade', 'Galvantula', 'Garbodor', 'Garchomp', 'Gardevoir', 'Gastly', 'Gastrodon', 'Genesect', 'Gengar', 'Geodude', 'Gible', 'Gigalith', 'Girafarig', 'Glaceon', 'Glalie', 'Glameow', 'Gligar', 'Gliscor', 'Gloom', 'Gogoat', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Golett', 'Golurk', 'Goodra', 'Goomy', 'Gorebyss', 'Gothita', 'Gothitelle', 'Gothorita', 'Granbull', 'Graveler', 'Greninja', 'Grimer', 'Grotle', 'Groudon', 'GroudonPrimal Groudon', 'Grovyle', 'Growlithe', 'Grumpig', 'Gulpin', 'Gurdurr', 'Gyarados', 'Happiny', 'Hariyama', 'Haunter', 'Hawlucha', 'Haxorus', 'Heatmor', 'Heatran', 'Heliolisk', 'Helioptile', 'Heracross', 'Herdier', 'Hippopotas', 'Hippowdon', 'Hitmonchan', 'Hitmonlee', 'Hitmontop', 'Ho-oh', 'Honchkrow', 'Honedge', 'Hoothoot', 'Hoppip', 'Horsea', 'Houndoom', 'Houndour', 'Huntail', 'Hydreigon', 'Hypno', 'Igglybuff', 'Illumise', 'Infernape', 'Inkay', 'Ivysaur', 'Jellicent', 'Jigglypuff', 'Jirachi', 'Jolteon', 'Joltik', 'Jumpluff', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Karrablast', 'Kecleon', 'Kingdra', 'Kingler', 'Kirlia', 'Klang', 'Klefki', 'Klink', 'Klinklang', 'Koffing', 'Krabby', 'Kricketot', 'Kricketune', 'Krokorok', 'Krookodile', 'Kyogre', 'KyogrePrimal Kyogre', 'Kyurem', 'KyuremBlack Kyurem', 'KyuremWhite Kyurem', 'Lairon', 'Lampent', 'Lanturn', 'Lapras', 'Larvesta', 'Larvitar', 'Latias', 'Latios', 'Leafeon', 'Leavanny', 'Ledian', 'Ledyba', 'Lickilicky', 'Lickitung', 'Liepard', 'Lileep', 'Lilligant', 'Lillipup', 'Linoone', 'Litleo', 'Litwick', 'Lombre', 'Lopunny', 'Lotad', 'Loudred', 'Lucario', 'Ludicolo', 'Lugia', 'Lumineon', 'Lunatone', 'Luvdisc', 'Luxio', 'Luxray', 'Machamp', 'Machoke',
              'Machop', 'Magby', 'Magcargo', 'Magikarp', 'Magmar', 'Magmortar', 'Magnemite', 'Magneton', 'Magnezone', 'Makuhita', 'Malamar', 'Mamoswine', 'Manaphy', 'Mandibuzz', 'Manectric', 'Mankey', 'Mantine', 'Mantyke', 'Maractus', 'Mareep', 'Marill', 'Marowak', 'Marshtomp', 'Masquerain', 'Mawile', 'Medicham', 'Meditite', 'MeowsticFemale', 'MeowsticMale', 'Meowth', 'Mesprit', 'Metagross', 'Metang', 'Metapod', 'Mew', 'Mewtwo', 'Mienfoo', 'Mienshao', 'Mightyena', 'Milotic', 'Miltank', 'Mime Jr.', 'Minccino', 'Minun', 'Misdreavus', 'Mismagius', 'Moltres', 'Monferno', 'Mothim', 'Mr. Mime', 'Mudkip', 'Muk', 'Munchlax', 'Munna', 'Murkrow', 'Musharna', 'Natu', 'Nidoking', 'Nidoqueen', 'Nidoran♀', 'Nidoran♂', 'Nidorina', 'Nidorino', 'Nincada', 'Ninetales', 'Ninjask', 'Noctowl', 'Noibat', 'Noivern', 'Nosepass', 'Numel', 'Nuzleaf', 'Octillery', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Oshawott', 'Pachirisu', 'Palkia', 'Palpitoad', 'Pancham', 'Pangoro', 'Panpour', 'Pansage', 'Pansear', 'Paras', 'Parasect', 'Patrat', 'Pawniard', 'Pelipper', 'Persian', 'Petilil', 'Phanpy', 'Phantump', 'Phione', 'Pichu', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pidove', 'Pignite', 'Pikachu', 'Piloswine', 'Pineco', 'Pinsir', 'Piplup', 'Plusle', 'Politoed', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Poochyena', 'Porygon', 'Porygon-Z', 'Porygon2', 'Primeape', 'Prinplup', 'Probopass', 'Psyduck', 'Pupitar', 'Purrloin', 'Purugly', 'Pyroar', 'Quagsire', 'Quilava', 'Quilladin', 'Qwilfish', 'Raichu', 'Raikou', 'Ralts', 'Rampardos', 'Rapidash', 'Raticate', 'Rattata', 'Rayquaza', 'Regice', 'Regigigas', 'Regirock', 'Registeel', 'Relicanth', 'Remoraid', 'Reshiram', 'Reuniclus', 'Rhydon', 'Rhyhorn', 'Rhyperior', 'Riolu', 'Roggenrola', 'Roselia', 'Roserade', 'Rotom', 'RotomFan Rotom', 'RotomFrost Rotom', 'RotomHeat Rotom', 'RotomMow Rotom', 'RotomWash Rotom', 'Rufflet', 'Sableye', 'Salamence', 'Samurott', 'Sandile', 'Sandshrew', 'Sandslash', 'Sawk', 'Sawsbuck', 'Scatterbug', 'Sceptile', 'Scizor', 'Scolipede', 'Scrafty', 'Scraggy', 'Scyther', 'Seadra', 'Seaking', 'Sealeo', 'Seedot', 'Seel', 'Seismitoad', 'Sentret', 'Serperior', 'Servine', 'Seviper', 'Sewaddle', 'Sharpedo', 'Shedinja', 'Shelgon', 'Shellder', 'Shellos', 'Shelmet', 'Shieldon', 'Shiftry', 'Shinx', 'Shroomish', 'Shuckle', 'Shuppet', 'Sigilyph', 'Silcoon', 'Simipour', 'Simisage', 'Simisear', 'Skarmory', 'Skiddo', 'Skiploom', 'Skitty', 'Skorupi', 'Skrelp', 'Skuntank', 'Slaking', 'Slakoth', 'Sliggoo', 'Slowbro', 'Slowking', 'Slowpoke', 'Slugma', 'Slurpuff', 'Smeargle', 'Smoochum', 'Sneasel', 'Snivy', 'Snorlax', 'Snorunt', 'Snover', 'Snubbull', 'Solosis', 'Solrock', 'Spearow', 'Spewpa', 'Spheal', 'Spinarak', 'Spinda', 'Spiritomb', 'Spoink', 'Spritzee', 'Squirtle', 'Stantler', 'Staraptor', 'Staravia', 'Starly', 'Starmie', 'Staryu', 'Steelix', 'Stoutland', 'Stunfisk', 'Stunky', 'Sudowoodo', 'Suicune', 'Sunflora', 'Sunkern', 'Surskit', 'Swablu', 'Swadloon', 'Swalot', 'Swampert', 'Swanna', 'Swellow', 'Swinub', 'Swirlix', 'Swoobat', 'Sylveon', 'Taillow', 'Talonflame', 'Tangela', 'Tangrowth', 'Tauros', 'Teddiursa', 'Tentacool', 'Tentacruel', 'Tepig', 'Terrakion', 'Throh', 'Timburr', 'Tirtouga', 'Togekiss', 'Togepi', 'Togetic', 'Torchic', 'Torkoal', 'Torterra', 'Totodile', 'Toxicroak', 'Tranquill', 'Trapinch', 'Treecko', 'Trevenant', 'Tropius', 'Trubbish', 'Turtwig', 'Tympole', 'Tynamo', 'Typhlosion', 'Tyranitar', 'Tyrantrum', 'Tyrogue', 'Tyrunt', 'Umbreon', 'Unfezant', 'Unown', 'Ursaring', 'Uxie', 'Vanillish', 'Vanillite', 'Vanilluxe', 'Vaporeon', 'Venipede', 'Venomoth', 'Venonat', 'Venusaur', 'Vespiquen', 'Vibrava', 'Victini', 'Victreebel', 'Vigoroth', 'Vileplume', 'Virizion', 'Vivillon', 'Volbeat', 'Volcanion', 'Volcarona', 'Voltorb', 'Vullaby', 'Vulpix', 'Wailmer', 'Wailord', 'Walrein', 'Wartortle', 'Watchog', 'Weavile', 'Weedle', 'Weepinbell', 'Weezing', 'Whimsicott', 'Whirlipede', 'Whiscash', 'Whismur', 'Wigglytuff', 'Wingull', 'Wobbuffet', 'Woobat', 'Wooper', 'WormadamPlant Cloak', 'WormadamSandy Cloak', 'WormadamTrash Cloak', 'Wurmple', 'Wynaut', 'Xatu', 'Xerneas', 'Yamask', 'Yanma', 'Yanmega', 'Yveltal', 'Zangoose', 'Zapdos', 'Zebstrika', 'Zekrom', 'Zigzagoon', 'Zoroark', 'Zorua', 'Zubat', 'Zweilous']
poke_gens = [4, 1, 3, 5, 1, 3, 2, 1, 5, 3, 6, 4, 5, 2, 3, 1, 1, 4, 5, 5, 2, 3, 6, 3, 1, 5, 6, 6, 5, 4, 2, 3, 3, 3, 3, 6, 3, 5, 4, 2, 5, 3, 1, 5, 3, 2, 1, 6, 4, 4, 6, 5, 1, 3, 2, 5, 5, 4, 5, 6, 5, 3, 4, 4, 4, 4, 1, 4, 6, 4, 1, 3, 3, 3, 6, 4, 5, 3, 3, 3, 1, 2, 5, 1, 1, 1, 1, 4, 4, 4, 6, 6, 2, 4, 3, 2, 4, 5, 3, 6, 6, 3, 1, 1, 2, 1, 5, 5, 4, 3, 5, 3, 2, 5, 3, 4, 3, 4, 4, 2, 2, 5, 5, 5, 1, 2, 4, 5, 5, 5, 6, 5, 5, 3, 2, 6, 1, 5, 4, 6, 6, 1, 1, 1, 1, 2, 6, 6, 1, 1, 4, 1, 4, 4, 5, 1, 5, 5, 1, 2, 5, 5, 3, 4, 3, 3, 5, 5, 5, 1, 1, 1, 4, 3, 1, 2, 5, 5, 5, 4, 2, 5, 2, 6, 5, 1, 1, 3, 1, 1, 3, 6, 2, 5, 5, 4, 2, 6, 1, 6, 6, 4, 6, 6, 3, 5, 2, 5, 5, 6, 6, 4, 6, 2, 4, 4, 5, 5, 4, 3, 1, 4, 5, 1, 1, 4, 5, 2, 4, 3, 4, 2, 4, 1, 6, 1, 1, 1, 1, 5, 5, 6, 6, 3, 5, 5, 5, 2, 1, 6, 1, 4, 3, 3, 3, 1, 3, 3, 5, 1, 4, 3, 1, 6, 5, 5, 4, 6, 6, 2, 5, 4, 4, 1, 1, 2, 2, 4, 6, 2, 2, 1, 2, 2, 3, 5, 1, 2, 3, 4, 6, 1, 5, 1, 3, 1, 5, 2, 1, 1, 1, 1, 1, 1, 5, 3, 2, 1, 3, 5, 6, 5, 5, 1, 1, 4, 4, 5, 5, 3, 3, 5, 5, 5, 3, 5, 2, 1, 5, 2, 3, 3, 4, 5, 2, 2, 4, 1, 5, 3, 5, 5, 3, 6, 5, 3, 4, 3, 3, 4, 3, 2, 4, 3, 3, 4, 4, 1,
             1, 1, 2, 2, 1, 1, 4, 1, 1, 4, 3, 6, 4, 4, 5, 3, 1, 2, 4, 5, 2, 2, 1, 3, 3, 3, 3, 3, 6, 6, 1, 4, 3, 3, 1, 1, 1, 5, 5, 3, 3, 2, 4, 5, 3, 2, 4, 1, 4, 4, 1, 3, 1, 4, 5, 2, 5, 2, 1, 1, 1, 1, 1, 1, 3, 1, 3, 2, 6, 6, 3, 3, 3, 2, 1, 1, 1, 1, 5, 4, 4, 5, 6, 6, 5, 5, 5, 1, 1, 5, 5, 3, 1, 5, 2, 6, 4, 2, 1, 1, 1, 5, 5, 1, 2, 2, 1, 4, 3, 2, 1, 1, 1, 1, 3, 1, 4, 2, 1, 4, 4, 1, 2, 5, 4, 6, 2, 2, 6, 2, 1, 2, 3, 4, 1, 1, 1, 3, 3, 4, 3, 3, 3, 2, 5, 5, 1, 1, 4, 4, 5, 3, 4, 4, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 1, 1, 5, 5, 6, 3, 2, 5, 5, 5, 1, 1, 1, 3, 3, 1, 5, 2, 5, 5, 3, 5, 3, 3, 3, 1, 4, 5, 4, 3, 4, 3, 2, 3, 5, 3, 5, 5, 5, 2, 6, 2, 3, 4, 6, 4, 3, 3, 6, 1, 2, 1, 2, 6, 2, 2, 2, 5, 1, 3, 4, 2, 5, 3, 1, 6, 3, 2, 3, 4, 3, 6, 1, 2, 4, 4, 4, 1, 1, 2, 5, 5, 4, 2, 2, 2, 2, 3, 3, 5, 3, 3, 5, 3, 2, 6, 5, 6, 3, 6, 1, 4, 1, 2, 1, 1, 5, 5, 5, 5, 5, 4, 2, 2, 3, 3, 4, 2, 4, 5, 3, 3, 6, 3, 5, 4, 5, 5, 2, 2, 6, 2, 6, 2, 5, 2, 2, 4, 5, 5, 5, 1, 5, 1, 1, 1, 4, 3, 5, 1, 3, 1, 5, 6, 3, 6, 5, 1, 5, 1, 3, 3, 3, 1, 5, 4, 1, 1, 1, 5, 5, 3, 3, 1, 3, 2, 5, 2, 4, 4, 4, 3, 3, 2, 6, 5, 2, 4, 6, 3, 1, 5, 5, 3, 5, 5, 1, 5]


# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name, gen in zip(
    poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths[:5])
print('*******************')

# Efficient loop

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen, count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
print('*******************')

pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting']
# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

# Pandas DataFrame Optimization

pit_df = []  # Only created as dummy, real DF is below.
'''
  Team League  Year   RS   RA   W    G  Playoffs
0  SFG     NL  2012  718  649  94  162         1
1  SFG     NL  2011  570  578  86  162         0
2  SFG     NL  2010  697  583  92  162         1
3  SFG     NL  2009  657  611  88  162         0
4  SFG     NL  2008  640  759  72  162         0
'''

# Iterate over pit_df and print each index variable, row, and row type
for i, row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

'''
0
Team         PIT
League        NL
Year        2012
RS           651
RA           674
W             79
G            162
Playoffs       0
Name: 0, dtype: object
<class 'pandas.core.series.Series'>

1
Team         PIT
League        NL
Year        2011
RS           610
RA           712
W             72
G            162
Playoffs       0
Name: 1, dtype: object
<class 'pandas.core.series.Series'>

2
Team         PIT
League        NL
Year        2010
RS           587
RA           866
W             57
G            162
Playoffs       0
Name: 2, dtype: object
<class 'pandas.core.series.Series'>

3
Team         PIT
League        NL
Year        2009
RS           636
RA           768
W             62
G            161
Playoffs       0
Name: 3, dtype: object
<class 'pandas.core.series.Series'>

4
Team         PIT
League        NL
Year        2008
RS           735
RA           884
W             67
G            162
Playoffs       0
Name: 4, dtype: object
<class 'pandas.core.series.Series'>
'''

giants_df = []  # Only created as dummy, real DF is below.
'''
  Team League  Year   RS   RA   W    G  Playoffs
0  SFG     NL  2012  718  649  94  162         1
1  SFG     NL  2011  570  578  86  162         0
2  SFG     NL  2010  697  583  92  162         1
3  SFG     NL  2009  657  611  88  162         0
4  SFG     NL  2008  640  759  72  162         0
'''

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i, row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']

    run_diff = runs_scored - runs_allowed

    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

'''
    Team League  Year   RS   RA   W    G  Playoffs   RD
0  SFG     NL  2012  718  649  94  162         1   69
1  SFG     NL  2011  570  578  86  162         0   -8
2  SFG     NL  2010  697  583  92  162         1  114
3  SFG     NL  2009  657  611  88  162         0   46
4  SFG     NL  2008  640  759  72  162         0 -119
'''

# Tuples with Pandas

rangers_df = []

# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
    print(row)

'''
Pandas(Index=0, Team='TEX', League='AL', Year=2012, RS=808, RA=707, W=93, G=162, Playoffs=1)
Pandas(Index=1, Team='TEX', League='AL', Year=2011, RS=855, RA=677, W=96, G=162, Playoffs=1)
Pandas(Index=2, Team='TEX', League='AL', Year=2010, RS=787, RA=687, W=90, G=162, Playoffs=1)
Pandas(Index=3, Team='TEX', League='AL', Year=2009, RS=784, RA=740, W=87, G=162, Playoffs=0)
Pandas(Index=4, Team='TEX', League='AL', Year=2008, RS=901, RA=967, W=79, G=162, Playoffs=0)
Pandas(Index=5, Team='TEX', League='AL', Year=2007, RS=816, RA=844, W=75, G=162, Playoffs=0)
Pandas(Index=6, Team='TEX', League='AL', Year=2006, RS=835, RA=784, W=80, G=162, Playoffs=0)
Pandas(Index=7, Team='TEX', League='AL', Year=2005, RS=865, RA=858, W=79, G=162, Playoffs=0)
Pandas(Index=8, Team='TEX', League='AL', Year=2004, RS=860, RA=794, W=89, G=162, Playoffs=0)
Pandas(Index=9, Team='TEX', League='AL', Year=2003, RS=826, RA=969, W=71, G=162, Playoffs=0)
Pandas(Index=10, Team='TEX', League='AL', Year=2002, RS=843, RA=882, W=72, G=162, Playoffs=0)
Pandas(Index=11, Team='TEX', League='AL', Year=2001, RS=890, RA=968, W=73, G=162, Playoffs=0)
Pandas(Index=12, Team='TEX', League='AL', Year=2000, RS=848, RA=974, W=71, G=162, Playoffs=0)
Pandas(Index=13, Team='TEX', League='AL', Year=1999, RS=945, RA=859, W=95, G=162, Playoffs=1)
Pandas(Index=14, Team='TEX', League='AL', Year=1998, RS=940, RA=871, W=88, G=162, Playoffs=1)
Pandas(Index=15, Team='TEX', League='AL', Year=1997, RS=807, RA=823, W=77, G=162, Playoffs=0)
Pandas(Index=16, Team='TEX', League='AL', Year=1996, RS=928, RA=799, W=90, G=163, Playoffs=1)
Pandas(Index=17, Team='TEX', League='AL', Year=1993, RS=835, RA=751, W=86, G=162, Playoffs=0)
Pandas(Index=18, Team='TEX', League='AL', Year=1992, RS=682, RA=753, W=77, G=162, Playoffs=0)
Pandas(Index=19, Team='TEX', League='AL', Year=1991, RS=829, RA=814, W=85, G=162, Playoffs=0)
Pandas(Index=20, Team='TEX', League='AL', Year=1990, RS=676, RA=696, W=83, G=162, Playoffs=0)
Pandas(Index=21, Team='TEX', League='AL', Year=1989, RS=695, RA=714, W=83, G=162, Playoffs=0)
Pandas(Index=22, Team='TEX', League='AL', Year=1988, RS=637, RA=735, W=70, G=161, Playoffs=0)
Pandas(Index=23, Team='TEX', League='AL', Year=1987, RS=823, RA=849, W=75, G=162, Playoffs=0)
Pandas(Index=24, Team='TEX', League='AL', Year=1986, RS=771, RA=743, W=87, G=162, Playoffs=0)
Pandas(Index=25, Team='TEX', League='AL', Year=1985, RS=617, RA=785, W=62, G=161, Playoffs=0)
Pandas(Index=26, Team='TEX', League='AL', Year=1984, RS=656, RA=714, W=69, G=161, Playoffs=0)
Pandas(Index=27, Team='TEX', League='AL', Year=1983, RS=639, RA=609, W=77, G=163, Playoffs=0)
Pandas(Index=28, Team='TEX', League='AL', Year=1982, RS=590, RA=749, W=64, G=162, Playoffs=0)
Pandas(Index=29, Team='TEX', League='AL', Year=1980, RS=756, RA=752, W=76, G=163, Playoffs=0)
Pandas(Index=30, Team='TEX', League='AL', Year=1979, RS=750, RA=698, W=83, G=162, Playoffs=0)
Pandas(Index=31, Team='TEX', League='AL', Year=1978, RS=692, RA=632, W=87, G=162, Playoffs=0)
Pandas(Index=32, Team='TEX', League='AL', Year=1977, RS=767, RA=657, W=94, G=162, Playoffs=0)
Pandas(Index=33, Team='TEX', League='AL', Year=1976, RS=616, RA=652, W=76, G=162, Playoffs=0)
Pandas(Index=34, Team='TEX', League='AL', Year=1975, RS=714, RA=733, W=79, G=162, Playoffs=0)
Pandas(Index=35, Team='TEX', League='AL', Year=1974, RS=690, RA=698, W=83, G=161, Playoffs=0)
Pandas(Index=36, Team='TEX', League='AL', Year=1973, RS=619, RA=844, W=57, G=162, Playoffs=0)
'''

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W
    print(i, year, wins)

'''
    0 2012 93
    1 2011 96
    2 2010 90
    3 2009 87
    4 2008 79
    5 2007 75
    6 2006 80
    7 2005 79
    8 2004 89
    9 2003 71
    10 2002 72
    11 2001 73
    12 2000 71
    13 1999 95
    14 1998 88
    15 1997 77
    16 1996 90
    17 1993 86
    18 1992 77
    19 1991 85
    20 1990 83
    21 1989 83
    22 1988 70
    23 1987 75
    24 1986 87
    25 1985 62
    26 1984 69
    27 1983 77
    28 1982 64
    29 1980 76
    30 1979 83
    31 1978 87
    32 1977 94
    33 1976 76
    34 1975 79
    35 1974 83
    36 1973 57
'''
yankees_df = []

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = runs_scored - runs_allowed

    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

'''
       Team League  Year   RS   RA    W    G  Playoffs   RD
    0   NYY     AL  2012  804  668   95  162         1  136
    1   NYY     AL  2011  867  657   97  162         1  210
    2   NYY     AL  2010  859  693   95  162         1  166
    3   NYY     AL  2009  915  753  103  162         1  162
    4   NYY     AL  2008  789  727   89  162         0   62
    5   NYY     AL  2007  968  777   94  162         1  191
    6   NYY     AL  2006  930  767   97  162         1  163
    7   NYY     AL  2005  886  789   95  162         1   97
    8   NYY     AL  2004  897  808  101  162         1   89
    9   NYY     AL  2003  877  716  101  163         1  161
    10  NYY     AL  2002  897  697  103  161         1  200
    11  NYY     AL  2001  804  713   95  161         1   91
    12  NYY     AL  2000  871  814   87  161         1   57
    13  NYY     AL  1999  900  731   98  162         1  169
    14  NYY     AL  1998  965  656  114  162         1  309
    15  NYY     AL  1997  891  688   96  162         1  203
    16  NYY     AL  1996  871  787   92  162         1   84
    17  NYY     AL  1993  821  761   88  162         0   60
    18  NYY     AL  1992  733  746   76  162         0  -13
    19  NYY     AL  1991  674  777   71  162         0 -103
    20  NYY     AL  1990  603  749   67  162         0 -146
    21  NYY     AL  1989  698  792   74  161         0  -94
    22  NYY     AL  1988  772  748   85  161         0   24
    23  NYY     AL  1987  788  758   89  162         0   30
    24  NYY     AL  1986  797  738   90  162         0   59
    25  NYY     AL  1985  839  660   97  161         0  179
    26  NYY     AL  1984  758  679   87  162         0   79
    27  NYY     AL  1983  770  703   91  162         0   67
    28  NYY     AL  1982  709  716   79  162         0   -7
    29  NYY     AL  1980  820  662  103  162         1  158
    30  NYY     AL  1979  734  672   89  160         0   62
    31  NYY     AL  1978  735  582  100  163         1  153
    32  NYY     AL  1977  831  651  100  162         1  180
    33  NYY     AL  1976  730  575   97  159         1  155
    34  NYY     AL  1975  681  588   83  160         0   93
    35  NYY     AL  1974  671  623   89  162         0   48
    36  NYY     AL  1973  641  610   80  162         0   31
    37  NYY     AL  1971  648  641   81  162         0    7
    38  NYY     AL  1970  680  612   93  163         0   68
    39  NYY     AL  1969  562  587   80  162         0  -25
    40  NYY     AL  1968  536  531   83  164         0    5
    41  NYY     AL  1967  522  621   72  163         0  -99
    42  NYY     AL  1966  611  612   70  160         0   -1
    43  NYY     AL  1965  611  604   77  162         0    7
    44  NYY     AL  1964  730  577   99  164         1  153
    45  NYY     AL  1963  714  547  104  161         1  167
    46  NYY     AL  1962  817  680   96  162         1  137
'''

# Using .apply() = like a .map
# apply(what, where):
# what -> the function to apply
# where -> axis = 1 (rows) or arix = 0 (columns)

rays_df = []

'''
       RS   RA   W  Playoffs
2012  697  577  90         0
2011  707  614  91         1
2010  802  649  96         1
2009  803  754  84         0
2008  774  671  97         1
'''

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

'''
RS          3783
RA          3265
W            458
Playoffs       3
'''

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

'''
2012    1274
2011    1321
2010    1451
2009    1557
2008    1445
'''


def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'


# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(
    lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

'''
2012     No
2011    Yes
2010    Yes
2009     No
2008    Yes
'''

dbacks_df = []


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc, 2)


# Display the first five rows of the DataFrame
print(dbacks_df.head())
'''
  Team League  Year   RS   RA   W    G  Playoffs
0  ARI     NL  2012  734  688  81  162         0
1  ARI     NL  2011  731  662  94  162         1
2  ARI     NL  2010  713  836  65  162         0
3  ARI     NL  2009  720  782  70  162         0
4  ARI     NL  2008  720  706  82  162         0
'''

# Create a win percentage Series
win_percs = dbacks_df.apply(
    lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')
'''
0     0.50
1     0.58
2     0.40
3     0.43
4     0.51
5     0.56
6     0.47
7     0.48
8     0.31
9     0.52
10    0.60
11    0.57
12    0.52
13    0.62
14    0.40
'''

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')
'''
   Team League  Year   RS   RA    W    G  Playoffs    WP
0   ARI     NL  2012  734  688   81  162         0  0.50
1   ARI     NL  2011  731  662   94  162         1  0.58
2   ARI     NL  2010  713  836   65  162         0  0.40
3   ARI     NL  2009  720  782   70  162         0  0.43
4   ARI     NL  2008  720  706   82  162         0  0.51
5   ARI     NL  2007  712  732   90  162         1  0.56
6   ARI     NL  2006  773  788   76  162         0  0.47
7   ARI     NL  2005  696  856   77  162         0  0.48
8   ARI     NL  2004  615  899   51  162         0  0.31
9   ARI     NL  2003  717  685   84  162         0  0.52
10  ARI     NL  2002  819  674   98  162         1  0.60
11  ARI     NL  2001  818  677   92  162         1  0.57
12  ARI     NL  2000  792  754   85  162         0  0.52
13  ARI     NL  1999  908  676  100  162         1  0.62
14  ARI     NL  1998  665  812   65  162         0  0.40 
'''

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])
'''
   Team League  Year   RS   RA    W    G  Playoffs    WP
0   ARI     NL  2012  734  688   81  162         0  0.50
1   ARI     NL  2011  731  662   94  162         1  0.58
4   ARI     NL  2008  720  706   82  162         0  0.51
5   ARI     NL  2007  712  732   90  162         1  0.56
9   ARI     NL  2003  717  685   84  162         0  0.52
10  ARI     NL  2002  819  674   98  162         1  0.60
11  ARI     NL  2001  818  677   92  162         1  0.57
12  ARI     NL  2000  792  754   85  162         0  0.52
13  ARI     NL  1999  908  676  100  162         1  0.62
'''

baseball_df = []

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)
'''
.values ->
[ 81  94  93 ... 103  84  60]
[162 162 162 ... 165 163 162]
'''

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())
'''
  Team League  Year   RS   RA   W    G  Playoffs    WP
0  ARI     NL  2012  734  688  81  162         0  0.50
1  ATL     NL  2012  700  600  94  162         1  0.58
2  BAL     AL  2012  712  705  93  162         1  0.57
3  BOS     AL  2012  734  806  69  162         0  0.43
4  CHC     NL  2012  613  759  61  162         0  0.38
'''

# ********************** ALTOGETHER ********************** 

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)
baseball_df['WP_loop'] = win_perc_preds_loop

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)
baseball_df['WP_apply'] = win_perc_preds_apply

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

'''
  Team League  Year   RS   RA  ...  Playoffs    WP  WP_preds  WP_loop  WP_apply
0  ARI     NL  2012  734  688  ...         0  0.50      0.53     0.53      0.53
1  ATL     NL  2012  700  600  ...         1  0.58      0.58     0.58      0.58
2  BAL     AL  2012  712  705  ...         1  0.57      0.50     0.50      0.50
3  BOS     AL  2012  734  806  ...         0  0.43      0.45     0.45      0.45
4  CHC     NL  2012  613  759  ...         0  0.38      0.39     0.39      0.39
'''