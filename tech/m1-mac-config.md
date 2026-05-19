---
created: 2026-05-19
tags: [tech, m1-mac, configuration, homebrew, php]
source: notes directory
---

# M1 Mac Configuration

Source: [Better Programming — 5 Crucial Developer Tweaks for New M1 Macs](https://betterprogramming.pub/5-crucial-developer-tweaks-for-new-m1-macs-a77c9990a985)

## Rosetta / Intel Compatibility

For running Intel (x86_64) Homebrew packages on M1:

```bash
# Show config for x86_64
arch -x86_64 brew config

# Install package for x86_64
arch -x86_64 brew install <pkg>
```

## PHP Configuration

### Enabling PHP in Apache

Add the following to `httpd.conf` and restart Apache:

```apache
LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

<FilesMatch \.php$>
    SetHandler application/x-httpd-php
</FilesMatch>
```

Finally, check DirectoryIndex includes index.php:

```apache
DirectoryIndex index.php index.html
```

### PHP Config File Locations

The `php.ini` and `php-fpm.ini` files can be found at:

```
/opt/homebrew/etc/php/8.1/
```

### Restarting PHP

To restart PHP after an upgrade:

```bash
# As a background service
brew services restart php

# Or run directly (no daemon)
/opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
```

## Homebrew Notes

- M1 Macs use ARM64 architecture by default
- Intel packages can be installed via Rosetta 2 translation
- Homebrew prefix on M1: `/opt/homebrew` (vs `/usr/local` on Intel)
