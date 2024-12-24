# nuntius!

Nuntius allows users to explore email spoofing concepts by sending emails from any email ID to any email ID using a simple web interface and backend PHP.

Update - 
Tunneling support for exposing localhost via Serveo.

<!-- <a href="https://github.com/shawsuraj/nuntius/releases">
    <img title="GitHub version" src="https://img.shields.io/badge/Version-v2.0.2-brightgreen" >
</a> -->


## Disclaimer
This project is for **educational and research purposes only**. The code demonstrates how email spoofing can occur and is intended to help developers and administrators improve email security. **Do not use this tool for illegal or malicious purposes.** 

The author takes no responsibility for any misuse of this code. Unauthorized use of this tool to send spoofed emails may violate local, national, or international laws. Use it only in systems where you have explicit permission.

Users are responsible for ensuring compliance with applicable laws in their jurisdiction, such as the CAN-SPAM Act, GDPR, and others.

## License
This project is licensed under the MIT License with additional clauses prohibiting malicious use. Please see the [LICENSE](LICENSE.md) file for details.

## Note

- The new tunneling features are untested due to server issues with Serveo, and alternative tunneling services like Localhost.run have been implemented.
- There is also uncertainty if the PHP email functionality works as intended or if it needs fixing.

# Installation

### Setup the web server
- Sign up for a free web hosting site (that offers php support).
- Upload all the contents of the server folder to your server.

### Configure to use CLI (optional)
- Install the requirements.
```bash
pip3 install requirements.txt
```

## Usage
### Web
- Open the url.
- Fill the form.
- Send.


## Upcoming features
- [ ] server hosting locally (ngrok/severno).
- [ ] Show status after sending emails.
- [ ] Automate the config process.
- [ ] Log the sent emails.
- [ ] Upload files directly via ftp.
- [ ] Configure to use multiple server via single CLI.
- [ ] GUI for windows and linux


## Author

**Suraj Shaw**
