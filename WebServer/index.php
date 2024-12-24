<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <title>NUNTIUS!</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>

<body>
    <canvas id="matrix-bg"></canvas>

    <div class="status empty">
        <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
        <p><strong>Empty!</strong> Please fill all the fields.</p>
    </div>
    <div class="status error">
        <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
        <p><strong>Error!</strong> Please enter correct information..</p>
    </div>
    <div class="status success">
        <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
        <p><strong>Success!</strong> Mail sent successfully. Support the repository <a class="link" href="https://github.com/shawsuraj/nuntius">here</a></p>
    </div>
    <div class="status failed">
        <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
        <p><strong>Failed!</strong> Error occured while sendin, please report the issue <a class="link" href="https://github.com/shawsuraj/nuntius/issues/new?assignees=&labels=&template=bug_report.md&title=">here</a>.</p>
    </div>


    <h1 id="heading">NUNTIUS!</h1>

    

    <form method="post" id="sendmail" action = "/php/mail.php">
        <div class="container">
            <label>From: </label>
            <input type="email" name="fromemail">
            <br>
            <label>To: </label>
            <input type="email" name="toemail">
            <br>
            <label>Subject: </label>
            <input type="text" name="subject">
            <br>
            <label>Body: </label>
            <textarea rows="8" name="body"></textarea>
            <br>
            <button name="submit" type="submit" value="Send Email">Submit</button>
            <span id="success_msg"></span>
            <span id="error_msg"></span>
        </div>
    </form>



    <script src="js/jquery-3.4.1.min.js"></script>

    <!--Source : https://codepen.io/wefiy/pen/WPpEwo-->
    <script src="js/matrix.js"></script>

    <?php
        $fullurl = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI] ";

        if (strpos($fullurl, "status=empty") == true) {
            echo "<script type='text/javascript'> $( 'div' ).remove( '.error' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.success' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.failed' );  </script>";
            
        }
        elseif (strpos($fullurl, "status=error") == true) {
            echo "<script type='text/javascript'> $( 'div' ).remove( '.empty' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.success' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.failed' );  </script>";
        }
        elseif (strpos($fullurl, "status=success") == true) {
            echo "<script type='text/javascript'> $( 'div' ).remove( '.empty' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.error' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.failed' );  </script>";
        }
        elseif (strpos($fullurl, "status=failed") == true) {
            echo "<script type='text/javascript'> $( 'div' ).remove( '.empty' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.error' );  </script>";
            echo "<script type='text/javascript'> $( 'div' ).remove( '.success' );  </script>";
        }
    ?>

</body></html>
