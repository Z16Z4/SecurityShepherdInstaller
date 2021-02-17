# Security Shepherd Installer

## General Info
This project is just a simple installer for Security Shepherd that gets it up and running easier for my software security class
### Original Documentation

https://github.com/OWASP/SecurityShepherd.git

### Setup for Running Installer
```
$sudo apt-get install python3 git -y

$git clone https://github.com/cronos-hash/SecurityShepherdInstaller.git

$cd SecurityShepherdInstaller

$python3 main.py

```


#### Stopping Security Shepherd
once security shepherd is installed run this command to stop  it
```
$cd SecurityShepherdInstaller
$docker-compose down
```

## Log-In Details:
once you gain access to security shepherd you will need to enable all the modules we use
```
username : admin
password: password
```

## Fixing possible errors
To fix this error ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
This error requires a reboot: use this command below:
```
sudo shutdown -r now
```
once the reboot occurs then run the script again using the command below
```
cd SecurityShepherdInstaller
python3 main.py




