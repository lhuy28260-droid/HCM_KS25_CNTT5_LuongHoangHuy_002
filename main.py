class Student:
    def __init__(self,id:str,name:str,theory_score:float,practice_score:float,assignment_score:float,average_score:float,academic_type:str):
        self._id:str = id
        self._name:str = name
        self._theory_score:str = theory_score
        self._practice_score:float = practice_score
        self._assignment_score:float = assignment_score
        self._average_score:float = average_score
        self._academic_type:str = ""

    @property
    def id(self)->str:
        return self._id
    @property
    def name(self)->str:
        return self._name
    @property
    def theory_score(self)->str:
        return self._theory_score
    @property
    def practice_Score(self)->float:
        return self.practice_Score
    @property
    def assignment_score(self)->float:
        return self.assignment_score
    @property
    def average_score(self)->str:
        return self.average_score
    total_score = 0.0
    def calculate_average(self,theory_score,practice_score,assignment_score):
        self.total_score = theory_score * 0.4 + practice_score * 0.4 + assignment_score * 0.2
    
    def classify_academic(self,total_score):
        if total_score < 5.0:
            self._academic_type = "Trung Bình"
        elif 5.0 <= total_score <= 8.0:
            self._academic_type = "Trung Bình"
        elif 6.5 <= total_score <= 8.0:
            self._academic_type = "Khá"
        else:
            self._academic_type = "Giỏi"

class StudentManager(Student):
    def __init__(self):
        self.students = []
    def display(self):
        if len(self.students) == 0:
            print("Danh sách rỗng!!!")
            return
        
        print("Hiển Thị danh sách sinh viên")
        print(" ===============================")
        print(f"{"Mã SV":<5} | {'Họ tên':<10} | {'Điểm lý thuyết':<5} | {'Điểm thực hành':<5} | {'Điểm bài tập':<5} | {'Điểm tổng kết':<5} | {'Học lực':<5}")
        print("====================================")
        for index , stu in enumerate(self.students,1):
            print(f"{index}.{stu['id']:<5} | {stu['name']:<10} | {stu['theory_score']:<5} | {stu['practice_score']:<5} | {stu['asignment_score']:<5} | {self.total_score:<5} | {self._academic_type:<5}")
        return None

    def add_student(self,student):
        input_id = input("Nhập mã sinh viên: ").upper()
        if not input_id:
            print("Mã sinh viên không được rỗng")
            return
        for stu in student:
            if stu.id == input_id:
                print("Mã sinh viên đã tồn tại!!!")
                break
        input_name = input("Nhập họ và tên sinh viên: ")
        if not input_name:
            print("Tên không được rỗng!!!")
            return
        while True:
            try: 
                theory_score = float(input("Nhập điểm lý thuyết: "))
                if not 0 <= theory_score <= 10:
                    print("Điểm phải nhập từ 0 đến 10")
                
                
                
        


def main():
    StudentManager.students = []
    while True:
        print("1.Hiển thị danh sách sinh viên")
        print("2.Thêm sinh viên mới")
        print("3.Cập nhật điểm sinh viên")
        print("4.Xóa sinh viên")
        print("5.Tìm kiếm sinh viên")
        print("6.Thoát")

        choice = input("Nhập lựa chọn của bạn(1->6): ")

        if choice == "1":
            StudentManager.display(StudentManager.students)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Cẩm ơn đã sử dụng chương trình!!!")
            break
        else:
            print("NHập vào không hợp lệ , vui lòng nhập lại")

if __name__ == "__main__":
    main()
    
    


