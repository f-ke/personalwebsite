package com.uwarterloorookie.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class hellocontroller {
    @ResponseBody
    @RequestMapping("/sucess")
    public String sucees(){
        return"/sucess";
    }

}
