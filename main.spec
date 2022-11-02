# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

exe_name = "爱妻助手2.0"
proj_path = "D:\\GitHub\\wife_helper\\"
icon_path =  proj_path+"src\\assets\\logo\logo.ico"

datas = [('src\\assets\\logo\\*', 'src\\assets\\logo\\'),
           ('src\\scripts\\*', 'src\\scripts\\')]

hidden_imports = ['win32com', 'pypinyin', 'openpyxl', 'xlwings']



a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon=icon_path,
)
