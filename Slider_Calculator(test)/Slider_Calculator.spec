# -*- mode: python -*-

block_cipher = None


a = Analysis(['Slider_Calculator.py'],
             pathex=['D:\\Programing\\Git\\ljj\\Slider_Calculator(test)'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Slider_Calculator',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
