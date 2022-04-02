from openpyxl import load_workbook
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def string_parser(s: str) -> str:
    while "-\n" in s:
        ind = s.index("-\n")
        s = s[:ind] + s[ind + 2:]
    while "," in s:
        ind = s.index(",")
        s = s[:ind] + s[ind + 1:]
    if '\n' in s:
        s = s.split('\n')[-2]
        
    return s

def remove_rows(matrix_data, rows_array):
    matrix_data = [[word for i, word in enumerate(line) if i not in rows_array] for line in matrix_data]
    return matrix_data

class Student_Entries():
    def __init__(self):
        self.students = defaultdict(dict)
        self.subjects = defaultdict(list)
        self.average_marks = defaultdict(float)
        self.standard_deviation = defaultdict(float)
        self.covariance = defaultdict(float)
        self.correlation = defaultdict(float)
        
    def add_student(self, name, subjects, marks):
        for i, subject in enumerate(subjects):
            if subject in self.students[name]:
                if isinstance(self.students[name][subject], list):
                    self.students[name][subject].append(marks[i])
                else:
                    self.students[name][subject] = [self.students[name][subject], marks[i]]
            else:
                self.students[name][subject] = marks[i]
    
    def print_students(self):
        for name, subjects in self.students.items():
            print(name, subjects)
            print()
            
    def marks_by_subject(self):
        marks_by_subject = defaultdict(list)
        for student in self.students:
            for subject, marks in self.students[student].items():
                if isinstance(marks, list):
                    for mark in marks:
                        self.subjects[subject].append(mark)
                else:
                    self.subjects[subject].append(marks)
    
    def average_marks_by_subject(self):
        self.marks_by_subject()
        average_marks = defaultdict(float)
        
        for subject, marks in self.subjects.items():
            self.average_marks[subject] = sum(marks) / len(marks)
    
    def print_average_marks(self):
        self.average_marks_by_subject()
        for subject in self.average_marks:
            print(f"Средняя оценка по {subject}: {average_marks[subject]:.2f}")
            
    def standard_deviation_by_subject(self):
        self.average_marks_by_subject()
        for subject, marks in self.subjects.items():
            standard_deviation = 0
            for mark in marks:
                standard_deviation += (mark - self.average_marks[subject]) ** 2
            self.standard_deviation[subject] = standard_deviation / (len(marks) - 1)
            
    def print_standard_deviation(self):
        self.standard_deviation_by_subject()
        for subject in self.standard_deviation:
            print(f"Стандартное отклонение для {subject}: {self.standard_deviation[subject]:.4f}")
            
    def print_variance(self):
        self.standard_deviation_by_subject()
        for subject in self.standard_deviation:
            print(f"Дисперсия для {subject}: {self.standard_deviation[subject] ** 2:.4f}")
    
    def print_stats(self):
        self.standard_deviation_by_subject()
        for subject in self.subjects:
            print(f"Результаты по предмету \"{subject}\": ")
            print(f"    Средняя оценка: {self.average_marks[subject]:.2f}")
            print(f"    Стандартное отклонение: {self.standard_deviation[subject]:.4f}")
            print(f"    Дисперсия: {self.standard_deviation[subject] ** 2:.4f}")
            print()
    
    def graph_marks_by_subject(self, save = False):
        self.standard_deviation_by_subject()
        
        for subject, marks in self.subjects.items():
            xs = [2, 3, 4, 5]
            cnt = Counter(marks)
            ys = [cnt[x] / len(marks) * 100 for x in xs]
            plt.figure(figsize = (12, 7))
            plt.bar(xs, ys, color = "silver", edgecolor = "gray", alpha = 0.9)
            plt.title(f"Гистограмма оценок по предмету \"{subject}\"", size = 14, family = "serif", alpha = 0.85, weight = "heavy")
            plt.xlabel("Оценки по предмету", size = 14, family = "serif", alpha = 0.85)
            plt.ylabel("Доля оценок в процентах", size = 14, family = "serif", alpha = 0.85)
            plt.axis([1.5, 5.5, 0, max(ys) * 1.05]);
            plt.xticks(xs)
            plt.yticks(range(0, int(max(ys)) + 10, 10))
            if save:
                plt.savefig(f"Гистограмма оценок по предмету {subject}")
            plt.show()
    
    def covariance_by_subjects(self):
        self.standard_deviation_by_subject()
        subject_list = sorted(self.subjects.keys())
        for i in range(0, len(subject_list) - 1):
            for j in range(i + 1, len(subject_list)):
                covariance = 0
                n = min(len(self.subjects[subject_list[i]]), len(self.subjects[subject_list[j]]))
                for k in range(n):
                    covariance += (self.subjects[subject_list[i]][k] - self.average_marks[subject_list[i]]) * \
                                   (self.subjects[subject_list[j]][k] - self.average_marks[subject_list[j]])
                self.covariance[(subject_list[i], subject_list[j])] = covariance / (n - 1)
                           
    def print_covariance(self):
        self.covariance_by_subjects()
        for pair, value in sorted(self.covariance.items(), key = lambda item: item[1], reverse = True):
            print(f"{pair}: {value:.4f}")
                
    def correlation_by_subjects(self):
        self.covariance_by_subjects()
        for (subject1, subject2), covariance in self.covariance.items():
            self.correlation[(subject1, subject2)] = covariance / self.standard_deviation[subject1] / self.standard_deviation[subject2]
    
    def print_correlation(self, tolerance = 0):
        self.correlation_by_subjects()
        for pair, value in sorted(self.correlation.items(), key = lambda item: item[1], reverse = True):
            if (abs(value) > tolerance):
                print(f"{pair}: {value:.4f}")
        
