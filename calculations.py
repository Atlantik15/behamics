class Calculations:
    def sum(self, number1, number2):
        return number1 + number2

    def calculate_exam_grade(self, points):
        grade = "Your grade is: "
        if 0 <= points <= 49 :
            return grade + "5"
        elif 50 <= points <= 59:
            return grade + "6"
        elif 60 <= points <= 69:
            return grade + "7"
        elif 70 <= points <= 79:
            return grade + "8"
        elif 80 <= points <= 85:
            return grade + "9"
        elif 86 <= points <= 100:
            return grade + "10"

    def minmax(self, grades):
        if not grades:
            return "Grade list is empty"

        if len(grades) == 1:
            return "Minimum and the maximum value is:" + grades.values

        maxGrade = max(grades, key=grades.get)
        minGrade = min(grades, key=grades.get)

        print(maxGrade)
        print(minGrade)

        return "Minimum value: " + str(grades[minGrade]) + " Maxiumum value: " + str(grades[maxGrade])