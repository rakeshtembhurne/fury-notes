---
created: 2026-05-19
tags: [tech, bitnami, nodejs, setup, deployment]
source: notes directory
---

# Bitnami Node.js Setup

## Initial Server Setup

```bash
# Update system packages
sudo apt update --yes && sudo apt upgrade --yes

# Configure timezone
dpkg-reconfigure tzdata

# Clear screen
clear

# Check current directory
ll

# Edit and source bashrc
vim ~/.bashrc && source ~/.bashrc

# Verify files
ll

# Check Node installation
which node
node --version

# Navigate to stack
ll
cd stack/
ll

# Create projects directory
sudo mkdir /opt/bitnami/projects
sudo chown $USER /opt/bitnami/projects

# Go to projects
cd /opt/bitnami/projects/
ll

# Clone the repository
git clone https://github.com/rakeshtembhurne/trademybots.git
ll

# Navigate to project
cd trademybots/
ll

# Install dependencies
npm i

# Checkout develop branch
git checkout develop
npm i

# Check working directory
pwd
exit

ll
cd stack/projects/
ll
cd trademybots/
ll
npm run start
exit
```

## PM2 Setup

```bash
# Install PM2 globally
npm i -g pm2
sudo npm i -g pm2

# Navigate to project
cd stack/projects/trademybots/

# Start with PM2
pm2 start app.js

# Check status
pm2 status

# Exit
exit
```

## Apache Virtual Host Configuration

```bash
# Copy sample HTTP vhost
sudo cp /opt/bitnami/apache/conf/vhosts/sample-vhost.conf.disabled /opt/bitnami/apache/conf/vhosts/tmbweb-vhost.conf

# Edit HTTP vhost
sudo vim /opt/bitnami/apache/conf/vhosts/tmbweb-vhost.conf

# Copy sample HTTPS vhost
sudo cp /opt/bitnami/apache/conf/vhosts/sample-https-vhost.conf.disabled /opt/bitnami/apache/conf/vhosts/tmbweb-https-vhost.conf

# Edit HTTPS vhost
sudo vim /opt/bitnami/apache/conf/vhosts/tmbweb-https-vhost.conf

# Restart Apache
sudo ~/stack/ctlscript.sh restart apache
exit
```

## SSL Certificate Setup

```bash
# Run Bitnami certificate tool
sudo ~/stack/bncert-tool

# Show help
sudo ~/stack/bncert-tool --help

# Stop Apache
sudo /opt/bitnami/ctlscript.sh stop apache

# Remove old configs
sudo rm -rf /opt/bitnami/apache2/conf/trademybots.com*

# Run certificate tool
sudo ~/stack/bncert-tool

# Start Apache
sudo /opt/bitnami/ctlscript.sh start apache

# Run again with domains
sudo ~/stack/bncert-tool --domains trademybots.com
ll

cd stack/
ll
cd ..
history
history --help
history | cut -c 8-
```

## PM2 Process Management

```bash
# Check PM2 status
pm2 status

# List files
ll
ll stack
ll stack/

# Run certificate tool
sudo ~/stack/bncert-tool
ll

# Navigate to project
cd stack/projects/trademybots/
ll

# Edit environment file
vim .env

# Stop process 0
pm2 stop 0

# Start process 0
pm2 start 0
ll

# Edit environment file again
vim .env

# Delete process 0
pm2 delete 0

# Start again
pm2 start app.js
ll

# Show all files
la
ll

# Edit environment file
vim .env

# Navigate to config
cd config/
ll
vim appConfig.js
vim passport.js
cd ..

# Edit environment file again
vim .env
clear

# Git status
git status
exit
```

## Git Workflow

```bash
# Check git status
git status

# List files
ll

# Navigate to project
cd stack/projects/trademybots/

# Check branches
git branch

# Pull from develop
git pull origin develop

# Restart PM2
pm2 restart all
exit

# Navigate and pull
ll
cd stack/projects/trademybots/
ll
git branch
git pull origin develop
npm i
exit

# Restart specific process
pm2 status
pm2 restart 1
pm2 restart 0
exit
```

## View Command History

```bash
# Show full history
history

# Show help
history --help

# Show history without line numbers
history | cut -c 8-
```
