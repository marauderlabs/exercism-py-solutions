from typing import List
from typing import Dict
from collections import defaultdict
from bisect import insort


class School:
    def __init__(self):
        # grade to list of sorted students
        self.students: Dict[int, List[str]] = defaultdict(list)

    def add_student(self, name: str, grade: int):
        '''Adds a student to the dict of students keyed by grade
        We proactively maintain a sorted list of students in the grade.
        '''
        students = self.students[grade]
        insort(students, name)

    def roster(self) -> List[str]:
        '''Returns a list of all students in the school, sorted
        by grade and also sorted within the grade'''
        sorted_grades = sorted(self.students.keys())
        sorted_students = []
        for g in sorted_grades:
            sorted_students += self.students[g]
        return sorted_students

    def grade(self, grade_number) -> List[str]:
        '''Returns a list of sorted students within the grade'''
        return self.students[grade_number]
