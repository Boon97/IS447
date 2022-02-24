<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->


<?php
    require_once 'common.php';
    // session_destroy();
    // $dbServername = "localhost";
    // $dbUsername = "root";
    // $dbPassword= "";
    // $dbName = "staff_details";

    // $conn = mysqli_connect($dbServername, $dbUsername,$dbPassword,$dbName);

    // $sql = "SELECT * FROM staff_login";
    // $result = mysqli_query($conn,$sql);
    // $resultCheck = mysqli_num_rows($result);

    // if ($resultCheck> 0){
    //     while ($row = mysqli_fetch_assoc($result)){
    //         echo $row['name'];
    //     }
    // }

    if (isset($_POST['submit'])){

        $employee_id = intval($_POST['employee_id']);
        $password = $_POST['password'];
        $userdao = new UserDAO();
        $user = $userdao->get($employee_id);
        var_dump($user);
    }


?>
<html>
    <body>
        <div id="login">
            <h3 class="text-center text-white pt-5">Login form</h3>
            <div class="container">
                <div id="login-row" class="row justify-content-center align-items-center">
                    <div id="login-column" class="col-md-6">
                        <div id="login-box" class="col-md-12">
                            <form id="login-form" class="form" action="" method="post">
                                <h3 class="text-center text-info">Login</h3>
                                <div class="form-group">
                                    <label for="employee_id" class="text-info">Employee ID:</label><br>
                                    <input type="text" name="employee_id" id="employee_id" class="form-control">
                                </div>
                                <div class="form-group">
                                    <label for="password" class="text-info">Password:</label><br>
                                    <input type="text" name="password" id="password" class="form-control">
                                </div>
                                <div class="form-group">
                                    <label for="remember-me" class="text-info"><span>Remember me</span>? <span><input id="remember-me" name="remember-me" type="checkbox"></span></label><br>
                                    <input type="submit" name="submit" class="btn btn-info btn-md" value="submit">
                                </div>
                                <div id="register-link" class="text-right">
                                    <a href="#" class="text-info">Register here</a>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>    


    <?php
        if (isset($_POST['submit'])){
            if (!isset($user)){
            echo "Username does not exist!";
            }
        
            if (isset($user)){
                if ($user->getPassword() != $password){
                    echo"Password is Not Valid!";
                }
            


                if ( ($user->getemployee_id() == $employee_id) && ($user->getpassword() == $password)){
                    $checker = True;

                    session_start();
                    $_SESSION["employee_id"] = $user->getemployee_id();
                    $_SESSION["password"] = $user->getpassword();
                    $_SESSION["name"] = $user->getname();
                    $_SESSION["email"] = $user->getemail();
                    $_SESSION["phone"] = $user->getphone();


                    // header("Location: login_success.html");
        
                }

            }
                    

        }
?>  
