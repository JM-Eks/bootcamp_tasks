# TASKS
# 1. Create a list called movies with at least five of your favourite movie titles. ✅
# 2. Use an appropriate list method to add a new movie to the list. ✅
# 3. Replace the second movie in the list with a different one. Update the list accordingly. ✅
# 4. Print the updated movie list. ✅
# 5. Retrieve and print the last movie in the list using negative indexing. ✅

myFavMovies = ["V For Vendetta", "Harry Potter", "Lord of the Rings", "Erin Brockovich", "Scarface"]
print(f"Initial list -> {myFavMovies}")

print("")

myFavMovies.insert(0, "12 Angry Men")
print(f"First update -> {myFavMovies}")

print("")

myFavMovies[-2] = "Romancing the Stone"
print(f"Second update -> {myFavMovies}")

print("")

print(f"The last movie in the list is: {myFavMovies[-1]}")