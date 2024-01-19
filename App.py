#Create a simple music player that can play MP3 files and allows the user to create and manage playlists

#SPOTIFY MUSIC APP -- Using Python Object Oriented Programming!!

class Spotify_App:
    """A class to model the sportify app"""

    #Define different attributes
    def __init__(self):
        self.playlist = []
        self.current_song = None

    #define a method to create a playlist
    def create_playlist(self, playlist_name):
        #Append every playlist name to the playlist list
        self.playlist.append(playlist_name)
        print(f"Playlist '{playlist_name}' created")
    
    #define method to add song to playlist
    def add_song_to_playlist(self, playlist_name, song):
        #condtional statement to chack for playlist_name in playlist list []
        if playlist_name in self.playlist:
            print(f"Added '{song}' to playlist '{playlist_name}'.")
        else:
            print(f"playlist '{playlist_name}' not found.")

    #Define method to 'play song'
    def play_song(self, song):
        self.current_song = song
        print(f"Now playing: {song}")
    
    #Deifne method to show current playing song
    def show_current_song(self):
        if self.current_song:
            print(f"Currently playing: {self.current_song}")
        else:
            print("No song is currently playing.")

    
#Creating an instance of the class
spotify = Spotify_App()

while True:
    print("\nAvailable commands: create playlist, add song, play song, current song, exit")
    #Prompt user for input
    command =  input("Enter a command: ")
    
    #Testing for different cases using if,elif and else conditionals 
    if command == 'create playlist':
        playlist_name = input("Enter playlist name: ")
        spotify.create_playlist(playlist_name)

    elif command == 'add song':
        playlist_name = input("Enter playlist name: ")
        song = input("Enter song name: ")
        spotify.add_song_to_playlist(playlist_name, song)

    
    elif command == 'play song':
        song = input("Enter song name: ")
        spotify.play_song(song)

    elif command == 'current song':
        spotify.show_current_song()

    elif command == 'exit':
        print("Exiting the sportify app. Goodbye!")
        break   #To breakout completely out of the loop

    else:
        print("Invalid command.please try again!!")