class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calculateResult(self):
        if(self.sub1>40 and self.sub2>40 and self.sub3>40):
            return (self.sub1+self.sub2+self.sub3)/3
        return 0
class School:
    def __init__(self,name,studentDict):
        self.name = name
        self.studentDict = studentDict
    def getStudentResult(self):
        for student in self.studentDict:
            if(student.calculateResult()>60):
                self.studentDict[student] = 'pass'
        return self.studentDict
            
    def findStudentWithHighestMarks(self,passedStudents):
        if(len(passedStudents)==0):
            return None
        topper = passedStudents[0]
        for student in passedStudents:
            if(topper.calculateResult()<student.calculateResult()):
                topper = student
        return topper



def main():
    N = int(input())
    studentDict = dict()
    for i in range(N):
        name = input()
        sub1 = int(input())
        sub2 = int(input())
        sub3 = int(input())
        student = Student(name,sub1,sub2,sub3)
        studentDict[student]='fail'
    schoolName = input()
    school = School(schoolName,studentDict)
    studentDict = school.getStudentResult()

    passedStudents = []
    for student in studentDict:
        if(studentDict[student]=='pass'):
            passedStudents.append(student);
    
    for i in passedStudents:
        print(i.name)
    if(school.findStudentWithHighestMarks(passedStudents)==None):
        print('No Student Passed')
    
    else:
        print(school.findStudentWithHighestMarks(passedStudents).name)

main()