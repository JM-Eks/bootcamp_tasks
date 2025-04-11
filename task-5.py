# TASKS
# You are managing a music app and need to handle a user's playlist.

# Instructions:
# 1. Create a list called playlist containing five song titles. ✅
# 2. A user wants to add two new songs at once. Use an appropriate method to extend the list with these songs. ✅
# 3. The user decides to remove a song they no longer like. Remove the third song from the playlist. ✅
# 4. Print the updated playlist and display the total number of songs in it. ✅
# 5. Retrieve and print the first three songs in the playlist using slicing. ✅

playlist = ["God Did", "Lady In Red", "Bout U", "Forever Young", "Waymaker"]
newSongs = ["24K Magic", "TTP"]
playlist.extend(newSongs)
del playlist[2]

print(f"UPDATED PLAYLIST\n{playlist}")
print(f"There are now {len(playlist)} songs in the playlist.")
print("")

first3Songs = playlist[0:3]
print(f"THE FIRST THREE SONGS IN THE PLAYLIST ARE:\n{', ' .join(first3Songs)}")