#!/bin/bash
echo " libreoffice --display :99 --nologo --norestore --invisible  --accept='socket,host=localhost,port=2002;urp;StarOffice.ServiceManager'" > /tmp/aa
env >> /tmp/aa

libreoffice --display :99 --nologo --norestore --invisible  --accept=\'socket,host=localhost,port=2002\;urp\;StarOffice.ServiceManager\'
