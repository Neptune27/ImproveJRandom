# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata

datas = []
datas += copy_metadata('pyppeteer')


block_cipher = None


a = Analysis(['kanjiBrowserGUI.py'],
             pathex=['D:\\PycharmProjects\\ImproveJRandom'],
             binaries=[],
             datas=datas,
             hiddenimports=['pynput.keyboard._win32', 'pynput.mouse._win32'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='kanjiBrowserGUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='kanjiBrowserGUI')
