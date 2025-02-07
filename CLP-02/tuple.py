students = (("Mostakem", 20, 85), ("Atik", 22, 78), ("Shakib", 21, 90));
students_list = list(students);
students_list.sort(key=lambda x: x[2]);
students = tuple(students_list);
print("sorted in ascending order by grade: ",students);
