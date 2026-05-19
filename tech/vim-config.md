---
created: 2026-05-19
tags: [tech, vim, editor, configuration, cheatsheet]
source: notes directory
---

# Vim Configuration and Commands

## Vim Motion & Editing Basics

### Verbs (Actions)
- **d** — Delete
- **c** — Change
- **>** — Indent
- **v** — Visually select
- **y** — Yank (copy)

### Common Motions
- **w** — word (forward by a word)
- **b** — back (back by a word)
- **j** — down a line
- **k** — up a line
- **2j** — down 2 lines

### Text Objects
- **iw** — "inner word" (anywhere from a word)
- **it** — "inner tag" (the contents of HTML tag)
- **i"** — "inner quotes"
- **ip** — "inner paragraph"
- **as** — "a sentence"

### Parameterized Text Objects
- **f,F** — "find" the next character (Capital F finds backwards)
- **t,T** — "find" the next character (up to but not including that character) (Capital T finds backwards)
- **/** — Search up to the next match
- **/?** — Search in reverse direction

### Useful Combinations
- **cw** — deletes the word and puts in insert mode
- **dw** — deletes the word
- **cf'** — change find single quote (deletes till first single quote and goes to insert mode)
- **.** — repeat last action
- **u** — undo

## Vim Configuration for Node.js Development

Source: [The Self Hosting Blog — Configuring Vim for Node.js Development](https://theselfhostingblog.com/posts/configuring-vim-for-node-js-development/)

## Bitnami Node.js Setup

### Initial Server Setup
```bash
# Update system
sudo apt update --yes && sudo apt upgrade --yes

# Configure timezone
dpkg-reconfigure tzdata

# Edit bashrc and reload
vim ~/.bashrc && source ~/.bashrc

# Check Node installation
which node
node --version
```

### Project Setup on Bitnami
```bash
# Create projects directory
sudo mkdir /opt/bitnami/projects
sudo chown $USER /opt/bitnami/projects

# Clone project
cd /opt/bitnami/projects/
git clone https://github.com/rakeshtembhurne/trademybots.git
cd trademybots/
git checkout develop
npm install
```

### PM2 Process Management
```bash
# Install PM2 globally
npm i -g pm2
sudo npm i -g pm2

# Start application
pm2 start app.js

# Check status
pm2 status

# Restart all
pm2 restart all

# Stop and delete
pm2 stop 0
pm2 delete 0
pm2 start app.js
```

### Virtual Host Configuration
```bash
# Copy sample configs
sudo cp /opt/bitnami/apache/conf/vhosts/sample-vhost.conf.disabled /opt/bitnami/apache/conf/vhosts/tmbweb-vhost.conf
sudo cp /opt/bitnami/apache/conf/vhosts/sample-https-vhost.conf.disabled /opt/bitnami/apache/conf/vhosts/tmbweb-https-vhost.conf

# Edit virtual hosts
sudo vim /opt/bitnami/apache/conf/vhosts/tmbweb-vhost.conf
sudo vim /opt/bitnami/apache/conf/vhosts/tmbweb-https-vhost.conf

# Restart Apache
sudo ~/stack/ctlscript.sh restart apache
```

### SSL Certificate with Bitnami
```bash
# Run Bitnami SSL certificate tool
sudo ~/stack/bncert-tool

# Stop Apache before SSL setup
sudo /opt/bitnami/ctlscript.sh stop apache

# Remove old configs
sudo rm -rf /opt/bitnami/apache2/conf/trademybots.com*

# Run certificate tool again
sudo /opt/bitnami/ctlscript.sh start apache
sudo ~/stack/bncert-tool
sudo ~/stack/bncert-tool --domains trademybots.com
```

### Git Workflow
```bash
# Check status
git status

# Pull latest
git pull origin develop

# Restart after pull
pm2 restart all
```

### View Command History
```bash
history
history --help
history | cut -c 8-
```
