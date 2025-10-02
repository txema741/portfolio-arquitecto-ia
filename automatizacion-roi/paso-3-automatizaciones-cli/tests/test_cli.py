"""
Test básico para el CLI Launcher de Paso 3.
Comprueba que los subcomandos existen y que el script no lanza errores de sintaxis.
"""

import subprocess
import pytest

def test_cli_help():
    """Verifica que el CLI muestra ayuda"""
    result = subprocess.run(
        ["python", "automatizacionRoi/paso-3-automatizaciones-cli/scripts/cli_launcher.py", "--help"],
        capture_output=True,
        text=True
    )
    assert "ROI" in result.stdout or "CoPQ" in result.stdout

def test_cli_roi_params():
    """Verifica que se requiere input en ROI"""
    result = subprocess.run(
        ["python", "automatizacionRoi/paso-3-automatizaciones-cli/scripts/cli_launcher.py", "roi"],
        capture_output=True,
        text=True
    )
    assert "the following arguments are required" in result.stderr
