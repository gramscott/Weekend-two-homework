class Room:
    def __init__(self, number):
        self.number = number
        self.guest_list = []
        self.song_list = []
    
    def add_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)
            
    def add_song_to_room(self, songs):
        self.song_list.append(songs)
        
    
 

