// SPDX-License-Identifier: MIT
pragma solidity >= 0.8;

contract Employee{
    struct details{
        uint8 empId;
        string empName;
        string department;
        uint32 salary;
    }
    mapping (uint8=>details) empMap;

    function addEmployee(uint8 id,string memory name,string memory dept,uint32 sal) public{
        details memory e=details(id,name,dept,sal);
        empMap[id]=e;
    }

    function displayEmployee(uint8 id) public view returns(details memory){
        details memory e=empMap[id];
        if(e.salary > 30000){
            e.salary+=5000;
        }
        return e;

    }

}
