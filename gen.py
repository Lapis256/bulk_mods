num = 65536 - 2 # Forge and Minecraft

text = f"""
modLoader = "lowcodefml"
loaderVersion = "[47,)"
license = "CC0"

mods = [ {", ".join([f'{{ modId = "spam_mods_{i}" }}' for i in range(num)])} ]
""".lstrip()

with open("src/META-INF/mods.toml", "w", encoding="utf-8") as f:
    f.write(text)
