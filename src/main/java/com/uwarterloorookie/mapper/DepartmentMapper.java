package com.uwarterloorookie.mapper;


import com.uwarterloorookie.bean.Department;
import org.apache.ibatis.annotations.*;

//@Mapper
//指定这是一个操作数据库的mapper
public interface DepartmentMapper {
    @Select("select * from department where id = #{d_id}")
    public Department getDeptById(int d_id);
    @Delete("delete from department where id = #{d_id}")
    public int deleteDeptById(int d_id);
    @Options(useGeneratedKeys = true,keyProperty = "id")//将主键信息封装
    @Insert("insert into department(departmentName) values(#{departmentName})")
    public int insertDept(Department department);
    @Update("update department set departmentName = #{departmentName} where id = #{id}")
    public int updateDept(Department department);
}
