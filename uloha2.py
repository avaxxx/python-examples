import math

def largest_triple(max_side):
    max_sum = 0

    # pole tuples to su dve hodnoty (1,1), (1,2)
    list_of_tuples = []
    # dvoma for cyklami si naplnime pole vsetkzmi kombinaciami
    for a in range (1, max_side):
        for b in range(1, max_side):
             c = math.sqrt( a * a + b * b)
             if c % 1 == 0:
                sum = a + b + int(c)
                if (sum > max_sum):
                    max_sum = sum
    return max_sum
    # # prejdeme si pole
    # for t in list_of_tuples:
    #     # ulozime hodnoty v tuple do premennych a, b
    #     a,b = t
    #     # vyratame odmocninu z c a ak je to cele cislo tak vyratame sumu, pokial je suma vacsia ako 
    #     # maximum co sme si definovali hore, ulozime do premennej max_sum tuto hodnotu
    #     c = math.sqrt( a * a + b * b)
    #     if c % 1 == 0:
    #         sum = a + b + int(c)
    #         if (sum > max_sum):
    #             max_sum = sum



def main():
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    assert largest_triple(150) == 490
    assert largest_triple(1000) == 3290

if __name__ == "__main__":
    main()
