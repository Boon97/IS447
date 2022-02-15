<?php

class UserDAO {
       
    // Given $username 
    // Returns null if the $username is not found in accounts database table.
    // Returns an User object if $username is found in accounts database table.

    public function get( $employee_id ) {

        $connMgr = new ConnectionManager();
        $conn = $connMgr->connect();

        $sql = "SELECT employee_id, name, password, email, phone 
        FROM staff_login
        WHERE employee_id = :employee_id";
        $stmt = $conn->prepare($sql);
        $stmt->bindParam(":employee_id", $employee_id, PDO::PARAM_STR);

        $user = null;
        if ( $stmt->execute() ) {

            $stmt->setFetchMode(PDO::FETCH_ASSOC);

            while ( $row = $stmt->fetch() ) {
                $user = new User(
                                $row["employee_id"], 
                                $row["name"], 
                                $row["password"],
                                $row["email"],
                                $row["phone"]
                                
                        );
            }

        }

        $stmt = null;
        $conn = null;        

        return $user;
    }
}
?>