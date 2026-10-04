from core_concepts.analyzer import StudentAnalyzer

students = [
    {"name": "Bushra", "marks": [88, 92, 85, 90]},
    {"name": "Aisha", "marks": [76, 81, 79, 84]},
    {"name": "Sara", "marks": [94, 91, 96, 93]},
]

analyzer = StudentAnalyzer(students)
analyzer.display_report()
