<?php

function isValid($from_email, $to_email, $subject, $body) {
    return checkEmail($from_email) && 
           filter_var($from_email, FILTER_VALIDATE_EMAIL) &&
           checkEmail($to_email) && 
           filter_var($to_email, FILTER_VALIDATE_EMAIL) &&
           checkString($subject) && 
           strlen(trim($body)) > 0;
}

function checkEmail($email) {
    $email_regex = '/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/';
    return preg_match($email_regex, $email) === 1;
}

function checkString($string) {
    $string_regex = "/^[A-Za-z .'-]+$/";
    return preg_match($string_regex, $string) === 1;
}

function sendMail($from_email, $to_email, $subject, $body) {
    $headers = "From: $from_email\r\n" .
               "Reply-To: $from_email\r\n" .
               "X-Mailer: PHP/" . phpversion() . "\r\n" .
               "MIME-Version: 1.0\r\n" .
               "Content-type: text/html; charset=UTF-8\r\n";

    return @mail($to_email, $subject, $body, $headers);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $from_email = $_POST['fromemail'] ?? '';
    $to_email = $_POST['toemail'] ?? '';
    $subject = $_POST['subject'] ?? '';
    $body = $_POST['body'] ?? '';

    if (empty($from_email) || empty($to_email) || empty($body)) {
        http_response_code(400);
        echo "Missing required fields.";
        exit();
    }

    if (!isValid($from_email, $to_email, $subject, $body)) {
        http_response_code(422);
        echo "Invalid input.";
        exit();
    }

    if (sendMail($from_email, $to_email, $subject, $body)) {
        http_response_code(200);
        echo "Email sent successfully.";
    } else {
        http_response_code(500);
        echo "Failed to send email.";
    }
}
