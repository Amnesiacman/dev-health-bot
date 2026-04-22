# dev-health-bot

`dev-health-bot` проверяет базовое "здоровье" репозитория и помогает быстро увидеть,
чего не хватает для нормального CI-ready процесса.

## Что проверяет v0.1

- наличие `.git`
- наличие `README.md`
- наличие `pyproject.toml`
- наличие директории `tests`
- наличие `.github/workflows/ci.yml`

## Установка и запуск

```bash
python3 -m pip install -e .
dev-health-bot --help
```

Локально без установки:

```bash
python3 main.py --help
```

## Примеры

Текстовый отчет:

```bash
python3 main.py --path .
```

JSON для CI/скриптов:

```bash
python3 main.py --path . --format json
```

Строгий режим (exit code 1, если есть проваленные проверки):

```bash
python3 main.py --path . --strict
```

## Exit codes

- `0`: отчет сформирован, в строгом режиме все проверки прошли
- `1`: только для `--strict`, если есть проваленные проверки

## GitHub Actions

- `ci.yml`: запускает тесты и smoke-проверку репозитория
- `release.yml`: создает GitHub Release при пуше тега `v*`
