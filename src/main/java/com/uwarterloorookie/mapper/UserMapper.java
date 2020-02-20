package com.uwarterloorookie.mapper;

import com.uwarterloorookie.bean.User;
import org.apache.ibatis.annotations.Select;

public interface UserMapper {

    @Select("select * from users where passWord = #{passWord} and userName = #{userName} ")
    public User getUser(String passWord, String userName);
    @Select("SELECT * FROM users where id = #{id}")
    public User gerUserById(int id);

}
