## Google Play Music Total Library Listen Time
This is a super basic script to get the total listen time of every song currently in the user's library.  It only counts song in the player's library, so any songs listened to in a station or the like won't be counted.

[Generate an app password to use in scripts like this!](https://myaccount.google.com/apppasswords)

Just edit the file to the the appropriate login information and run it using `python totallistentime.py`.

It will output every album with every song it finds with at least one play.  It looks like the following, where each album is a dictionary, where for each song number there's a tuple with the number of plays and the duration of the song in miliseconds.

     'Eidolon': {1: (200, '29000'),
             2: (200, '250000'),
             3: (200, '217000'),
             4: (201, '299000'),
             5: (200, '107000'),
             6: (200, '282000'),
             7: (201, '258000'),
             8: (200, '70000'),
             9: (200, '311000'),
             10: (199, '203000'),
             11: (199, '133000'),
             12: (198, '344000'),
             13: (198, '374000'),
             14: (198, '410000')},

At the end it will display the total number of miliseconds listened and the total play time converted a human-readable format.

    7514133010
    86 days, 23:15:33.010000

86 days, 23 hours, 15 minutes, 33 seconds, and 10 miliseconds of total play time.