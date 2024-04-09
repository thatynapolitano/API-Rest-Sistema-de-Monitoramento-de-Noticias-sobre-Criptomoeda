#!/bin/bash

python ~/Projeto_4/requisicao.py
python ~/Projeto_4/selects.py
echo run_time: $(date +"%D_%T") >> ~/Projeto_4/log.txt
