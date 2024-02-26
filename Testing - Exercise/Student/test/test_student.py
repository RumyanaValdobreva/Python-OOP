from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("TestName", {"Python": ["note1", "note2", "note3"]})
        self.student_2 = Student("Student 2")

    def test_correct_initialization_with_courses(self):
        self.assertEqual("TestName", self.student.name)
        self.assertEqual({"Python": ["note1", "note2", "note3"]}, self.student.courses)

    def test_correct_initialization_without_courses(self):
        self.assertEqual("Student 2", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_correct_attributes_types(self):
        self.assertIsInstance(self.student.name, str)
        self.assertIsInstance(self.student_2.name, str)

    def test_enroll_if_there_is_existing_course(self):
        result = self.student.enroll("Python", ["note4", "note5"], add_course_notes="n")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["note1", "note2", "note3", "note4", "note5"]}, self.student.courses)

        result = self.student.enroll("Python", ["note6", "note7"], add_course_notes="Y")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["note1", "note2", "note3", "note4", "note5", "note6", "note7"]},
                         self.student.courses)

    def test_enroll_when_course_not_existed_with_y(self):
        result = self.student.enroll("JavaScript", ["note1", "note2"], "Y")

        self.assertIn("JavaScript", self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2"], self.student.courses["JavaScript"])

    def test_enroll_when_course_not_existed_with_empty_space(self):
        result = self.student.enroll("JavaScript", ["note1", "note2"], "")

        self.assertIn("JavaScript", self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2"], self.student.courses["JavaScript"])

    def test_enroll_not_existing_course_without_added_notes(self):
        result = self.student.enroll("JavaScript", ["note1", "note2"], "k")

        self.assertIn("JavaScript", self.student.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["JavaScript"])

    def test_add_notes_successfully_to_existing_course(self):
        self.student_2.enroll("JavaScript", ["note1", "note2"])

        result = self.student_2.add_notes("JavaScript", "note3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1", "note2", "note3"], self.student_2.courses["JavaScript"])

    def test_add_notes_to_not_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("JavaScript", "note3")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_exising(self):
        result = self.student.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student.courses)

    def test_leave_course_when_course_not_existing(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("C#")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()