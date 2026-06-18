import subprocess
import sys


def run_command(command: list[str]) -> int:
    """Ejecuta un comando y retorna su código de salida."""
    print(f"-> Ejecutando: {' '.join(command)}")
 
    # Añade shell=True para que Windows ejecute el comando en su consola
    result = subprocess.run(command, shell=True) 
    #return result
    #result = subprocess.run(command)
    return result.returncode


def main() -> None:
    # 1. Ejecutar Ruff
    ruff_result = run_command(["ruff", "check", "."])
    #ruff_result = run_command([r"c:/Users/Administrador/Documents/documentos_phyton/venv/Scripts/ruff.exe", "check", "."])
    # 2. Ejecutar Mypy
    mypy_result = run_command(["mypy", "."])

    # Si algún comando falló, el script termina con error
    if ruff_result != 0 or mypy_result != 0:
        print("\n❌ Se encontraron errores en el código.")
        sys.exit(1)
    else:
        print("\n✨ ¡Todo el código pasa las pruebas de Ruff y Mypy!")


if __name__ == "__main__":
    main()