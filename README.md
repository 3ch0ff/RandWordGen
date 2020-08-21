# Random Wordlist Generator

With this program you can make your randomic wordlist 

> only for linux operating system

## OS Requirements

 - python3
 - python3-pip
 - git

## How to install
### First Stage

Install OS Requirements with your operating system package manager

For **DEBIAN** distribution use:

```
sudo apt-get update && sudo apt-get full-upgrade --yes
sudo apt-get install python3 python3-pip git --yes
```

For **ARCH** distribution use:

```
sudo pacman -Syu
sudo pacman python3 git
```

For **FEDORA** distribution use:

```
sudo yum update
sudo yum install python3 python3-pip git
```

### Final Stage

```
git clone https://github.com/3ch0ff/RandWordGen.git
cd ./RandWordGen
python3 -m pip install -r requirements.txt
chmod +x randwordgen.py
python3 randwordgen.py
```

Your wordlist is in *output* directory 

**Thanks for use my program**
