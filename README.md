# nuntius!

Send email to anyone from anyone.

<a href="https://github.com/shawsuraj/nuntius/releases">
    <img title="GitHub version" src="https://img.shields.io/badge/Version-v2.0.0-brightgreen" >
</a>

# Installation

### Setup the web server
- Sign up for a free web hosting site (that offers php support).
- Upload all the contents of the server folder to your server.

### Configure to use CLI
- Edit the server_config.json file
- Change the False into True.
- Replace the "someurl" with your own url
```json
{
  "isConfigured" : "True",

  "url" : "https://test.com/",
  "ftp" : {
    "hose" : "hostname",
    "username" : "username",
    "password" : "password"
    }
  }
}
```
- Install the requirements.
```bash
pip3 install requirements.txt
```

## Usage
### Web
- Open the url.
- Fill the form.
- Send.

### CLI
```bash
$ python3 nuntius.py
```

## Upcoming features
- [ ] Automate the config process.
- [ ] Log the sent emails.
- [ ] Upload files directly via ftp.
- [ ] Configure to use multiple server via single CLI.


## Author

**Suraj Shaw**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
