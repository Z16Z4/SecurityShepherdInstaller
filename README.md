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

## Stopping Security Shepherd
```
$cd SecurityShepherdInstaller
$docker-compose down
```

## Log-In Details:
```
username : admin
password: password
```

## Fixing possible errors
your machine may need to be restarted because docker installed, run this command below:
```
sudo shutdown -r now
```



