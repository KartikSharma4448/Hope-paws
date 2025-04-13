<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'src/Exception.php';
require 'src/PHPMailer.php';
require 'src/SMTP.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['Name']);
    $email = htmlspecialchars($_POST['Email']);
    $phone = htmlspecialchars($_POST['Phone']);
    $location = htmlspecialchars($_POST['Location']);
    $description = htmlspecialchars($_POST['Description']);

    $mail = new PHPMailer(true);

    try {
        // SMTP configuration
        $mail->isSMTP();
        
        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;
        $mail->Username = 'kartikuma9261@gmail.com'; // Your Gmail address
        $mail->Password = 'rbjx njxx hkks gdud'; // Your Gmail App Password
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
            <p><strong>Email:</strong> $email</p>
            <p><strong>Phone:</strong> $phone</p>
            <p><strong>Location:</strong> $location</p>
            <p><strong>Description:</strong> $description</p>
        ";
       
        $mail->send();
        echo "Thank you! Your emergency report has been submitted.";
    } catch (Exception $e) {
        echo "Error: {$mail->ErrorInfo}";
    }
}
?>
