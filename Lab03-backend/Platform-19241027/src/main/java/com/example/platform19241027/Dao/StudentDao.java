package com.example.platform19241027.Dao;

import com.example.platform19241027.Entity.Student;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface StudentDao {
    public Student selectStudentByUsername(String username);
    public void registerNewStudent(Student student);
}
