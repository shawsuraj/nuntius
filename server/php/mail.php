<?php

function isValid() {
  if (checkEmail($_POST['fromemail']) &&
      checkEmail($_POST['toemail']) &&
      checkString($_POST['subject']) &&
      strlen($_POST['body']) > 0) {
        return true;
      }
      
  return false;
}

function checkEmail($email) {
  $email_regex = '/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/';
  if (!preg_match($email_regex, $email)) {
    return false;
  }
  return true;
}

function checkString($string) {
  $string_regex = "/^[A-Za-z .'-]+$/";
  if (!preg_match($string_regex, $string)) {
    return false;
  }
  return true;
}

if (isValid()) {
  $from_email = $_POST['fromemail']; // required
  $to_email = $_POST['toemail'];  // required
  $subject = $_POST['subject'];
  $content = $_POST['body'];  // required

  $headers = "" .
    "From: ".$from_email."\r\n".
    "Reply-To: ".$from_email."\r\n" .
    "X-Mailer: PHP/" . phpversion();
  $headers .= 'MIME-Version: 1.0' . "\r\n";
  $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
  @mail($to_email, $subject, $content, $headers);
}
?>
