# CSV tool

[![Build & Install Python Package](https://github.com/IlievIliya92/csv_tool/actions/workflows/python-build-install-pkg.yml/badge.svg)](https://github.com/IlievIliya92/csv_tool/actions/workflows/python-build-install-pkg.yml) [![Pylint](https://github.com/IlievIliya92/csv_tool/actions/workflows/pylint.yml/badge.svg)](https://github.com/IlievIliya92/csv_tool/actions/workflows/pylint.yml)

## Usage

```console
./csv_tool_app -i ./input_file.csv
```

## Build & install

```console
python setup.py build
python setup.py install
```

## Docker Image

```console
docker build -t csv_tool:1.0.0 .
docker run -it csv_tool:1.0.0
cd csv_tool
pytest tests
```