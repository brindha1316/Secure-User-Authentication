<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $entered_otp = $_POST['otp'];
    $stored_otp = $_SESSION['otp'];

    if ($entered_otp === $stored_otp) {
        echo "<h3>Authentication Successful</h3>";
    } else {
        echo "<h3>Invalid OTP</h3>";
    }
}
?>
