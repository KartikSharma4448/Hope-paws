<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'src/Exception.php';
require 'src/PHPMailer.php';
require 'src/SMTP.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $transaction_number = htmlspecialchars($_POST['transaction_number']);
    $Mobile_Number = htmlspecialchars($_POST['Mobile_Number']);
    $Amount = htmlspecialchars($_POST['Amount']);
    

    $mail = new PHPMailer(true);

    try {
        // SMTP configuration
        $mail->isSMTP();
        
        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;
        $mail->Username = 'kartikuma9261@gmail.com'; // Your Gmail address
        $mail->Password = 'nass litu tusc pekp'; // Your Gmail App Password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        // Email settings
        $mail->setFrom('kartikuma9261@gmail.com', 'HopePaws Emergency');
        $mail->addAddress('kartikuma9261@gmail.com'); // Where you receive reports

        $mail->isHTML(true);
        
        $mail->Subject = "Donation from $name";
        $mail->Body = "
            <h3>Donation Details:</h3>
            <p><strong>Name:</strong> $name</p>
            <p><strong>Transaction Number:</strong> $transaction_number</p>
            <p><strong>Mobile Number:</strong> $Mobile_Number</p>
            <p><strong>Amount:</strong> $Amount</p>
        ";

        $mail->send();
        echo "Thank you! Your emergency report has been submitted.";
    } catch (Exception $e) {
        echo "Error: {$mail->ErrorInfo}";
    }
}
?>
