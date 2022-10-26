# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

ROOT_DIR = 'c:\\***\\***\\'

a = Analysis(['main.py', ROOT_DIR+'src/app.py', ROOT_DIR+'src/views/home_view.py'],
             pathex=[],
             binaries=[],
             datas=[(ROOT_DIR+'src', 'src')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False ,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='爱妻助手2.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
app = BUNDLE(exe,
             name='main.app',
             icon=None,
             bundle_identifier=None)