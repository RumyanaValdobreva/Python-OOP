from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "TestUsername"
    level = 5
    health = 35.5
    damage = 15.5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_correct_initialization(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_valid_attributes_types(self):
        self.assertTrue(isinstance(self.hero.username, str))
        self.assertTrue(isinstance(self.hero.level, int))
        self.assertTrue(isinstance(self.hero.health, float))
        self.assertTrue(isinstance(self.hero.damage, float))

    def test_hero_username_same_as_enemy_hero_username(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_under_or_equal_to_zero(self):
        self.hero.health = 0

        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health -= 1

        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve2.exception))

    def test_enemy_health_under_or_equal_to_zero(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

        enemy.health -= 1

        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(ve2.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-42.0, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_you_win(self):
        enemy = Hero("Enemy", 1, 1, 1)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(39.5, self.hero.health)
        self.assertEqual(20.5, self.hero.damage)

    def test_you_lose(self):
        enemy = Hero("Enemy", 100, 100, 100)

        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(27.5, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_valid_str_method_returns_info(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

        self.assertEqual(expected, self.hero.__str__())


if __name__ == '__main__':
    main()