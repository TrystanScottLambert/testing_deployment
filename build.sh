#!/bin/bash
set -e

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist
mkdir -p dist

echo "Building macOS ARM64 binary (Apple Silicon)..."
source .venv-universal/bin/activate
pyinstaller \
  --onefile \
  --target-arch arm64 \
  --name valrip \
  --add-data "rip_validator/extdata:rip_validator/extdata" \
  --add-data "rip_validator/schemas:rip_validator/schemas" \
  --hidden-import rip_validator \
  --hidden-import rip_validator.cli \
  --hidden-import rip_validator.column_name_validator \
  --hidden-import rip_validator.config \
  --hidden-import rip_validator.data_and_metadata_validator \
  --hidden-import rip_validator.data_types \
  --hidden-import rip_validator.data_validator \
  --hidden-import rip_validator.filter_check \
  --hidden-import rip_validator.helper_validator_methods \
  --hidden-import rip_validator.metadata_validator \
  --hidden-import rip_validator.model_daml \
  --hidden-import rip_validator.model_waves_maml \
  --hidden-import rip_validator.status \
  --hidden-import rip_validator.validate \
  rip_validator/cli.py
mv dist/valrip dist/valrip-macos-arm64
rm -rf build # Clean build folder between architectures

echo "Building macOS x86_64 binary (Intel)..."
pyinstaller \
  --onefile \
  --target-arch x86_64 \
  --name valrip \
  --add-data "rip_validator/extdata:rip_validator/extdata" \
  --add-data "rip_validator/schemas:rip_validator/schemas" \
  --hidden-import rip_validator \
  --hidden-import rip_validator.cli \
  --hidden-import rip_validator.column_name_validator \
  --hidden-import rip_validator.config \
  --hidden-import rip_validator.data_and_metadata_validator \
  --hidden-import rip_validator.data_types \
  --hidden-import rip_validator.data_validator \
  --hidden-import rip_validator.filter_check \
  --hidden-import rip_validator.helper_validator_methods \
  --hidden-import rip_validator.metadata_validator \
  --hidden-import rip_validator.model_daml \
  --hidden-import rip_validator.model_waves_maml \
  --hidden-import rip_validator.status \
  --hidden-import rip_validator.validate \
  rip_validator/cli.py
mv dist/valrip dist/valrip-macos-x86_64

deactivate
source .venv/bin/activate

echo "Building Linux AMD64 binary..."
docker run --rm --platform linux/amd64 -v "$(pwd):/src" python:3.12 bash -c "
  cd /src && \
  pip install pyinstaller && \
  pip install -r requirements.txt && \
  pip install -e . && \
  pyinstaller valrip.spec
"
mv dist/valrip dist/valrip-linux-amd64

echo "Building Linux ARM64 binary..."
docker run --rm --platform linux/arm64 -v "$(pwd):/src" python:3.12 bash -c "
  cd /src && \
  pip install pyinstaller && \
  pip install -r requirements.txt && \
  pip install -e . && \
  pyinstaller valrip.spec
"
mv dist/valrip dist/valrip-linux-arm64

echo ""
echo "✓ Build complete! Binaries:"
ls -lh dist/
