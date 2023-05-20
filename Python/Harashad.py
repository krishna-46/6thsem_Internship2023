# You are tasked with building a simple music player application that can play different types of music files. Implement a Python class called MusicPlayer that represents a music player. The MusicPlayer class should have the following attributes and methods:
# Attributes:
# playlist (list of strings): A list of music files in the playlist.
# current_song (string): The name of the currently playing song.
# Methods:
# __init__(self, playlist): Initializes a new music player with the given playlist.
# play(self, song): Plays the specified song from the playlist and updates the current_song attribute accordingly.
# pause(self): Pauses the currently playing song.
# resume(self): Resumes playing the currently paused song.
# stop(self): Stops playing the current song and resets the current_song attribute to an empty string.
# add_song(self, song): Adds the specified song to the playlist.
# remove_song(self, song): Removes the specified song from the playlist.
# Write the MusicPlayer class implementation and provide a sample code snippet that demonstrates the usage of the class by creating an instance of MusicPlayer and performing various operations on it.
# Feel free to add any additional helper methods or attributes to enhance the functionality of the MusicPlayer class if you wish.


class MusicPlayer :
    

    def __init__(self,playlist) :
        self.playlist=playlist
        self.current_song= ""

    def play (self,song):
        if song in self.playlist:
            self.current_song=song
            print("playing",song)

        else:
            print("song not found")

    def pause(self):
        if self.current_song:
            print("Pausing:", self.current_song)
        else:
            print("No song is currently playing.")

    def resume(self):
        if self.current_song:
            print("Resuming:", self.current_song)
        else:
            print("No song is currently playing.")

    def stop(self):
        if self.current_song:
            print("Stopping:", self.current_song)
            self.current_song = ""
        else:
            print("No song is currently playing.")

    def add_song(self, song):
        if song not in self.playlist:
            self.playlist.append(song)
            print("Added song:", song)
        else:
            print("Song already exists in the playlist.")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print("Removed song:", song)
        else:
            print("Song not found in the playlist.")


# Create a music player instance with an initial playlist
playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
player = MusicPlayer(playlist)

# Play a song
player.play("song2.mp3")

# Pause the currently playing song
player.pause()

# Resume the paused song
player.resume()

# Stop the currently playing song
player.stop()

# Add a new song to the playlist
player.add_song("song4.mp3")

# Remove a song from the playlist
player.remove_song("song2.mp3")

    




    


        