<?php
$mysql = new mysqli("localhost", "root", "jbgsn787", "User");
if ($mysql->connect_errno) {
    die("Disconnection: " . $mysql->connect_error);
}
$password_hash = password_hash($_POST["password"], PASSWORD_DEFAULT);
$name = $_POST["full_name"];

if(isset($_POST["login"])){
    $sql = "SELECT password_hash FROM User WHERE name = '$name'";
    //搜索结果
    $res = $mysql -> query($sql) -> fetch_assoc();

    if($res){
        if(password_verify($_POST["password"], $res["password_hash"])){
            //if matched, go to next page(profile page? search page?)
            echo "<script>window.location.href = 'search_page.html';</script>"; // Fixed missing quotation mark and removed space in URL parameter
        } else {
            //if dismatched
            echo "<script>alert('Incorrect Password! Please try again.'); history.go(-1);</script>"; // Fixed missing quotation mark
        }
    } else {
        echo "<script>alert('You need to register first!'); window.location.href = 'register.html';</script>"; // Fixed missing quotation mark
    }
}
?>
