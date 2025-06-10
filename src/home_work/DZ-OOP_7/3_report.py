class FinancialReport:
    def __init__(self, company_name, revenue, expenses):
        self.company_name = company_name
        self.revenue = revenue
        self.expenses = expenses

    def generate_report(self):
        report = (f"Отчёт компании \"{self.company_name}\" "
                  f"за последний финансовый период:\n")
        report += f"Доходы: {self.revenue} млн рублей\n"
        report += f"Расходы: {self.expenses} млн рублей\n"
        return report

# Класс-декоратор для налоговой инспекции
class TaxAuthorityDecorator:
    def __init__(self, component):
        self.component = component

    def generate_report(self):
        original_report = self.component.generate_report()
        decorated_report = f"{original_report}\n"
        decorated_report += "Представлено в налоговый орган ФНС России.\n"
        decorated_report += "Сведения о налогооблагаемой прибыли прилагаются."
        return decorated_report

# Класс-декоратор для Пенсионного фонда
class PensionFundDecorator:
    def __init__(self, component):
        self.component = component

    def generate_report(self):
        original_report = self.component.generate_report()
        decorated_report = f"{original_report}\n"
        decorated_report += ("Представлено в Пенсионный фонд\nРоссийской "
                             "Федерации.\n")
        decorated_report += "Перечислены страховые взносы сотрудников."
        return decorated_report

# Класс-декоратор для Росстата
class RosstatDecorator:
    def __init__(self, component):
        self.component = component

    def generate_report(self):
        original_report = self.component.generate_report()
        decorated_report = f"{original_report}\n"
        decorated_report += ("Представлено в Федеральную службу \n"
                             "государственной статистики (Росстат).\n")
        decorated_report += "Данные статистического наблюдения приложены."
        return decorated_report

# Главный участок программы
if __name__ == "__main__":
    # Создаём отчёт для компании
    company_report = FinancialReport(company_name="ООО 'Технокомп'",
                                     revenue=500,
                                     expenses=300)

    # Оформляем отчёт для разных ведомств
    print("\nОтчёт для налоговой инспекции:")
    tax_report = TaxAuthorityDecorator(company_report)
    print(tax_report.generate_report())

    print("\nОтчёт для Пенсионного фонда:")
    pension_report = PensionFundDecorator(company_report)
    print(pension_report.generate_report())

    print("\nОтчёт для Росстата:")
    rosstat_report = RosstatDecorator(company_report)
    print(rosstat_report.generate_report())