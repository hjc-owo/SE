package com.example.platform19241027.Service.Impl;

import com.example.platform19241027.Dao.StudentDao;
import com.example.platform19241027.Entity.Student;
import com.example.platform19241027.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StudentServiceImpl implements StudentService {
    @Autowired
    private StudentDao studentDao;

    @Override
    public Student selectStudentByUsername(String username) {
        return studentDao.selectStudentByUsername(username);
    }

    @Override
    public void registerNewStudent(Student student){
        studentDao.registerNewStudent(student);
    }
}
