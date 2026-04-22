# dev-health-bot

[English version](README.md)

CLI-утилита для быстрой оценки готовности репозитория к нормальному процессу разработки.

## Что проверяет

- наличие `.git`
- наличие `README.md`
- наличие `pyproject.toml`
- наличие `tests/`
- наличие `.github/workflows/ci.yml`

## Использование

```bash
python3 main.py --path .
python3 main.py --path . --format json
python3 main.py --path . --strict
```

## Использование в CI

Строгий режим помогает заваливать пайплайн, если в репозитории не хватает базовых обязательных элементов.

## Коды возврата

- `0` скан завершён (и strict-проверка пройдена)
- `1` strict-режим не пройден
