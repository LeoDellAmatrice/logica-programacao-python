Write-Host "Buildando CheetahPy..." -ForegroundColor Green

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
pip install pyinstaller

pyinstaller app/main.py `
  --onefile `
  --windowed `
  --name CheetahPy `
  --add-data "app/assets/;assets/" `
  --icon app/assets/icons/cheetahpy.ico `
  --clean

deactivate

Write-Host "Build finalizado!" -ForegroundColor Green
