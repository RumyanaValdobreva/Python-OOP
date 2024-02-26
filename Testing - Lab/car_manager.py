from unittest import TestCase, main

# from car_manager import Car


class TestCarManager(TestCase):

    def setUp(self):
        self.car = Car("CarMake", "CarModel", 10, 60)

    def test_correct_initialization(self):
        self.assertEqual("CarMake", self.car.make)
        self.assertEqual("CarModel", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "CarModel", 10, 60)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("CarMake", "", 10, 60)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_invalid_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("CarMake", "CarModel", 0, 60)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_invalid_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("CarMake", "CarModel", 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_not_enough_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount -= 5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_invalid_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_fuel_than_capacity_fills_to_capacity(self):
        self.car.refuel(80)

        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_car_with_valid_fuel(self):
        self.car.refuel(1000)
        self.car.drive(10)

        self.assertEqual(59, self.car.fuel_amount)

    def test_drive_car_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
