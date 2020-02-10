from typing import List
from typing import Dict


class Garden:
    def __init__(self, diagram: str, students: List[str] = None):
        self.DEFAULT_STUDENTS: List[str] = [
            'Alice',
            'Bob',
            'Charlie',
            'David',
            'Eve',
            'Fred',
            'Ginny',
            'Harriet',
            'Ileana',
            'Joseph',
            'Kincaid',
            'Larry',
        ]
        self.students = sorted(students or self.DEFAULT_STUDENTS)
        self.diagram: List[str] = diagram.split('\n')
        self.columns: int = len(self.diagram[0])/2
        self.plant_codes: Dict[str, str] = {
            'V': 'Violets',
            'C': 'Clover',
            'R': 'Radishes',
            'G': 'Grass',
        }
        self.student_index = {c: i for i, c in enumerate(self.students)}

    def plants(self, student: str) -> List[str]:
        # Let the KeyError thrown, denote invalid input - no such student
        index = self.student_index[student]
        if self.columns < index:
            raise ValueError(student + " has no cup in the garden")
        index *= 2
        return [self.plant_codes[code] for row in self.diagram
                for code in row[index:index+2]]
