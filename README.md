# Blackjack-game
The classic "21" Blackjack Game

So as part of Milestone project 2 in the python course, the aim was to create a blackjack game.

The structure of the game was the following:

- Human vs Automated dealer
- Cards have a value corresponding to their number, however face cards are valued at 10 and an ace can be worth 11 or 1
- Player to be closest to a value of <= 21 wins the round
- Player can make two choices, to stay or to draw a card
- The player hold a certain amount of chips which they can bet, we keep track of this value
- Ability to run several game ending scenarios including player/dealer; wins/busts and ties.

With respect to gameplay, a deck of 52 cards was created ♥ ♦ ♠ ♣

The challenges i encountered in this project are listed as follows:

- Due to the fact that there was alot of code, i found myself getting confused at some points betweem arugments that need to be passed into 
a function for example and class attributes. I think for argument names which can be abstract its best to have a certain syntax such as "_arg"
so that i can quickly recall its purpose. Having said that, if i apply this method in my work i should note down this use in th readme.file.

- In the semi/full-reveal functions to show the player and dealers hands i learned how to use the "\t" method to tab out a printing statement,
i tried using different methods which were not applicable for the card showing print statement that utilised the for loop.

- I wrote a few bits of code in the wrong order which was causing my code to not run properly yet was difficult to spot, but realising where the issue
was having an effect enabled me to quickly fix it. For instance, in the Chips() class i wrote self.bet += self.total_chips as opposed to
self.total_chips += self.bet

Some improvements i made to the game are listed as follows:

- I ensured that if the player decided to repeat, the game they would be able to work with the chips they initially started with.
I placed the instantiation of the Chip() class outside of the very first while loop so that it would only run once during the program.

- Adding onto the previous points, print statements welcoming the player and briefly explaining the game were also placed outside of the while loop
so they wouldnt run each time the player chose to replay the game.

- Given that chips were to rollover each time, there was a possibility that the player would run out of chips, hence, i implemented a condition that checks
if the player still has chips. If they dont, they are prompted that theyve essentially lost but can run the script againt to play again.

- Furthermore, playing multiple times without an end goal may seem meaningless so in the initial print statements i challenge the player to accumulate 
250 chips.

- Incorporated some time.sleep() methods to pace the  game nicely.

I really enjoyed making this game as well as playing it, the version of blackjack i used to play back in school was completely different and had way more
sophisticated rules, however this style of play is short and sweet.
