import datetime
from hieroglyphs import HIEROGLYPHS_SET


def time_hieroglyphs(hours: int, minutes: int) -> list:
    hieroglyphs = HIEROGLYPHS_SET[hours]
    return hieroglyphs

if __name__ == "__main__":
   print(time_hieroglyphs(1, 0))
   print(time_hieroglyphs(2, 0))

