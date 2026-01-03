Write-Host "Buildando CheetahPy..." -ForegroundColor Green

pyinstaller app/main.py `
  --onefile `
  --windowed `
  --name CheetahPy `
  --add-data "app/assets/images/cheetahpy.png;assets/images" `
  --add-data "app/assets/icons/cheetahpy.ico;assets/icons" `
  --icon app/assets/icons/cheetahpy.ico `
  --clean

Write-Host "Build finalizado!" -ForegroundColor Green
