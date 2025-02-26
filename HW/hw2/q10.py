'''
List Manipulation Challenge: Movie Watchlist Manager

Create a program that manages a movie watchlist using Python lists. The program should allow users to add movies, remove movies, display the watchlist, and perform various operations on the list.

Implement the following functions: 
Add a movie to the watchlist
Remove a movie from the watchlist
Display the current watchlist
Check if a movie is in the watchlist
Get the number of movies in the watchlist
Clear the entire watchlist
Sort the watchlist alphabetically
Reverse the order of the watchlist
Get a random movie recommendation from the watchlist
Create a simple menu-driven interface for users to interact with the watchlist

'''
def menu():
    print(" ")
    print("Movie Watchlist Manager: ")
    print("1. Add a movie to the watchlist")
    print("2. Remove a movie from the watchlist")
    print("3. Display the current watchlist")
    print("4. Check if a movie is in the watchlist")
    print("5. Get the number of movies in the watchlist")
    print("6. Clear the entire watchlist")
    print("7. Sort the watchlist alphabetically")
    print("8. Reverse the order of the watchlist")
    print("9. Get a random movie recommendation from the watchlist")
    print("10. Exit")

watchlist = []

while True:
    menu()
    choice = input("Enter your choice(1-10): ")
    print()
    
    if choice == "1":
        movie = input("Enter the movie name: ")
        watchlist.append(movie)
        print(f"{movie} added to the watchlist.")

    elif choice == "2":
        movie = input("Enter the movie name: ")
        if movie in watchlist:
            watchlist.remove(movie)
            print(f"{movie} removed from the watchlist.")
        else:
            print(f"{movie} not found in the watchlist.")

    elif choice == "3":
        print("Current watchlist:")
        for movie in watchlist:
            print(movie)

    elif choice == "4":
        movie = input("Enter the movie name: ")
        if movie in watchlist:
            print(f"{movie} is in the watchlist.")
        else:
            print(f"{movie} not found in the watchlist.")

    elif choice == "5":
        print("Number of movies in the watchlist: ", len(watchlist))

    elif choice == "6":
        watchlist.clear()
        print("Watchlist cleared.")

    elif choice == "7":
        watchlist.sort()    
        print("Watchlist sorted alphabetically.")

    elif choice == "8":
        watchlist.reverse()
        print("Watchlist reversed.")

    elif choice == "9":
        if len(watchlist) > 0:
            import random
            print("Random movie recommendation:", random.choice(watchlist))
        else:
            print("Watchlist is empty.")

    elif choice == "10":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")  