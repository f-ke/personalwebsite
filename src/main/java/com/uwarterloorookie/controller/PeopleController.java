package com.uwarterloorookie.controller;

import com.uwarterloorookie.bean.User;
import com.uwarterloorookie.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
public class PeopleController {
    @Autowired
    UserMapper userMapper;
    @GetMapping("/mypeople/{id}")
    public String getmypeople(Model model, @PathVariable("id") int id){
        User user1 = userMapper.gerUserById(id);
        model.addAttribute("user", user1);
        return"/people";

    }

}
