#!/bin/bash

crontab -l > ~/Projeto_4/mycron
echo "0 * * * * ~/Projeto_4/cron.sh" >> ~/Projeto_4/mycron

crontab ~/Projeto_4/mycron
rm mycron
echo feito
