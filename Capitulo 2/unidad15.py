#quizz del final de la unidad 01
student_tup = [('211101', 'David Doe', '010-123-1111'), ('211102','John Smith', '010-123-2222'), ('211103', 'Jane Carter', '010-123-3333')]

student_dic = {student[0]: (student[1], student[2]) for student in student_tup}

for student in student_tup:
    student_id, student_name, student_phone = student
    print(f"{student_id} : {student_name}")

student_id = input("Ingrese el numero de identificacion del estudiante: ")

if student_id in student_dic:
    student_info = student_dic[student_id]
    print(
        f"{student_id} es el estudiante {student_info[0]} y su numero de telefono es: {student_info[1]}")
else:
    print(
        f"no se encontro ningun estudiante con el numero de identificacion.{student_id}")
    print("Fin del programa")