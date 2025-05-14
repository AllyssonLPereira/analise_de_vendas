class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class CalculateSales:

    days_week: tuple = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )

    def __init__(self, sales_per_day: dict) -> object:
        self.sales_per_day = sales_per_day

    def __str__(self):
        return f"""
            {bcolors.OKGREEN}Vendas por dia:{bcolors.ENDC} {self.sales_per_day}
            {bcolors.OKGREEN}Total das vendas:{bcolors.ENDC} R$ {self.total:.2f}
            {bcolors.OKGREEN}Média das vendas:{bcolors.ENDC} R$ {self.media:.2f}
            {bcolors.OKGREEN}Menor venda:{bcolors.ENDC} R$ {self.min[1]:.2f} - {self.min[0]}
            {bcolors.OKGREEN}Maior venda:{bcolors.ENDC} R$ {self.max[1]:.2f} - {self.max[0]}
        """

    @classmethod
    def get_infos(cls):
        print("Qual o valor de venda dos seguintes dias:\n")

        try:
            sales_per_day = {
                day: float(input(f"{bcolors.OKBLUE}{day}{bcolors.ENDC}: R$"))
                for day in cls.days_week
            }

        except ValueError:
            raise ValueError("Valor inválido. Por favor, digite um número.")

        for value in sales_per_day.values():
            if not value:
                raise ValueError(
                    f"{bcolors.WARNING}Você esqueceu de especificar o valor de algum dia!{bcolors.ENDC}"
                )

        return cls(sales_per_day)

    @property
    def total(self):
        self._total = sum(self.sales_per_day.values())

        if not self._total:
            raise ValueError(
                f"{bcolors.WARNING}Você não especificou o valores!{bcolors.ENDC}"
            )

        if not isinstance(self._total, float):
            raise TypeError(
                f"{bcolors.WARNING}Os valores inseridos são inválido!{bcolors.ENDC}"
            )

        return self._total

    @property
    def media(self):
        self._media = sum(self.sales_per_day.values()) / len(self.sales_per_day)

        if not self._total:
            raise ValueError(
                f"{bcolors.WARNING}Você não especificou o valores!{bcolors.ENDC}"
            )

        if not isinstance(self._total, float):
            raise TypeError(
                f"{bcolors.WARNING}Os valores inseridos são inválido!{bcolors.ENDC}"
            )

        return self._media

    @property
    def min(self):
        return min(self.sales_per_day.items(), key=lambda item: item[1])

    @property
    def max(self):
        return max(self.sales_per_day.items(), key=lambda item: item[1])


if __name__ == "__main__":
    result = CalculateSales.get_infos()

    print(result)
