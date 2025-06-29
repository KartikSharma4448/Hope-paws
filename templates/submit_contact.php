<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Include email sending logic
require 'send_email.php';

// Collect form data
$name = $_POST['name'] ?? '';
$email = $_POST['email'] ?? '';
$number = $_POST['number'] ?? '';
$message = $_POST['message'] ?? '';

// Basic validation
if (empty($name) || empty($email) || empty($message)) {
    echo "All fields are required.";
    exit;
}

// Send the email
$success = sendContactEmail($name, $email, $number, $message);

if ($success) {
    echo "Message sent successfully!";
    // You can also redirect to a thank-you page
    // header("Location: thank_you.html");
} else {
    echo "Failed to send message. Please try again later.";
}
?>
