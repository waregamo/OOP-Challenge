from pet import Pet

def main():
    # Create a pet object with the name "Cockrobin"
    my_pet = Pet("Cockrobin")
    
    # Test the methods
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    
    # Get the current status of the pet
    my_pet.get_status()
    
    # Train the pet with some tricks
    my_pet.train("roll over")
    my_pet.train("play dead")
    
    # Show the learned tricks
    my_pet.show_tricks()

if __name__ == "__main__":
    main()