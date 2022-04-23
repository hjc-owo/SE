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
public class LoginController {
    @Autowired
    private StudentService studentService;

    @PostMapping("/login")
    public Map<String, Object> login(@RequestBody Map<String, String> re_map, HttpServletRequest request) {
        String username = re_map.get("username");
        String password = re_map.get("password");
        HttpSession session = request.getSession();
        Map<String, Object> map = new HashMap<>();
        try {
            Student student = new Student(username, password);
            Student student1 = studentService.selectStudentByUsername(student.getUsername());
            Object sessionExists = request.getSession().getAttribute("username");
            if (sessionExists != null && sessionExists.equals(username)) {
                map.put("success", false);
                map.put("message", "是不是已经在登录状态了捏～");
            } else if (student1 == null) {
                map.put("success", false);
                map.put("message", "用户名不存在捏～还没注册捏～");
            } else if (!Objects.equals(student1.getPassword(), student.getPassword())) {
                map.put("success", false);
                map.put("message", "密码输错了捏～");
            } else {
                session.setAttribute("username", username);
                session.setAttribute("password", password);
                map.put("success", true);
                map.put("message", "登陆成功了捏～");
            }
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success", false);
            map.put("message", "登录失败了呢，怎么会是呢？");
        }
        return map;
    }
}
