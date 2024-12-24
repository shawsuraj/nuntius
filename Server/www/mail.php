<?php

function isValid($from_email, $to_email, $subject, $body) {
  if ((checkEmail($from_email) && filter_var($from_email, FILTER_VALIDATE_EMAIL)) &&
      (checkEmail($to_email) && filter_var($to_email, FILTER_VALIDATE_EMAIL)) &&
      checkString($subject) &&
      strlen($body) > 0) {
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

function sendMail($from_email, $to_email, $subject, $body) {
  try {
    $headers = "" .
    "From: ".$from_email."\r\n".
    "Reply-To: ".$from_email."\r\n" .
    "X-Mailer: PHP/" . phpversion();
    $headers .= 'MIME-Version: 1.0' . "\r\n";
    $headers .= 'Content-type: text/html; charset=UTF-8' . "\r\n";
    @mail($to_email, $subject, $body, $headers);

    return true;
  }
  catch (Exception $e) {
    return false;
  }
}

if (isset($_POST['submit'])) {

  // get data from the form
  $from_email = $_POST['fromemail']; // required
  $to_email = $_POST['toemail'];  // required
  $subject = $_POST['subject'];
  $body = $_POST['body'];  // required

  // check if input is empty
  if (empty($from_email) || empty($to_email) || empty($body)) {
    header("Location: ../index.php?status=empty");
    exit();
  } else {
    // check if input characters are valid
    if(!isValid($from_email, $to_email, $subject, $body)){
      header("Location: ../index.php?status=error");
      exit();
    } else {
      // send the mail
      if (sendMail($from_email, $to_email, $subject, $body)) {
        header("Location: ../index.php?status=success");
        exit();
      } else {
        header("Location: ../index.php?status=failed");
        exit();
      }
    }
  }
}

?>
