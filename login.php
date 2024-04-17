<?php
$mysql = new mysqli("localhost", "root", "", "User");
if ($mysql->connect_errno) {
    die("Disconnection: " . $mysql->connect_error);
}
$password_hash = password_hash($_POST["password"], PASSWORD_DEFAULT);
$name = $_POST["full_name"];

if(isset($_POST["login"])){
    $sql = "SELECT Password_hash FROM UserData WHERE UserName = '$name'";
    //搜索结果
    $res = $mysql -> query($sql) -> fetch_assoc();

    if($res){
        if(password_verify($_POST["password"], $res["Password_hash"])){
            //if matched, go to next page(profile page? search page?)
            echo "<script>window.location.href = 'search_page.html';</script>";
        } else {
            //if dismatched
            echo "<script>alert('Incorrect Password! Please try again.'); history.go(-1);</script>";
        }
    } else {
        echo "<script>alert('You need to register first!'); window.location.href = 'register.html';</script>";
    }
}
?>
