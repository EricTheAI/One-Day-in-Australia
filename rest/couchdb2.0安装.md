# [Team 2]
# Posung Chen / poc2 / 773278
# Xiao liang / liangx4 / 754282
# Jiawei Zhang / jiaweiz6 / 815546
# Jia Wang / jiaw8 / 815814
# Fan Hong / hongf / 795265

1. ```
   ## *** Ensure nodejs and npm are installed. These are used for Fauxton ***
   # Possibly update these

   # https://github.com/nodesource/distributions#debinstall
   curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -

   # This installs both npm and nodejs (node), and creates symbolic link from node to nodejs
   sudo apt-get install nodejs npm

   sudo apt-get update
   sudo apt-get -y install build-essential pkg-config erlang libicu-dev libmozjs185-dev libcurl4-openssl-dev rebar

   # Remove old files (assumed in /usr/local/src), if any
   cd /usr/local/src
   sudo rm -fR couchdb

   # get latest version of couchdb
   sudo git clone https://github.com/apache/couchdb.git
   sudo cd couchdb
   sudo ./configure --disable-docs

   sudo touch THANKS
   sudo touch /usr/lib/erlang/man/man1/x86_64-linux-gnu-gcov-tool.1.gz
   sudo touch /usr/lib/erlang/man/man1/gcov-tool.1.gz
   sudo make release
   # This takes a while, please be patient. This ends with text: 
   # "You can now copy the rel/couchdb directory anywhere on your system.
   #  Start CouchDB with ./bin/couchdb from within that directory."

   # *** user-registration-and-security ***
   sudo adduser --disabled-login --disabled-password --no-create-home --gecos "" couchdb

   # Copy the built couchdb release to /opt
   # Note: if you prefer another couchdb install location than /opt then that is fine, just adjust where relevant below
   sudo cp -R /usr/local/src/couchdb/rel/couchdb /opt
   sudo chown -R couchdb:couchdb /opt/couchdb

   # Change the permission of the CouchDB directories by running
   sudo find /opt/couchdb -type d -exec chmod 0770 {} \;

   # Update the permissions for your .ini files
   sudo chmod 0777 -R /opt/couchdb/

   # *** You can start the CouchDB server by running ***
   # Note: Ctrl-C to stop the couchdb
   # Warning: After a short trial run stop couchdb and ensure that couchdb runs as: user couchdb, when doing setup, whether single-node or cluster
   cd /opt/couchdb/bin
   ./couchdb

   # Try the installation
   #
   # Ubuntu server: use curl through another terminal window to the server: curl http://localhost:5984
   ```

   2. create couchdb2.0 in /bins

   ```bash
   !/bin/sh
   COUCHDB_BIN_DIR="/opt/couchdb/bin"
   ERTS_BIN_DIR=$COUCHDB_BIN_DIR/../
   cd "$COUCHDB_BIN_DIR/../"

   export ROOTDIR=${ERTS_BIN_DIR%/*}
   START_ERL=cat "$ROOTDIR/releases/start_erl.data"
   ERTS_VSN=${START_ERL% *}
   APP_VSN=${START_ERL#* }

   export BINDIR="ROOTDIR/erts-ERTS_VSN/bin"
   export EMU=beam
   export PROGNAME=echo $0 | sed 's/.*\///'
   exec "BINDIR/erlexec" -boot "ROOTDIR/releases/$APP_VSN/couchdb2" \
   	-args_file "$ROOTDIR/etc/vm.args" \
   -	config "$ROOTDIR/releases/$APP_VSN/sys.config" "$@"
   ```


## 3. Running as a Daemon

CouchDB no longer ships with any daemonization scripts.

