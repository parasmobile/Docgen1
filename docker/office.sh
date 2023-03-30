#!/bin/bash
/usr/bin/xvfb-run -a -s "-ac" libreoffice --display :99 --nologo --norestore --invisible  --accept='socket,host=localhost,port=2002;urp;StarOffice.ServiceManager'
