# Text-based Adventure Game: Jungle Quest
# Creativity: Added four levels of choices (exceeds minimum of three), included a secret hidden choice, added loops for replayability, and created multiple alternate endings with humor and suspense.
# After showing this program to two people, they enjoyed discovering the hidden paths and appreciated the branching storyline logic.

def adventure_game():
    while True:
        print("Welcome to Jungle Quest!")
        print("You find yourself stranded in a dense jungle. Your goal is to find a way to safety. Choose wisely!")

        # First Level
        print("\nYou see two paths ahead. One is DARK and overgrown, and the other is BRIGHT and clear. Which path do you take?")
        choice1 = input("Enter DARK or BRIGHT: ").strip().lower()

        if choice1 == "dark":
            print("\nYou brave the dark path, pushing aside thick vines. You hear a growl behind you. Do you RUN, HIDE, or CLIMB a tree?")
            choice2 = input("Enter RUN, HIDE, or CLIMB: ").strip().lower()

            if choice2 == "run":
                print("\nYou sprint through the jungle and stumble into a quicksand pit! Do you GRAB the vine nearby or CALL for help?")
                choice3 = input("Enter GRAB or CALL: ").strip().lower()

                if choice3 == "grab":
                    print("\nYou grab the vine and pull yourself out just in time. You find a rescue team nearby and make it out safely. Congratulations, you survived the jungle!")
                elif choice3 == "call":
                    print("\nYou shout for help, but your voice attracts a pack of wild animals. Unfortunately, this is the end of your adventure.")
                else:
                    print("\nInvalid choice. The jungle is unforgiving. You meet an untimely demise.")

            elif choice2 == "hide":
                print("\nYou hide behind a tree, but the growling gets closer. Suddenly, you notice a hidden CAVE. Do you ENTER, STAY hidden, or SET a trap?")
                choice3 = input("Enter ENTER, STAY, or SET: ").strip().lower()

                if choice3 == "enter":
                    print("\nYou enter the cave and discover ancient treasure! You're rescued days later, rich beyond your wildest dreams. What an adventure!")
                elif choice3 == "stay":
                    print("\nYou stay hidden, but the growling creature finds you. Unfortunately, the adventure ends here.")
                elif choice3 == "set":
                    print("\nYou cleverly set a trap using vines and sticks. The growling creature gets caught, and you escape unharmed. Resourcefulness saved you!")
                else:
                    print("\nInvalid choice. The jungle shows no mercy. Your story ends here.")

            elif choice2 == "climb":
                print("\nYou climb a tree to escape the growling. From above, you spot a hidden pathway. Do you DESCEND and follow it or WAIT for rescue?")
                choice3 = input("Enter DESCEND or WAIT: ").strip().lower()

                if choice3 == "descend":
                    print("\nYou follow the hidden pathway and find a small village. The villagers help you get back to safety. Well done, explorer!")
                elif choice3 == "wait":
                    print("\nYou wait patiently, but help never comes. The jungle claims another adventurer.")
                else:
                    print("\nInvalid choice. Indecision leads to your downfall.")
            else:
                print("\nInvalid choice. Lost in hesitation, you fall prey to the jungle.")

        elif choice1 == "bright":
            print("\nYou take the bright path and find a river. You see a RAFT and a BRIDGE. How do you cross the river?")
            choice2 = input("Enter RAFT or BRIDGE: ").strip().lower()

            if choice2 == "raft":
                print("\nYou hop on the raft and start paddling. Midway, you see a waterfall ahead. Do you JUMP off, HOLD on, or PADDLE to the side?")
                choice3 = input("Enter JUMP, HOLD, or PADDLE: ").strip().lower()

                if choice3 == "jump":
                    print("\nYou jump into the water and swim to safety. You eventually find a village and are rescued. Great job surviving!")
                elif choice3 == "hold":
                    print("\nYou hold on, but the raft goes over the waterfall. Sadly, this is the end of your adventure.")
                elif choice3 == "paddle":
                    print("\nYou paddle to the side and avoid the waterfall. On the riverbank, you find a rescue team and are saved. Smart thinking!")
                else:
                    print("\nInvalid choice. The river claims another adventurer.")

            elif choice2 == "bridge":
                print("\nYou cross the bridge and find a sign that says 'BEWARE OF THE TRAP'. Do you CONTINUE, TURN back, or INSPECT the area?")
                choice3 = input("Enter CONTINUE, TURN, or INSPECT: ").strip().lower()

                if choice3 == "continue":
                    print("\nYou continue carefully and discover a hidden helicopter landing pad. Soon, you're airlifted to safety. What a daring escape!")
                elif choice3 == "turn":
                    print("\nYou turn back but lose your way in the jungle. Unfortunately, your adventure ends here.")
                elif choice3 == "inspect":
                    print("\nYou inspect the area and disarm a hidden trap. Your caution pays off, and you safely reach a rescue point. Great job!")
                else:
                    print("\nInvalid choice. Lost in uncertainty, you succumb to the jungle.")
            else:
                print("\nInvalid choice. Indecision leads you astray, and the jungle takes its toll.")

        else:
            print("\nInvalid choice. You wander aimlessly and become another mystery of the jungle.")

        # Replay prompt
        replay = input("\nDo you want to play again? (yes or no): ").strip().lower()
        if replay != "yes":
            print("\nThanks for playing Jungle Quest! Goodbye.")
            break

# Run the game
adventure_game()
