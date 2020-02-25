<?php
session_start();
if ($_POST['Submit'] == 'Send')
{
    $to = $_POST['toemail'];
    $subject = $_POST['subject'];
    $message = '<html><body>';
    $message .= $_POST['textarea'];
    $message .= "</body></html>";
    $fromemail = $_POST['fromemail'];
    $fromname = $_POST['fromname'];
    $lt= '<';
    $gt= '>';
    $sp= ' ';
    $from= 'From:';
    $headers .= 'From: '.$from."\r\n".
        'Reply-To: '.$from."\r\n" .
        'X-Mailer: PHP/' . phpversion();
    $headers = $from.$fromname.$sp.$lt.$fromemail.$gt;
    $headers .= "MIME-Version: $fromname\r\n";
    $headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
    mail($to,$subject,$message,$headers);
    header("Location: admin.php?msg= Great !Your EMail Sent -Click Back Button To Resend Mail Or Write New Mail");
    exit();
}
?>
