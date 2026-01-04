Write-Host "Instalando dependencias python..." -ForegroundColor Green

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
pip install pyinstaller

Write-Host "Buildando CheetahPy..." -ForegroundColor Green

pyinstaller app/main.py `
  --onefile `
  --windowed `
  --name CheetahPy `
  --add-data "app/assets/;assets/" `
  --icon app/assets/icons/cheetahpy.ico `
  --clean

deactivate

Write-Host "Build finalizado!" -ForegroundColor Green
