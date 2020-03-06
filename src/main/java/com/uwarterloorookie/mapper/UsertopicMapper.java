package com.uwarterloorookie.mapper;

import com.uwarterloorookie.bean.Usertopics;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface UsertopicMapper {
@Select("select * from usertopics where userid = #{userid}")
  public List<Usertopics> SelecttopicsByuserid(int userid);
@Select("select topictext from usertopics where id = #{topid}")
  public String Gettextbytopicid(int topid);

}
