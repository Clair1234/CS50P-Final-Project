# CS50P-Final-Project : Guess the song by its lyrics
## Video Demo:  <URL HERE>
### General Description :
The purpose of this project is to have a game based in the terminal where the player has to guess a song, selected by the program, only based on its most repeated words. The player can customize their game experience by choosing how many words are shown. When the player decides to stop playing, their score is given out of the number of plays they just did.

I decided to work on this project because I wanted to practise manipulating documents starting with opening and reading text documents. The central idea of this project was being able to create a cloud of the most repeated words out of a document. It then took the form of a game based on song because I wanted to implement a ludic aspect and have a personal preference for music rather than random texts.

### Detailed description :
#### User side
To try the program, the only requirement is to run the program, there is no need to implement a library or to rely on another window.

The user will first be prompted to choose a number between 1 to 15, corresponding to the number of words that will be shown each time to guess the song. If the user picks a number outside of [1 ; 15] or a word, they will be prompted again until a number between 1 and 15 is settled on.

The guess system is based on three phases, at the end of each phase the user has one chance to guess the title of the song selected.

On the first phase, the player is given the number of words they chose corresponding to, from top to bottom, the most to the least repeated word in the song.

On the second phase, the user is given the number of times the said words are repeated, this allows the player to target the words to guess the song from. For example, if the player chooses to show ten words and on the second phase, they get that the first six words are repeated more than 30 times while the four following are repeated less than 10 times then it becomes irrelevant to guess based on the ten first words rather than to focus on only the first six.

On the third phase, they get the words with the number of times each word is repeated and the artist of the song. This is the last clue the program gives out. If the following guess is wrong, the program will reveal the song.

If the player guesses on any phase, the round is finished, and their score incremented by one point. The phase on which the song has been guessed does not impact the way the score is incremented.

After each round, the user is asked if they want to continue playing. To continue they have to type out the word “yes”, any other input will be interpreted as a quit. This allows the player to easily quit playing and avoid getting stuck playing. When the game is quit, the player’s score will be shown, they will be able to see the number of songs guessed out of the number of songs the program has prompted them with.

#### Code side
To complete the different functions of the game, the program is segmented into different functions calling one another.

First, I set a list of forbidden words, the goal is to put aside words that are recurrent but do not help in guessing the song. It prevents that the list of most said words is entirely pronouns. The artist’s name and title are defined as "Unknown" it allows the program to have a default setting in case there is a problem with the main.

Regarding the main, various variables are initialised allowing to set up a score system and prepare for the `while` loop representing the action of playing the game.

The main `while` loop counts the number of rounds played, what is supposed to be returned each round (dictionary and list) is set to empty. The program starts by selecting a song with the `pick_song2()` function. The first part of its program is to access the folder with the different songs. It has a default setting to the song "Another one bites the dust". It then goes through the file `texts_names.txt` twice. The use of an external .txt file with all the songs allows that, in case of one wanted to add a new song they only have to manipulate a .txt file rather than a .py file, granted they have to write the exact name .txt of the file but it permits to really separate from the code in itself. The first time it goes through the `texts_names.txt` it counts the number of lines in it. And then, after it picks out randomly a number out of the number of lines in the text, it goes through it a second time to pick out a file with the song lyrics in it. The directory to the song picked out is given back to the `main` function.

Then, the program gets the "level" which is the number of words that will be shown to the player through the `get_level()` function. This loops until an integer (here between 1 and 15) is given. This allows to control step by step the interactions with the user.

After that, a "cloud" of word is generated with the `generate_cloud(str, int, list, list)` function. Firstly, it tries to open the text file with the song. From the first line, it takes the information on the artist's and the song's name, because each file with song is formatted the same way. For the other lines, it splits each word from one another, gets rid of the punctuation (with the `get_rid_of_punctuation(str)` function that replace any punctuation with empty quotes) and if the word is not amongst the forbidden words defined previously, it gets added to the list `words_in_song`.

That list is implemented in two ways. Either the word has already occurred, the function, `add_word(str, list)`, is used. The `words_in_song` list works as a dictionary so the value associated to the word is incremented by one. If the word has not already occurred, the function `create_word(str, list)` is used, it sets a new line in the dictionary with the word and its value is set to 1.

The dictionary is then ordered alphabetically and by higher value. The list of returned words is append up to the number of words defined by the `level` variable.

As the manipulation of file is finished, the file with the song is closed.

A second loop is set in the main, this time it is limited to a maximum of three loops, it deals with the number of guesses allowed before the answer is given to the player. There are three phases during the guess section, each monitored by the `number_of_guesses` variable. Each guess is compared to the right answer case insensitive. The user is then asked if they want to play again. If the player does not explicitely write "yes" (case insensitive) the game comes to an end.

The game ends with the score given out to the player. Two possibilities are covered by the `get_sentence(int)` function, either the user has had one correct guess and gets a "Well done!" or no guess were correct, and the user gets a "Better luck next time!".

The `song_list` list defined at the beginning of the code and the `pick_song()` function are not currently used in the program they were simply building blocks to the final version of this project.

### TODO
### Download
Download the repository through Clone Repository or Download Zip
```
git clone
```
### Installation
After download, go to 'cmd' and navigate to the project folder directory
```
cd project
```
### Usage
Run the program python script `project.py` with [python](https://www.python.org/).
```
python project.py
```
Test the program python script `test_project.py` with [pytest](https://docs.pytest.org/en/7.2.x/).
```
pytest test_project.py
```
After successfully running the program, it will prompt for a level, an integer.
Enter a number between 1 and 15.
It will then give out words related to the songs.
You are free to guess the song.

>[!NOTE]
>The program is case-insensitive.

>[!IMPORTANT]
>The song title has to be spelt correctly or else it will be counted as a false guess.
