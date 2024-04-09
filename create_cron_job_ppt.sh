#!/bin/bash

crontab -l > ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/mycron
echo "*/1 * * * * ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/cron.sh" >> ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/mycron

crontab ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/mycron
rm mycron
echo feito
