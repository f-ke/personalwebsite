package com.uwarterloorookie.controller;

import com.uwarterloorookie.bean.User;
import com.uwarterloorookie.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.thymeleaf.util.StringUtils;

import javax.servlet.http.HttpSession;
import java.util.Map;

@Controller
public class LoginController {
    @Autowired
    UserMapper userMapper;
    @PostMapping("/user/login")

    public String login(@RequestParam("username") String userName, @RequestParam("password") String passWord, Map<String, Object> map,
                        HttpSession session, Model model) {


        User user1 =  userMapper.getUser(passWord, userName);
        if(user1 != null){
            session.setAttribute("loginuser", userName);
            model.addAttribute("user",user1);
            System.out.println(user1);
           return "/home";


        }else{
            map.put("msg", "Wrong password or Username");
            return "/login";

        }

   }
   @GetMapping("/myhome/{id}")

   public String gethome(Model model, @PathVariable("id") int id){
       User user1 = userMapper.gerUserById(id);
       model.addAttribute("user", user1);
       return "/home";

   }
  @GetMapping("/mytest")

  public String gettest(){

      return "/myhome/{id}";

  }
}
