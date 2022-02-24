<?php

    class User {

        private $employee_id;
        private $password;
        private $name;
        // private $role;

        function __construct($employee_id, $name, $password, $email, $phone) {
            $this->employee_id = $employee_id;
            $this->name = $name;
            $this->password = $password;
            $this->email = $email;
            $this->phone = $phone;
            
            // $this->role = $role;
        }

        public function getemployee_id() {
            return $this->employee_id;
        }

        public function getname() {
            return $this->name;
        } 
        
        public function getpassword() {
            return $this->password;
        }

        public function getemail() {
            return $this->email;
        }

        public function getphone() {
            return $this->phone;
        }

        

        // public function getRole() {
        //     return $this->role;
        // }

    }

?>