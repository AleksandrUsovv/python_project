import pandas as pd
survey = pd.read_csv('survey_results_public.csv')
hobbyist_counts = survey['Hobbyist'].value_counts()
print(f"Профессиональные программисты: {hobbyist_counts['Yes']}")
print(f"Хобби программисты: {hobbyist_counts['No']}")

# 2.
age_info = survey['Age'].describe()[['mean', 'max', 'min']]
print(f"Средний возраст программистов: {age_info['mean']:.2f}")
print(f"Максимальный возраст программистов: {age_info['max']:.0f}")
print(f"Минимальный возраст программистов: {age_info['min']:.0f}")

# 3.
country_counts = survey['Country'].value_counts().sort_values(ascending=False)
print("Количество программистов по странам:")
print(country_counts)

# 4.
currency_counts = survey['CurrencyDesc'].value_counts().sort_values(ascending=False)
print("Количество программистов по валютам:")
print(currency_counts)