import pandas as pd
survey = pd.read_csv('survey_results_public.csv')
hobbyist_counts = survey['Hobbyist'].value_counts()
print(f"Профессиональные программисты: {hobbyist_counts['Yes']}")
print(f"Хобби программисты: {hobbyist_counts['No']}")

# 2. Вывод информации о среднем, максимальном и минимальном возрасте программистов
age_info = survey['Age'].describe()[['mean', 'max', 'min']]
print(f"Средний возраст программистов: {age_info['mean']:.2f}")
print(f"Максимальный возраст программистов: {age_info['max']:.0f}")
print(f"Минимальный возраст программистов: {age_info['min']:.0f}")

# 3. Вывод таблицы с количеством программистов по странам в порядке убывания
country_counts = survey['Country'].value_counts().sort_values(ascending=False)
print("Количество программистов по странам:")
print(country_counts)

# 4. Вывод таблицы с количеством программистов по валютам в порядке убывания
currency_counts = survey['CurrencyDesc'].value_counts().sort_values(ascending=False)
print("Количество программистов по валютам:")
print(currency_counts)