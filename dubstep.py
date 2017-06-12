"""
Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
result should be WE ARE THE CHAMPIONS MY FRIEND
"""


# with regex
def song_decoder(song):
    return re.sub('(WUB)+', ' ', song).strip()

# without regex
import string

def song_decoder(song):
    oldSong = song.replace("WUB", " ")
    return compress(oldSong)
     
def compress(song):
    prev = "" # previous white space character
    curr = ""
    final = []
    for c in song:
        curr = c
        if curr in list(string.ascii_uppercase):
            final.append(curr)
        elif prev == " " and curr == " ":
            continue
        else:
            final.append(" ")
        prev = curr

    return "".join(final).strip()