import unittest
from classes.song import Song
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest. TestCase):
    def setUp(self):
        self.guest = Guest(name="Bob")
        self.room = Room(number=1)
        self.guest_list = []
        self.song = Song(["Gangstas Paradise","Come On Eileen", "Bat Out Of Hell"])

    def test_add_guests(self):
        self.room.add_guest(self.guest.name)
        self.assertEqual(["Bob"], self.room.guest_list)

    def test_remove_guest(self):
        self.room.remove_guest(self.guest)
        self.assertEqual([], self.room.guest_list)

    def test_if_room_has_guests_list(self):
        self.assertEqual([], self.guest_list)

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song.song_list[0])
        self.assertEqual("Gangstas Paradise", self.song.song_list[0])
