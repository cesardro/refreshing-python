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

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)