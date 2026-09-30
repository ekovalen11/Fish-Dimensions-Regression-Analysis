# Лабораторная работа №1. FishGrow: EDA

## 0. Паспорт воспроизводимости

| Параметр | Значение |
|---|---|
| URL исходного репозитория | https://github.com/tylerrussin/Fish-Dimensions-Regression-Analysis |
| URL форка (origin)        | https://github.com/ekovalen11/Fish-Dimensions-Regression-Analysis |
| Коммит (git rev-parse HEAD) | 1f65547b63c3043e2dcfff0c6435afa993331d4e |
| Дата клонирования | 2026-09-30 |
| Ветка | lab/01-eda |
| ОС | Ubuntu 24.04 |
| Python | 3.7.17 (pyenv, зафиксирован в .python-version) |
| pandas | 1.3.5 |
| numpy | 1.21.5 |
| dash | 2.1.0 |
| plotly | 5.6.0 |
| Команда запуска | `python run.py` |
| Результат запуска | приложение стартует, главная и /predict открываются в браузере |

## 1. Производственный контекст

Платформа FishGrow прогнозирует массу рыбы и контролирует качество
входных измерений. Целевая переменная — масса (Weight). Входные признаки —
геометрические измерения (длины, высота, ширина) и категория вида (Species).
Тестовая выборка остаётся закрытой до финальной проверки модели и на этапе
EDA не используется.

## 2. Отклонения от инструкции

Проблема: pipenv install --dev → "Python 3.7 was not found on your system".
Причина: в Pipfile зафиксирован python_version = "3.7"; в Ubuntu 24.04
         системный Python — 3.12, Python 3.7 отсутствует.
Решение: установлен pyenv и Python 3.7.17; в корне проекта создан
         .python-version (pyenv local 3.7.17); создано локальное venv
         через `python3.7 -m venv env`; pip откачен до <24.1;
         зависимости установлены из requirements.txt, полученного из
         Pipfile.lock.
Риск: версии транзитивных зависимостей могут отличаться от исходных;
      зафиксированы в reports/environment.txt.
### Форк репозитория (403 Forbidden при push)

При попытке выполнить `git push -u origin lab/01-eda` получена ошибка:

    remote: Permission to tylerrussin/Fish-Dimensions-Regression-Analysis.git
            denied to ekovalen11.
    fatal: «https://github.com/tylerrussin/Fish-Dimensions-Regression-Analysis/»
           недоступно: The requested URL returned error: 403

Причина: `origin` указывал на исходный репозиторий `tylerrussin`,
прав на запись в который у аккаунта `ekovalen11` нет. Это ожидаемое
поведение для чужого публичного репозитория.

Решение:
1. Репозиторий форкнут под аккаунтом `ekovalen11`:
   https://github.com/ekovalen11/Fish-Dimensions-Regression-Analysis
2. `origin` переключён на форк:
   `git remote set-url origin https://github.com/ekovalen11/...`
3. Добавлен дополнительный remote `upstream`, указывающий на исходный
   репозиторий, для возможной синхронизации:
   `git remote add upstream https://github.com/tylerrussin/...`
4. Push выполнен в форк: `git push -u origin lab/01-eda`.

Отклонение от инструкции: работа ведётся не в исходном репозитории,
а в форке. Это соответствует формату сдачи «запрос на слияние»:
PR будет открыт из ветки `lab/01-eda` форка в `main` исходного репозитория.

## Журнал решений

| Дата | Событие | Решение |
|---|---|---|
| 2026-09-30 | Клонирован репозиторий `tylerrussin/Fish-Dimensions-Regression-Analysis`, зафиксирован коммит `1f65547` | Создана ветка `lab/01-eda` |
| 2026-09-30 | `pipenv install --dev` → `Python 3.7 was not found on your system` | Установлен pyenv + Python 3.7.17, зафиксирован через `pyenv local 3.7.17` (.python-version) |
| 2026-09-30 | `pip install pipenv` → `error: externally-managed-environment` (PEP 668) | pipenv не используется; создано venv через `python3.7 -m venv env`, зависимости извлечены из Pipfile.lock в requirements.txt |
| 2026-09-30 | Порт 8050 занят при повторном запуске run.py | Процессы предыдущего запуска убиты (`kill <PID>`), приложение запущено заново |
| 2026-09-30 | `git commit` → `Author identity unknown` | Настроены `git config --global user.name/user.email` |
| 2026-09-30 | `git push` → `403 Forbidden` (Permission denied to ekovalen11) | Сделан форк под аккаунтом ekovalen11, origin переключён на форк, добавлен upstream |
| 2026-09-30 | Зафиксированы версии окружения (Python 3.7.17, pandas 1.3.5, numpy 1.21.5, dash 2.1.0, plotly 5.6.0) | Сохранены в `reports/environment.txt` |
| 2026-09-30 | Сделан коммит `81e6dea` «lab01: зафиксировано воспроизведение исходного проекта и окружение» | Ветка `lab/01-eda` запушена в форк |
