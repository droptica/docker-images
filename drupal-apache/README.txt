Set up custom document root. Usefull especially when you have a vendor dir outside of your web root. 
You would then map the whole dir into docker (including the vendor) and specify a DOCUMENT_ROOT for the vhost configuration.

ENV DOCUMENT_ROOT /var/www/html/mycustomdir

