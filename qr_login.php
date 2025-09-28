<?php
session_start();
$username = $_POST['username'];
$email = $_POST['email'];

// For simulation, generate OTP and store in session
$otp = rand(100000, 999999);
$_SESSION['otp'] = strval($otp);

echo "<h2>Scan QR Code or Enter OTP</h2>";
echo "<p>OTP for $username has been generated.</p>";
echo "<p><strong>OTP:</strong> $otp</p>"; // Normally QR or email
?>

<form method="POST" action="verify.php">
    <input type="text" name="otp" placeholder="Enter OTP">
    <button type="submit">Verify OTP</button>
</form>
