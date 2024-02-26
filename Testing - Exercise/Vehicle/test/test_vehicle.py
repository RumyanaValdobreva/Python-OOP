from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.5, 150.5)

    def test_correct_initialization(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(150.5, self.vehicle.horse_power)
        self.assertEqual(10.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_valid_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_enough_fuel_to_drive(self):
        self.vehicle.drive(5)
        self.assertEqual(4.25, self.vehicle.fuel)

    def test_drive_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_valid_fuel_quantity(self):
        self.vehicle.fuel = 2

        self.vehicle.refuel(1.5)
        self.assertEqual(3.5, self.vehicle.fuel)

    def test_refuel_when_fuel_is_too_much_raises_exception(self):
        self.vehicle.fuel = 1

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(15)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_return_valid_str(self):
        expected = f"The vehicle has 150.5 " \
                   f"horse power with 10.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == '__main__':
    main()
