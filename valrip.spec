# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['rip_validator/cli.py'],
    pathex=[],
    binaries=[],
    datas=[('rip_validator/extdata', 'rip_validator/extdata'), ('rip_validator/schemas', 'rip_validator/schemas')],
    hiddenimports=['rip_validator', 'rip_validator.cli', 'rip_validator.column_name_validator', 'rip_validator.config', 'rip_validator.data_and_metadata_validator', 'rip_validator.data_types', 'rip_validator.data_validator', 'rip_validator.filter_check', 'rip_validator.helper_validator_methods', 'rip_validator.metadata_validator', 'rip_validator.model_daml', 'rip_validator.model_waves_maml', 'rip_validator.status', 'rip_validator.validate'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='valrip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='x86_64',
    codesign_identity=None,
    entitlements_file=None,
)
