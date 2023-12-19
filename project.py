import sys
import random

# words_in_song = {}

forbidden_words = {"i", "you", "he", "she", "the", "a", "an", "and", "my", "am", "is"}
song_list = [
    "smells_like_teen_spirit.txt",
    "another_one_bites_the_dust.txt",
    "imagine.txt",
    "billie_jean.txt",
]

# default values
artist = ["Unknown"]
title = ["Unknown"]


def main():
    # Initialisation of variables
    score = 0
    out_of = 0
    continue_ = True

    # Round specific loop
    while continue_:
        # Count the number of rounds played
        out_of += 1

        # Initialisation of round's specific variables
        returned = []
        words_in_song = {}

        # Pick song and generate words
        song = pick_song2()
        level = get_level()
        returned = genearte_cloud(song, level, returned, words_in_song)

        # Guessing section - Prepare the guess loop
        guessed = False
        number_of_guesses = 0

        while guessed == False:
            # Count the number of guesses
            number_of_guesses += 1

            # Outputs depending on the number of guesses done
            for t in returned:
                print(t[0], end=" ")
                if number_of_guesses in [2, 3]:
                    print(f"appears {t[1]} times", end="")
                print()

            # Third guess clue
            if number_of_guesses == 3:
                print()
                print(f"It's a song by {artist[0]}")
            print()
            guess = input("Guess the title: ")

            # Analyse the guess
            if guess.lower().strip() == title[0].lower():
                print(f"Correct, it's indeed {title[0]} by {artist[0]}")
                score += 1
                guessed = True

            # If not guessed afer 3 tries
            if number_of_guesses == 3 and guessed == False:
                guessed = True
                print(f"The answer is {title[0]} by {artist[0]}")
            print()

        # Continue playing section
        print("Continue? (yes/no)")
        playing = input().strip()
        if playing.lower() == "yes":
            continue_ = True
        else:
            continue_ = False
        print()

    # Score section
    print(f"Score: {score} / {out_of}")
    print(get_sentence(score))
    print()


def get_level():
    not_accepted = True
    while not_accepted:
        try:
            level = int(input("How many words to be shown (Up to 15)? "))
            print()
            not_accepted = False
            if level > 15 or level < 1:
                not_accepted = True
        except:
            not_accepted = True
    return level


def pick_song():
    # pick a random element from a list of strings.
    song = random.choice(song_list)
    return f"../project/texts/" + song

def pick_song2():
    # pick a random element from another file
    link = "../project/texts/texts_names.txt"
    # Default value in case there is a problem
    song = "another_one_bites_the_dust.txt"


    # First reading of the file
    try:
        list_of_songs = open(link)
    except:
        sys.exit("Couldn't open the file in pick_song")
    else:
        # Count lines
        count = 0
        while True:
            line = list_of_songs.readline()
            if not line:
                break
            count += 1
            selected = random.randint(1, count)
        # Close file so we can start back at the begining of said file
        list_of_songs.close()
        # Second reading of the file
        try:
            list_of_songs = open(link)
        except:
            sys.exit("Couldn't open the file in pick_song")
        else:
            # Find line
            count2 = 0
            while True:
                line = list_of_songs.readline()
                if not line:
                    break
                count2 += 1
                if count2 == selected :
                    song = line.removesuffix("\n")


        list_of_songs.close()
    return f"../project/texts/" + song


def genearte_cloud(s: str, level: int, returned: list, words_in_song: list):
    try:
        song = open(s)
    except:
        sys.exit("Couldn't open the file")
    else:
        count = 0
        while True:
            count += 1
            line = song.readline()
            if not line:
                break
            if count > 2:
                words = line.split()
                for word in words:
                    word = get_rid_of_punctuation(word).title().strip()
                    if word.lower() not in forbidden_words:
                        if word_exist(word, words_in_song):
                            add_word(word, words_in_song)
                        else:
                            create_word(word, words_in_song)
            elif count == 1:
                title_name, artist_name = line.split(" - ")
                artist[0] = get_rid_of_punctuation(artist_name.strip())
                title[0] = get_rid_of_punctuation(title_name.strip())

        sorted_dict = dict(sorted(words_in_song.items()))
        sorted_dict = sorted(sorted_dict.items(), key=lambda x: x[1], reverse=True)

        for word in sorted_dict[:level]:
            returned.append(word)

        song.close()
        return returned


def get_rid_of_punctuation(word: str):
    punctuation = [",", ".", "!", "?", "(", ")", "\n"]
    for i in punctuation:
        word = word.replace(i, "")
    return word


def word_exist(item: str, words_in_song: list):
    if item in words_in_song:
        return True
    else:
        return False


def add_word(item: str, words_in_song: list):
    words_in_song[item] += 1


def create_word(item: str, words_in_song: list):
    words_in_song[item] = 1


def get_sentence(i: int):
    if i == 0:
        return "Better luck next time!"
    return "Well done!"


if __name__ == "__main__":
    main()
