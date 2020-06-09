# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Chris\\Documents\\SupremeBot\\app'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='supremeapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe, Tree('C:\\Users\\Chris\\Documents\\SupremeBot\\app\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='SupremeApp')
