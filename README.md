# Анализ макроэкономических данных

## Клонирование и запуск

```bash
git clone https://github.com/Ig0rek15/data_analysis
cd data_analysis

# установка зависимостей
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt

# запуск
python main.py --files data1.csv data2.csv --report average-gdp

# запуск тестов (покрытие 78%)
pytest
```

### Чтобы добавить новый отчёт:

- Создать новый класс отчёта в директории app/reports, унаследовавшись от BaseReport

- Реализовать методы generate и headers

- Зарегистрировать отчёт в app/reports/__init__.py

---

Примеры запуска можно посмотреть в results/
