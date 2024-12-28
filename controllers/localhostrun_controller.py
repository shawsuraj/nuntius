import subprocess
import time

class LocalhostRunController :
    def __init__(self, port):
        self.port = port
        self.localhost_run_process = None
        self.public_url = None

    def start_php_server(self, php_directory) :
        try :
            self.php_server_process = subprocess.Popen(
            ["php", "-S", "localhost:{}".format(self.port), "-t", php_directory],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            )
            
            print("PHP server started on localhost:{}".format(self.port))

        except Exception as e :
            print("Failed to start PHP server : {}".format(e)) 

    def start_localhost_run(self) :
        try :
            # SSH to establish connection localhost.run
            self.localhost_run_process = subprocess.Popen(
                [
                    "ssh",
                    "-o",
                    "StrictHostKeyChecking=no",
                    "-o",
                    "ServerAliveInterval=60",
                    "-R",
                    "80:localhost:{0}".format(self.port),
                    "nokey@localhost.run"
                 ],
                stdout = open('localhostrun.log','w'),  # Capture output to a file
                stdin = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL, 
                start_new_session = True
            )

            print ("Waiting for 10 seconds for the server to start...") 
            time.sleep(10)

            # Reading and extracting the URL from the output
            lines = subprocess.check_output(['cat', 'localhostrun.log']).decode().split("\n")
            for line in lines:
                if "http://" in line or "https://" in line:
                    self.public_url = "https://" + line.split(' ',1)[0]
                    print("localhost.run public URL: {}".format(self.public_url))
                    break

            # print(self.public_url)

        except Exception as e :
            print("Failed to start localhost.run tunner: {}".format(e))