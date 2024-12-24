import subprocess
from pyngrok import ngrok

class NgrokController :
    def __init__(self, port) :
        self.port = port
        self.php_directory = "Server/www"
        self.php_server = None
        self.public_url = None

    def start_php_server(self) :
        try :
            print(self.port)
            self.php_server = subprocess.Popen(["php", "-S", "localhost:{}".format(self.port), "-t", self.php_directory])
            print("Localhost php server is started on https://localhost:{}".format(self.port))
        
        except Exception as e :
            print("Failed to start PHP server : {}".format(e))
        
    def start_ngrok(self) :
        try :
            self.public_url = ngrok.connect(self.port)
        
        except Exception as e :
            print ("Failed to start ngrok tunner {}".format(e))

    def stop(self) :
        if self.php_server :
            self.php_server.terminate()
        ngrok.kill()
