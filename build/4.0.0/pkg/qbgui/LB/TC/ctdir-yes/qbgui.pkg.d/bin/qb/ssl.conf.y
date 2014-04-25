LoadModule ssl_module modules/mod_ssl.so
Listen 443
<VirtualHost _default_:443>
SSLEngine on
SSLCertificateFile /usr/local/apache/conf/server.crt 
SSLCertificateKeyFile /usr/local/apache/conf/server.key 
</VirtualHost>

Listen 9000
<VirtualHost *:9000>
SSLEngine on
SSLCertificateFile /usr/local/apache/conf/server.crt
SSLCertificateKeyFile /usr/local/apache/conf/server.key
DocumentRoot "/usr/local/apache/qb/auth/"
ErrorLog logs/error_log
</VirtualHost>

