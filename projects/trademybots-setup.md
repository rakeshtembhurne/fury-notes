---
created: 2026-05-19
tags: [projects, trademybots, deployment, devops, bitnami]
source: notes directory
---

# TradeMyBots Setup — Bitnami Deployment

> This file documents the deployment process for TradeMyBots project on Bitnami stack.

## System Setup Commands

```bash
# Update OS
sudo apt update --yes && sudo apt upgrade --yes

# Configure timezone
dpkg-reconfigure tzdata

# Enable bash aliases
sed -i '/alias dir=/s/^#//g' ~/.bashrc
sed -i '/alias grep=/s/^#//g' ~/.bashrc
sed -i '/alias fgrep=/s/^#//g' ~/.bashrc
sed -i '/alias egrep=/s/^#//g' ~/.bashrc
sed -i '/alias ll=/s/^#//g' ~/.bashrc
sed -i '/alias la=/s/^#//g' ~/.bashrc
sed -i '/alias l=/s/^#//g' ~/.bashrc
source ~/.bashrc
```

## Project Installation

```bash
# Clone the project
sudo mkdir /opt/bitnami/projects
sudo chown $USER /opt/bitnami/projects
cd /opt/bitnami/projects/
git clone https://rakeshtembhurne@github.com/rakeshtembhurne/trademybots.git
cd trademybots/
git checkout develop
npm install
```

## PM2 Process Manager

```bash
# Install PM2 globally
sudo npm install --global pm2

# Start the application
pm2 start /opt/bitnami/projects/trademybots/app.js

# Check status
pm2 status

# Restart all processes
pm2 restart all

# Stop specific process
pm2 stop 0

# Delete process
pm2 delete 0
```

## Apache Virtual Host Configuration

### HTTP Virtual Host
```apache
<VirtualHost 127.0.0.1:80 _default_:80>
  ServerName trademybots.com
  ServerAlias *
  DocumentRoot /opt/bitnami/projects/trademybots
  <Directory "/opt/bitnami/projects/trademybots">
    Options -Indexes +FollowSymLinks -MultiViews
    AllowOverride All
    Require all granted
  </Directory>
  ProxyPass / http://localhost:8080/
  ProxyPassReverse / http://localhost:8080/
</VirtualHost>
```

### HTTPS Virtual Host
```apache
<VirtualHost 127.0.0.1:443 _default_:443>
  ServerName trademybots.com
  ServerAlias *
  SSLEngine on
  SSLCertificateFile "/opt/bitnami/apache/conf/bitnami/certs/server.crt"
  SSLCertificateKeyFile "/opt/bitnami/apache/conf/bitnami/certs/server.key"
  DocumentRoot /opt/bitnami/projects/trademybots
  <Directory "/opt/bitnami/projects/trademybots">
    Options -Indexes +FollowSymLinks -MultiViews
    AllowOverride All
    Require all granted
  </Directory>
  ProxyPass / http://localhost:8080/
  ProxyPassReverse / http://localhost:8080/
</VirtualHost>
```

## SSL Certificate Setup with Let's Encrypt (Lego)

```bash
# Install Lego
cd /tmp
curl -Ls https://api.github.com/repos/xenolf/lego/releases/latest | grep browser_download_url | grep linux_amd64 | cut -d '"' -f 4 | wget -i -
tar xf lego_v*.tar.gz
sudo mkdir -p /opt/bitnami/letsencrypt
sudo mv lego /opt/bitnami/letsencrypt/lego

# Obtain SSL Certificate
sudo /opt/bitnami/ctlscript.sh stop
sudo /opt/bitnami/letsencrypt/lego --tls --email="tj2point0@gmail.com" --domains="trademybots.com" --domains="www.trademybots.com" --path="/opt/bitnami/letsencrypt" run
sudo /opt/bitnami/ctlscript.sh start

# Move Certificates
sudo mv /opt/bitnami/apache2/conf/bitnami/certs/server.crt /opt/bitnami/apache2/conf/bitnami/certs/server.crt.old
sudo mv /opt/bitnami/apache2/conf/bitnami/certs/server.key /opt/bitnami/apache2/conf/bitnami/certs/server.key.old
sudo ln -sf /opt/bitnami/letsencrypt/certificates/trademybots.com.key /opt/bitnami/apache2/conf/bitnami/certs/server.key
sudo ln -sf /opt/bitnami/letsencrypt/certificates/trademybots.com.crt /opt/bitnami/apache2/conf/bitnami/certs/server.crt
sudo chown root:root /opt/bitnami/apache2/conf/bitnami/certs/server*
sudo chmod 600 /opt/bitnami/apache2/conf/bitnami/certs/server*
```

## Certificate Renewal Script

```bash
sudo mkdir -p /opt/bitnami/letsencrypt/scripts

# Create renewal script
sudo cat > /opt/bitnami/letsencrypt/scripts/renew-certificate.sh << 'EOF'
#!/bin/bash
sudo /opt/bitnami/ctlscript.sh stop
sudo /opt/bitnami/letsencrypt/lego --tls --email="tj2point0@gmail.com" --domains="trademybots.com" --domains="www.trademybots.com" --path="/opt/bitnami/letsencrypt" renew --days 90
sudo /opt/bitnami/ctlscript.sh start
EOF

sudo chmod +x /opt/bitnami/letsencrypt/scripts/renew-certificate.sh
```

## Crontab Setup for Auto-Renewal

```bash
# Add to crontab (runs monthly)
(crontab -l ; echo "0 0 1 * * /opt/bitnami/letsencrypt/scripts/renew-certificate.sh 2> /dev/null") | crontab -
```

## Bitnami Control Script Commands

```bash
# Restart Apache
sudo /opt/bitnami/ctlscript.sh restart apache

# Full restart
sudo /opt/bitnami/ctlscript.sh restart

# Stop services
sudo /opt/bitnami/ctlscript.sh stop

# Start services
sudo /opt/bitnami/ctlscript.sh start

# Run SSL certificate tool
sudo ~/stack/bncert-tool
```

## Git Deployment Workflow

```bash
# Pull latest changes
cd /opt/bitnami/projects/trademybots/
git branch
git pull origin develop
npm i

# Restart PM2
pm2 restart all
```

## Environment Configuration

The `.env` file is stored at `/opt/bitnami/projects/trademybots/.env` and contains:
- MongoDB URI
- Session secret
- OAuth credentials (Google, GitHub, Facebook, LinkedIn, etc.)
- API keys (Stripe, Twilio, Mailgun, SendGrid, etc.)
- Social media credentials (Instagram, Snapchat, Twitter, etc.)

## File Locations

| Path | Description |
|------|-------------|
| `/opt/bitnami/projects/trademybots/` | Project root |
| `/opt/bitnami/apache/conf/vhosts/` | Apache virtual host configs |
| `/opt/bitnami/letsencrypt/` | Let's Encrypt certificates |
| `/opt/bitnami/letsencrypt/scripts/` | Certificate renewal scripts |
| `~/.pm2/logs/` | PM2 logs |

---

> Related: [[trademybots-playbook]] · [[dev-tech-learnings]] · [[n8n-infrastructure-deployment]] · [[aws-ec2-docker-n8n-free-hosting]]
