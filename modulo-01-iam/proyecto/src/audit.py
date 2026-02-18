"""
iam-user-audit
Auditoría de seguridad IAM para AWS Certified Developer Associate
Módulo 01 — IAM

Uso:
    python audit.py
    python audit.py --output reporte.json
"""

import boto3
import json
import argparse
from datetime import datetime, timezone, timedelta
from tabulate import tabulate

from iam_checker import IamChecker
from reporter import Reporter


def main():
    parser = argparse.ArgumentParser(description='Auditoría de seguridad IAM')
    parser.add_argument('--output', help='Archivo de salida JSON (opcional)')
    args = parser.parse_args()

    print("\n=== AWS IAM Security Audit ===")

    # Obtener información de la cuenta
    sts = boto3.client('sts')
    identity = sts.get_caller_identity()
    account_id = identity['Account']
    print(f"Cuenta: {account_id}")
    print(f"Fecha:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Ejecutar verificaciones
    checker = IamChecker()
    results = checker.run_all_checks()

    # Mostrar resultados en consola
    reporter = Reporter(results, account_id)
    reporter.print_summary()

    # Guardar en archivo si se especificó
    if args.output:
        reporter.save_json(args.output)
        print(f"\nReporte guardado en: {args.output}")


if __name__ == '__main__':
    main()
