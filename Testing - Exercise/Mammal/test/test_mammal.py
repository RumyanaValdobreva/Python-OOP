from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal("MammalName", "MammalType", "MammalSound")

    def test_correct_initialization(self):
        self.assertEqual("MammalName", self.mammal.name)
        self.assertEqual("MammalType", self.mammal.type)
        self.assertEqual("MammalSound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_does_it_make_correct_sound_when_we_call_make_sound(self):
        actual = self.mammal.make_sound()
        self.assertEqual("MammalName makes MammalSound", actual)

    def test_does_it_return_correct_kingdom_when_we_call_get_kingdom(self):
        actual = self.mammal.get_kingdom()
        self.assertEqual("animals", actual)

    def test_does_it_return_correct_info_when_we_call_info(self):
        actual = self.mammal.info()
        self.assertEqual("MammalName is of type MammalType", actual)


if __name__ == '__main__':
    main()
