package com.example.platform19241027.Service;

import com.example.platform19241027.Entity.Student;

public interface StudentService {
    public Student selectStudentByUsername(String username);
    public void registerNewStudent(Student student);
}
