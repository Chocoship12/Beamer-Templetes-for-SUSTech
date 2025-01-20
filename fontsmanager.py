from matplotlib import font_manager

for font in font_manager.findSystemFonts(fontpaths=None, fontext='ttf'):
    print(font)
