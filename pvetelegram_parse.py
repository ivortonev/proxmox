#!/usr/bin/python3

import os
import argparse
import subprocess

def processar_upid(upid):
    INPUT_STR = upid

    campos = upid.split(":")

    SUB_DIR = campos[4][-1]
    PVE_HOST = campos[1]
    TIPO = campos[5]
    USUARIO = campos[7]
    ARQ_CONF = campos[6]
    VM_NAME = f"/etc/pve/nodes/{PVE_HOST}/qemu-server/{ARQ_CONF}.conf"

    log_file = f"/var/log/pve/tasks/{SUB_DIR}/{INPUT_STR}"

    try:
        with open(log_file, 'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        log_content = "Arquivo de log não encontrado"

    try:
        with open(VM_NAME, 'r') as file:
          for linha in file:
              if linha.startswith("name"):
                LINHA_QVNAME = linha.strip()
                CAMPOS_QV = LINHA_QVNAME.split(":")
                QVNAME = CAMPOS_QV[1]
                QVNAME = QVNAME.strip()
    except FileNotFoundError:
        QVNAME = "Arquivo de configuração não encontrado"

    return {
        "INPUT_STR": INPUT_STR,
        "SUB_DIR": SUB_DIR,
        "ARQ_CONF": ARQ_CONF,
        "VM_NAME": VM_NAME,
        "USUARIO": USUARIO,
        "TIPO": TIPO,
        "LOG_CONTENT": log_content,
        "QVNAME": QVNAME,
        "PVE_HOST": PVE_HOST
    }

parser = argparse.ArgumentParser(description='String da task')
parser.add_argument('valor', type=str)
args = parser.parse_args()
upid = str(args.valor)

resultado = processar_upid(upid)

notify_string = "Host: " + resultado["PVE_HOST"] + "\\nNome da VM: " + resultado["QVNAME"] + "\\nUsuario: " + resultado["USUARIO"] + "\\nTipo de operacao: " + resultado["TIPO"]

print (notify_string)

subprocess.run(["/opt/pvetelegram/bin/pvetelegram_sendmsg.sh", notify_string])
