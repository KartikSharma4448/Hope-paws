<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'src/Exception.php';
require 'src/PHPMailer.php';
require 'src/SMTP.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $number = htmlspecialchars($_POST['number']);

    $message = htmlspecialchars($_POST['message']);

    $mail = new PHPMailer(true);

    try {
        // SMTP configuration
        $mail->isSMTP();
        
        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;
        $mail->SMTPDebug = 0; // Detailed SMTP debug output

        $mail->Username = 'kartikuma9261@gmail.com'; // Your Gmail address
        $mail->Password = 'nass litu tusc pekp'; // Your Gmail App Password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        // Email settings
        $mail->setFrom('kartikuma9261@gmail.com', 'HopePaws Emergency');
        $mail->addAddress('kartikuma9261@gmail.com'); // Where you receive reports

        $mail->isHTML(true);
        $mail->Subject = "New Emergency Report from $name";
        $mail->Body = "
            <h3>Emergency Report Details:</h3>
            <p><strong>Name:</strong> $name</p>
            <p><strong>email:</strong> $email</p>
            <p><strong>number:</strong> $number</p>
            <p><strong>message:</strong> $message</p>
        ";
       
        $mail->send();
        echo "Thank you! Your emergency report has been submitted.";
    } catch (Exception $e) {
        echo "Error: {$mail->ErrorInfo}";
    }
}
?>
