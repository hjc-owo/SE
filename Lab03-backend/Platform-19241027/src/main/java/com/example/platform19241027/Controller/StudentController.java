package com.example.platform19241027.Controller;

import com.example.platform19241027.Entity.Student;
import com.example.platform19241027.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class StudentController {

    @Autowired
    private StudentService studentService;

    @PostMapping("/register")
    public Map<String, Object> register(@RequestBody Map<String, String> re_map) {
        String username = re_map.get("username");
        String password = re_map.get("password");
        Map<String, Object> map = new HashMap<>();
        try {
            Student student = new Student(username, password);
            Student student1 = studentService.selectStudentByUsername(student.getUsername());
            if (student1 != null) {
                map.put("success", false);
                map.put("message", "用户名已注册，相信聪明的你一定知道怎么办了吧～");
            } else {
                studentService.registerNewStudent(student);
                map.put("success", true);
                map.put("message", "注册成功了呢～");
            }
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success", false);
            map.put("message", "注册失败了呢，怎么会是呢？");
        }
        return map;
    }
}
