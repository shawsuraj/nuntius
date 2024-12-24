from controllers.ngrok_controller import NgrokController
from controllers.serveo_controller import ServeoController

def start_ngrok_server(port) :
    ngrok_controller = NgrokController(port)
    ngrok_controller.start_php_server()
    ngrok_controller.start_ngrok()

    print(ngrok_controller.public_url)

    return "{}/mail.php".format(ngrok_controller.public_url)

def start_serveo_server(port) :
    serveo_controller = ServeoController(port)
    serveo_controller.start_php_server("Server/www")
    # print("check st_se_srv")
    serveo_controller.start_serveo()
    # print("check st_se")


    print(serveo_controller.public_url)

    # if not serveo_controller.public_url:
    #     raise RuntimeError("Failed to retrieve Serveo public URL.") 
    
    return "{}/mail.php".format(serveo_controller.public_url)

