# For Task 1. Noted in 04/07/2026.

#Listing:
# user_song_list = ["Bad - Micahel Jackson", "Bones - Imagine Dragons", "Beat It - Michael Jackson"]

# user_song_list.append("Shake It Off - Taylor Swift")
# user_song_list[1] = "Boost It Up - Miles Minnick"
# del user_song_list[0]  

# print(user_song_list)


# For Part 2. 

full_game_inventory = {

    "potions": 5,
    "arrows": 20,
    "swords": 1
}

print(full_game_inventory.get('arrows')) 
full_game_inventory["arrows"] = 30 

full_game_inventory["shields"] = 2


print(full_game_inventory)
