class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_song = ''

    def play(self, song):
        if song in self.playlist:
            self.current_song = song
            print("Now playing: " + song)
        else:
            print(song + " is not in the playlist.")

    def pause(self):
        if self.current_song:
            print("Paused: " + self.current_song)
        else:
            print("No song is currently playing.")

    def resume(self):
        if self.current_song:
            print("Resuming: " + self.current_song)
        else:
            print("No song is currently paused.")

    def stop(self):
        if self.current_song:
            print("Stopped: " + self.current_song)
            self.current_song = ''
        else:
            print("No song is currently playing.")

    def add_song(self, song):
        if song not in self.playlist:
            self.playlist.append(song)
            print("Added " + song + " to the playlist.")
        else:
            print(song + " is already in the playlist.")

# Create an instance of MusicPlayer
playlist = ['song1.mp3', 'song2.mp3', 'song3.mp3']
player = MusicPlayer(playlist)

while True:
    print("Choose an action:")
    print("1. Play a song")
    print("2. Pause the current song")
    print("3. Resume the current song")
    print("4. Stop the current song")
    print("5. Add a song to the playlist")
    print("0. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        song_index = int(input("Enter the song number to play: ")) - 1
        if song_index >= 0 and song_index < len(playlist):
            player.play(playlist[song_index])
        else:
            print("Invalid song number.")

    elif choice == "2":
        player.pause()

    elif choice == "3":
        player.resume()

    elif choice == "4":
        player.stop()

    elif choice == "5":
        new_song = input("Enter the name of the song to add: ")
        player.add_song(new_song)

    elif choice == "0":
        break

    else:
        print("Invalid choice. Please try again.\n")
