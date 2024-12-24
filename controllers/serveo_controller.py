import subprocess
import os
import signal

import pexpect

class ServeoController :
    def __init__(self, port) :
        self.port = port
        self.serveo_process = None
        self.public_url = None

    def start_php_server(self, php_directory) :
        self.php_server_process = subprocess.Popen(
            ["php", "-S", "localhost:{}".format(self.port), "-t", php_directory],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("PHP server started on localhost:{}".format(self.port))

    def start_serveo(self):
        try:
            # self.serveo_process = subprocess.Popen(
            #     ["ssh", "-R", "80:localhost:{}".format(self.port), "serveo.net"],
            #     stdout=subprocess.PIPE,
            #     stderr=subprocess.PIPE,
            #     text=True,
            # )

            # print("test-sC-start")
            # print (self.serveo_process.stdout)

            # for line in self.serveo_process.stdout:
            #     if "http://" in line or "https://" in line:
            #         self.public_url = line.strip()
            #         print("Serveo public URL: {}".format(self.public_url))
            #         break

            # Pexpect to capture the serveo url
            child = pexpect.spawn(
                f"ssh -R 80:localhost:{self.port} serveo.net", encoding="utf-8"
            )
            child.logfile = open("serveo.log", "w")  # Optional: Log for debugging

            # Look for the Serveo URL in the output
            while True:
                index = child.expect(["http://.*", "https://.*", pexpect.EOF, pexpect.TIMEOUT])
                if index in [0, 1]:  # Match for HTTP/HTTPS URL
                    self.public_url = child.match.group(0)
                    print("Serveo public URL: {}".format(self.public_url))
                    break
                elif index == pexpect.EOF:
                    print("Serveo process exited unexpectedly.")
                    break
                elif index == pexpect.TIMEOUT:
                    print("Timed out waiting for Serveo URL.")
                    break

        except Exception as e:
            print("Failed to start Serveo tunnel: {}".format(e))
            self.stop()

    def stop(self):
        if self.serveo_process:
            os.killpg(os.getpgid(self.serveo_process.pid), signal.SIGTERM)
            print("Serveo tunnel stopped.")
        if hasattr(self, "php_server_process") and self.php_server_process:
            self.php_server_process.terminate()
            print("PHP server stopped.")