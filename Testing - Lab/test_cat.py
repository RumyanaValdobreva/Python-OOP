from unittest import TestCase, main

# from cat import Cat


class CatTest(TestCase):
    def setUp(self):
        self.cat = Cat("TestCat")

    def test_correct_initialization(self):
        self.assertEqual("CatName", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_expect_fed_and_sleepy_cat_with_increased_size(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.sleepy)
        self.assertTrue(self.cat.fed)

    def test_result_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_sleeping_cat_when_cat_is_fed(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleeping_cat_when_cat_is_hungry_raises_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == "__main__":
    main()