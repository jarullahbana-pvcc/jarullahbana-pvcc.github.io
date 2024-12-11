# Name: Jarullah Bana
# Program Purpose: This program demonstrates how to manipulate a list, including:
# - Finding the number of items in the list.
# - Sorting the list.
# - Adding/removing items.
# - Copying a list of items into another list.
# - Changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "Annabelle", "Gonzo", "Sweetie-Pie", "Diego"]
dogs2 = []

def pause():
    input("\nPress ENTER to continue...")

def main():
    # Number of dogs in the list
    how_many = len(dogs)
    print("Number of dogs in the list, using len():", how_many)
    print("\nOriginal list of dog names:")
    print(dogs)
    pause()

    # Reverse the list
    dogs.reverse()
    print("\nList from last to first, using reverse():")
    print(dogs)
    pause()

    # Alphabetized list
    dogs.sort()
    print("\nAlphabetized list, using sort():")
    print(dogs)
    pause()

    # Reverse alphabetized list
    dogs.sort(reverse=True)
    print("\nList in reverse alphabetized order, using sort(reverse=True):")
    print(dogs)
    pause()

    # Add a dog to the end of the list
    dogs.append("Ranger")
    print("\nAdd a dog to the end of the list, using append():")
    print(dogs)
    pause()

    # Remove the first dog
    doggy = dogs.pop(0)
    print("\nRemove a dog off from the front of the list, using pop():")
    print(dogs)
    print(doggy, "was removed from the front of the list.")
    pause()

    # Remove a dog from position 3
    another_dog = dogs.pop(3)
    print("\nRemove a dog from position 3 (the 4th dog) in the list, using pop(index):")
    print(dogs)
    print(another_dog, "was removed from position 3 of the list.")
    pause()

    # Remove a dog by name
    dogs.remove("Annabelle")
    print("\nRemove a dog by name rather than position in the list, using remove(name):")
    print(dogs)
    pause()

    # Copy the list into another list
    dogs2 = dogs[:]
    print("\nA list can be copied into another list by setting one equal to the other:")
    print("Dogs:")
    print(dogs)
    print("Dogs2:")
    print(dogs2)
    pause()

    # Use a FOR loop to modify each dog's name
    print("\nUse a FOR loop to give each dog in the same list a last name, using the for loop:")
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Bana"  # Change "Bana" to your last name
    print(dogs)
    pause()

# Run the program
main()
