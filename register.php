<?php
    if(empty($_POST["full_name"])){
        die("Name cannot be empty!");
    }

    if(strlen($_POST["password"]) < 6){
        die("Password needs longer than 6 number!");
    }

    /*if($_POST["password"] !== $_POST["doublecheck"]){
        die("Password Dismatch!");
    }*/

    /*if(!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)){
        die("Invaild Email!");
    }*/

    $password_hash = password_hash($_POST["password"], PASSWORD_DEFAULT);
    $name = $_POST["full_name"];
    $email = $_POST["email"];

    $mysql = new mysqli("localhost", "root", "", "User");
    if($mysql->connect_errno){
        die("Disconnection: ". $mysql->connect_error);
    }

    if(isset($_POST["reg"])){
        $sql = "INSERT INTO UserData (Role, UserName, Email, Password_hash) values ('Customer', '$name', '$email', '$password_hash')";
        $mysql->query($sql);

        if($mysql ->affected_rows > 0){
            echo "<script>alert('Registration successful'); window.location.href = './login.html';</script>";
        }
    }
?>