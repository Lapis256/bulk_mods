python gen.py > $null

New-Item -ItemType Directory -Path build -Force > $null
Compress-Archive -Path src/* -DestinationPath build/spam_mods.jar -CompressionLevel Optimal -Force > $null
