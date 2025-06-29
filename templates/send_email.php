<?php
function sendContactEmail($name, $email, $number, $message) {
    $to = "gta.thelegend@gmail.com"; // <-- Replace with your real email
    $subject = "New Contact Form Submission";
    $body = "You have received a new message from HopePaws contact form:\n\n" .
            "Name: $name\n" .
            "Email: $email\n" .
            "Number: $number\n" .
            "Message:\n$message\n";

    $headers = "From: $email\r\n" .
               "Reply-To: $email\r\n" .
               "X-Mailer: PHP/" . phpversion();

    return mail($to, $subject, $body, $headers);
}
?>