def mark_translate(mark):
    if mark == "отлично":
        return 5
    elif mark == "хорошо":
        return 4
    elif mark == "удовл.":
        return 3
    else:
        return 2

def name_aliases(name):
    if name == "Алгоритмические языки и программирование":
        return "Алгоритмизация и программирование"
    elif name == "История":
        return "История (история России, всеобщая история)"
    return name

#Вход: название файла + название страницы + (Год_поступления, группа, семестр)
lan = "en"
if lan == 'ru':
    inputs = [["2021 г.н. (сейчас 1 курс - только 1 семестр).xlsx", "ПМИ 1-1 - 1 семестр", (2021, 1, 1)],
          ["2021 г.н. (сейчас 1 курс - только 1 семестр).xlsx", "ПМИ 1-2 - 1 семестр", (2021, 2, 1)],
          ["2020 г.н. (сейчас 2 курс).xlsx", "1 семестр", (2020, 1, 1)],
          ["2020 г.н. (сейчас 2 курс).xlsx", "2 семестр", (2020, 1, 2)],
          ["2019 г.н. (сейчас 3 курс).xlsx", "1 семестр", (2019, 1, 1)],
          ["2019 г.н. (сейчас 3 курс).xlsx", "2 семестр", (2019, 1, 2)],
          ["2018 г.н. (сейчас 4 курс).xlsx", "1 семестр", (2018, 1, 1)],
          ["2018 г.н. (сейчас 4 курс).xlsx", "2 семестр", (2018, 1, 2)],
          ["2017 г.н. (выпукс 2021 года).xlsx", "1 семестр", (2017, 1, 1)],
          ["2017 г.н. (выпукс 2021 года).xlsx", "2 семестр", (2017, 1, 2)]
         ]
else:
    inputs = [["2021_g_n__seychas_1_kurs_-_tolko_1_semestr.xlsx", "ПМИ 1-1 - 1 семестр", (2021, 1, 1)],
          ["2021_g_n__seychas_1_kurs_-_tolko_1_semestr.xlsx", "ПМИ 1-2 - 1 семестр", (2021, 2, 1)],
          ["2020_g_n__seychas_2_kurs.xlsx", "1 семестр", (2020, 1, 1)],
          ["2020_g_n__seychas_2_kurs.xlsx", "2 семестр", (2020, 1, 2)],
          ["2019_g_n__seychas_3_kurs.xlsx", "1 семестр", (2019, 1, 1)],
          ["2019_g_n__seychas_3_kurs.xlsx", "2 семестр", (2019, 1, 2)],
          ["2018_g_n__seychas_4_kurs.xlsx", "1 семестр", (2018, 1, 1)],
          ["2018_g_n__seychas_4_kurs.xlsx", "2 семестр", (2018, 1, 2)],
          ["2017_g_n__vypusk_2021_goda.xlsx", "1 семестр", (2017, 1, 1)],
          ["2017_g_n__vypusk_2021_goda.xlsx", "2 семестр", (2017, 1, 2)]
         ]

students_data = Student_Entries()

for input in inputs:
    wb = load_workbook(filename = input[0])
    page = wb[input[1]]
    subjects = []
    exams_col = []

    for i, word in enumerate(page[11]):
        if (page[12][i].value == "Курсовой проект" or page[12][i].value == "Экзамен"):
            subjects.append(name_aliases(page[11][i].value))
            exams_col.append(i)

    for i in range(16, 100):
        if page[i][0].value == None:
            break
        name = page[i][3].value
        marks = []
        
        for mark in exams_col:
            val = str(page[i][mark].value)
            if '\n' in val:
                val = val.split('\n')[-2]
            marks.append(mark_translate(val))
            
        students_data.add_student(name, subjects, marks)

students_data.print_correlation()