The CouchDB team recommends [runit](http://smarden.org/runit/) torun CouchDB persistently and reliably. According to official site:

> *runit* is a cross-platform Unix init scheme with service supervision,a replacement for sysvinit, and other init schemes. It runs onGNU/Linux, *BSD, MacOSX, Solaris, and can easily be adapted toother Unix operating systems.

Configuration of runit is straightforward; if you have questions, contactthe CouchDB [user mailing list](http://mail-archives.apache.org/mod_mbox/couchdb-user/)or [IRC-channel #couchdb](http://webchat.freenode.net/?channels=#couchdb)in FreeNode network.

Let's consider configuring runit on Ubuntu 16.04. The followingsteps should be considered only as an example. Details will varyby operating system and distribution. Check your system's packagemanagement tools for specifics.

Install runit:

```
sudo apt-get install runit
```

Create a directory where logs will be written:

```
sudo mkdir /var/log/couchdb
sudo chown couchdb:couchdb /var/log/couchdb
```

Create directories that will contain runit configuration for CouchDB:

```linux
sudo mkdir /etc/sv/couchdb
sudo mkdir /etc/sv/couchdb/log
```

Create /etc/sv/couchdb/log/run script:

```
#!/bin/sh
exec svlogd -tt /var/log/couchdb
```

Basically it determines where and how exactly logs will be written.See `man svlogd` for more details.

Create /etc/sv/couchdb/run:

```
#!/bin/sh
export HOME=/opt/couchdb
exec 2>&1
exec chpst -u couchdb /opt/couchdb/bin/couchdb
```

This script determines how exactly CouchDB will be launched.Feel free to add any additional arguments and environment variables here if necessary.

Make scripts executable:

```
sudo chmod u+x /etc/sv/couchdb/log/run
sudo chmod u+x /etc/sv/couchdb/run
```

Then run:s

```
sudo ln -s /etc/sv/couchdb/ /etc/service/couchdb
```

In a few seconds runit will discover a new symlink and start CouchDB.You can control CouchDB service like this:

```
sudo sv status couchdb
sudo sv stop couchdb
sudo sv start couchdb
```

Naturally now CouchDB will start automatically shortly after system starts.

You can also configure systemd, launchd or SysV-init daemons to launchCouchDB and keep it running using standard configuration files. Consultyour system documentation for more information.

4. opt/couchdb/etc/local.ini

   ```
   ; CouchDB Configuration Settings

   ; Custom settings should be made in this file. They will override settings
   ; in default.ini, but unlike changes made to default.ini, this file won't be
   ; overwritten on server upgrade.

   [couchdb]
   ;max_document_size = 4294967296 ; bytes
   ;os_process_timeout = 5000
   max_dbs_open = 1024

   ; WARNING: use your own uuid number from the default local.ini (not this one!!!)
   uuid = 67d6a46cb75d63cf096c847628ea9ef7


   [couch_peruser]
   ; If enabled, couch_peruser ensures that a private per-user database
   ; exists for each document in _users. These databases are writable only
   ; by the corresponding user. Databases are in the following form:
   ; userdb-{hex encoded username}
   enable = true
   ; If set to true and a user is deleted, the respective database gets
   ; deleted as well.
   ;delete_dbs = true

   [chttpd]
   ; Single-node: use e.g. 5984
   ; Cluster: use e.g. 15984 for the first node, 25984 for the second node, 35984 for the third node
   port = 5984

   ; IMPORTANT: bind_address settings see: http://docs.couchdb.org/en/latest/config/http.html
   bind_address = 0.0.0.0
   socket_options = [{recbuf, 262144}, {sndbuf, 262144}, {nodelay, true}]

   [httpd]
   ; NOTE that this only configures the "backend" node-local port, not the
   ; "frontend" clustered port. You probably don't want to change anything in
   ; this section.
   ; Uncomment next line to trigger basic-auth popup on unauthorized requests.
   ; WWW-Authenticate = Basic realm="administrator"

   ; Uncomment next line to set the configuration modification whitelist. Only
   ; whitelisted values may be changed via the /_config URLs. To allow the admin
   ; to change this value over HTTP, remember to include {httpd,config_whitelist}
   ; itself. Excluding it from the list would require editing this file to update
   ; the whitelist.
   ;config_whitelist = [{httpd,config_whitelist}, {log,level}, {etc,etc}]

   server_options = [{backlog, 128}, {acceptor_pool_size, 16}]
   socket_options = [{recbuf, 262144}, {sndbuf, 262144}, {nodelay, true}]
   enable_cors = true

   ; 3 minutes = 3 * 60 * 1000 = 180000
   changes_timeout = 180000

   x_forwarded_host = X-Forwarded-Host
   x_forwarded_proto = X-Forwarded-Proto
   x_forwarded_ssl = X-Forwarded-Ssl

   ;Note that writer = stderr fits (seems to) with the systemd startup script described in the couchdb installation part in this documentation
   ;[log]
   ;level = debug
   writer = stderr
   level = warning

   [query_servers]
   ;nodejs = /usr/local/bin/couchjs-node /path/to/couchdb/share/server/main.js

   [httpd_global_handlers]
   ;_google = {couch_httpd_proxy, handle_proxy_req, <<"http://www.google.com">>}

   [couch_httpd_auth]
   ; If you set this to true, you should also uncomment the WWW-Authenticate line
   ; above. If you don't configure a WWW-Authenticate header, CouchDB will send
   ; Basic realm="server" in order to prevent you getting logged out.
   ; require_valid_user = true

   ; WARNING: use your own secret number from the default local.ini (not this one!!!)
   ;secret = f52f991eb7dd2033544cd8a9cc9e58e1
   ;allow_persistent_cookies = true

   ; 14 days = 14 * 24 * 60 * 60 = 1209600 seconds
   ; timeout = 1209600
   ; auth_cache_size = 1000

   [os_daemons]
   ; For any commands listed here, CouchDB will attempt to ensure that
   ; the process remains alive. Daemons should monitor their environment
   ; to know when to exit. This can most easily be accomplished by exiting
   ; when stdin is closed.
   ;foo = /path/to/command -with args

   [daemons]
   ; enable SSL support by uncommenting the following line and supply the PEM's below.
   ; the default ssl port CouchDB listens on is 6984
   ; httpsd = {chttpd, start_link, [https]}

   [ssl]
   ;cert_file = /full/path/to/server_cert.pem
   ;key_file = /full/path/to/server_key.pem
   ;password = somepassword
   ; set to true to validate peer certificates
   ;verify_ssl_certificates = false
   ; Set to true to fail if the client does not send a certificate. Only used if verify_ssl_certificates is true.
   ;fail_if_no_peer_cert = false
   ; Path to file containing PEM encoded CA certificates (trusted
   ; certificates used for verifying a peer certificate). May be omitted if
   ; you do not want to verify the peer.
   ;cacert_file = /full/path/to/cacertf
   ; The verification fun (optional) if not specified, the default
   ; verification fun will be used.
   ;verify_fun = {Module, VerifyFun}
   ; maximum peer certificate depth
   ;ssl_certificate_max_depth = 1
   ;
   ; Reject renegotiations that do not live up to RFC 5746.
   ;secure_renegotiate = true
   ; The cipher suites that should be supported.
   ; Can be specified in erlang format "{ecdhe_ecdsa,aes_128_cbc,sha256}"
   ; or in OpenSSL format "ECDHE-ECDSA-AES128-SHA256".
   ;ciphers = ["ECDHE-ECDSA-AES128-SHA256", "ECDHE-ECDSA-AES128-SHA"]
   ; The SSL/TLS versions to support
   ;tls_versions = [tlsv1, 'tlsv1.1', 'tlsv1.2']

   ; To enable Virtual Hosts in CouchDB, add a vhost = path directive. All requests to
   ; the Virual Host will be redirected to the path. In the example below all requests
   ; to http://example.com/ are redirected to /database.
   ; If you run CouchDB on a specific port, include the port number in the vhost:
   ; example.com:5984 = /database
   [vhosts]
   ;example.com = /database/

   [update_notification]
   ;unique notifier name=/full/path/to/exe -with "cmd line arg"

   ; To create an admin account uncomment the '[admins]' section below and add a
   ; line in the format 'username = password'. When you next start CouchDB, it
   ; will change the password to a hash (so that your passwords don't linger
   ; around in plain-text files). You can add more admin accounts with more
   ; 'username = password' lines. Don't forget to restart CouchDB after
   ; changing this.
   [admins]
   ; WARNING: UPDATE THIS!!!
   ; Cluster: use the same admin user and password on all Cluster nodes
   admin = admin

   [replicator]
   ; adjust this to your situation
   ; 3 minutes = 3 * 60 * 1000 = 180000
   connection_timeout = 180000
   use_checkpoints = true
   worker_batch_size = 2000

   [compactions]
   _default =  [{db_fragmentation,"70%"},{view_fragmentation,"60%"},{from,"00:00"},{to,"06:00"}]

   [cors]
   ; See also https://github.com/pouchdb/add-cors-to-couchdb
   ; Note: the Fauxton cors settings are slightly different
   origins = *
   credentials = true
   headers = accept, authorization, content-type, origin, cookie, referer, x-csrf-token
   methods = GET, OPTIONS, HEAD, PUT, POST, DELETE, TRACE

   ```