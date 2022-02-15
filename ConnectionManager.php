<?php

class ConnectionManager {

    public function connect() {
        $servername = 'localhost';
        $username = 'root';
        $password = '';
        $dbname = 'staff_details';
        
        $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);     

        return $conn;
    }

}