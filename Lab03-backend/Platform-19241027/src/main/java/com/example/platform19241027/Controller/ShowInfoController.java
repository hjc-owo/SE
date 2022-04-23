package com.example.platform19241027.Controller;

import com.example.platform19241027.Entity.Student;
import com.example.platform19241027.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

@RestController
public class ShowInfoController {
    @Autowired
    private StudentService studentService;

    @PostMapping("/show_info")
    public Map<String, Object> show_info(@RequestBody String wantUsername, HttpServletRequest request) {
        HttpSession session = request.getSession();
        String username = (String) session.getAttribute("username");
        Map<String, Object> map = new HashMap<>();
        try {
            Student student = studentService.selectStudentByUsername(username);
            if (student == null) {
                map.put("success", false);
                map.put("message", "没登录就想查询？想得美哦～");
            } else if (!Objects.equals(username, wantUsername)) {
                map.put("success", false);
                map.put("message", "不是查自己的？");
            } else {
                map.put("name", student.getUsername());
                map.put("password", student.getPassword());
                map.put("message", "查询成功啦，好耶！");
            }
        } catch (Exception e) {
            e.printStackTrace();
            map.put("name", null);
            map.put("password", null);
            map.put("message", "是不是哪里出了什么问题？");
        }
        return map;
    }
}
