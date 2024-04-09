#!/bin/bash

python ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/requisicao.py
python ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/selects.py
echo run_time: $(date +"%D_%T") >> ~/API Rest - Sistema de Monitoramento de Notícias sobre Criptomoeda/log.txt
