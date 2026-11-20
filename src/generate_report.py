import pandas as pd
from pathlib import Path

def generate_html_report():
    data_path = Path("../assets/data/Fish.csv")
    df = pd.read_csv(data_path)
    
    html = df.describe().to_html()
    
    report_path = Path("../reports/auto_report.html")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>Auto Report</title></head><body>")
        f.write("<h1>Автоматический отчет по данным (Доп. задание)</h1>")
        f.write(html)
        f.write("</body></html>")
    print(f"Отчет сохранен в {report_path}")

def test_data_ranges():
    df = pd.read_csv("../assets/data/Fish.csv")
    max_length = df['Length1'].max()
    if max_length > 100:
        raise ValueError(f"ОШИБКА: Длина (Length1) = {max_length}. Похоже, единицы измерения изменены с см на мм!")
    
    if (df[['Weight', 'Length1']] < 0).any().any():
        raise ValueError("ОШИБКА: Найдены отрицательные значения в весе или длине!")
    
    print("Тест пройден: единицы измерения и диапазоны в норме.")

if __name__ == "__main__":
    generate_html_report()
    test_data_ranges()