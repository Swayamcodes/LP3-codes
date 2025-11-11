// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

contract StudentData {

    struct Student {
        string name;
        uint age;
        uint roll;
    }

    Student[] private students;
    mapping(uint => bool) private rollExists;

    function addStudent(string memory name, uint age, uint roll) public {
        require(!rollExists[roll], "Roll Number Already Exists");
        students.push(Student(name, age, roll));
        rollExists[roll] = true;
    }

    function viewStudentAtIndex(uint index)
        public
        view
        returns (string memory name, uint age, uint roll)
    {
        require(index < students.length, "Index out of range");

        Student memory current = students[index];
        return (current.name, current.age, current.roll);
    }

    function getAllStudents() public view returns (Student[] memory) {
        return students;
    }

    function getStudentByRollNo(uint rollNo)
        public
        view
        returns (string memory name, uint age, uint roll)
    {
        for (uint i = 0; i < students.length; i++) {
            if (students[i].roll == rollNo) {
                return (students[i].name, students[i].age, students[i].roll);
            }
        }
        revert("Student Not Found");
    }

    function updateStudent(uint rollNo, string memory newName, uint newAge) public {
        for (uint i = 0; i < students.length; i++) {
            if (students[i].roll == rollNo) {
                students[i].name = newName;
                students[i].age = newAge;
                return;
            }
        }
        revert("Student Not Found");
    }

    function deleteStudent(uint rollNo) public {
        for (uint i = 0; i < students.length; i++) {
            if (students[i].roll == rollNo) {
                students[i] = students[students.length - 1];
                students.pop();
                rollExists[rollNo] = false;
                return;
            }
        }
        revert("Student Not Found");
    }

    function getSize() public view returns (uint size) {
        return students.length;
    }

    receive() external payable {
        revert("ETH Received");
    }

    fallback() external payable {
        revert("Invalid function call");
    }
}
