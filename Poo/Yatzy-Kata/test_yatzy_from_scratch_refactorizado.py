import pytest
from yatzy import Yatzy


def test_chance():
    ### La suma de todos los dados ###
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)



def test_yatzy():
    #### 50 puntos si son todos los dados iguales ####
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 2, 1)




def test_ones():
    ### La suma de todos los UNOS ###
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)


def test_twos():
    ### La suma de todos los DOSES ###
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)


def test_threes():
    ### La suma de todos los TRESES ###
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)


def test_constructor():
    tirada = Yatzy(1, 1, 1, 1, 1)
    for dado in tirada.dice:
        assert 1 == dado


@pytest.fixture
def inyector():
    # es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 4, 5)
    return tirada


def test_fours(inyector):
    ### La suma de todos los CUATROS ###
    valorEsperado = 8
    assert valorEsperado == inyector.fours()


def test_fives(inyector):
    ### La suma de todos los CINCOS ###
    valorEsperado = 10
    assert valorEsperado == inyector.fives()


def test_sixes(inyector):
    ### La suma de todos los SEISES ###
    valorEsperado = 6
    assert valorEsperado == inyector.sixes()


def test_pair():
    ### Se le ha cambiado el nómbre del método de score_pair a pair, consiste en la suma de una pareja, ####
    #### en caso de dos parejas se le sumará la más alta ####
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)


def test_two_pairs():
    ### Suma dos parejas ###

    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)



def test_three_of_a_kind():
    ### Suma 3 cartas iguales ###
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)



def test_four_of_a_kind():
    ### Suma 4 cartas iguales ###
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)



def test_small_straight():
    ### Si la tirada de los dados es 1,2,3,4,5 signicará escalera pequeña y el jugador obtendrá 15 puntos ###
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.small_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.small_straight(1, 2, 3, 4, 6)




def test_large_straight():
    ### Si la tirada de los dados es 2,3,4,5,6 signicará escalera grande y el jugador obtendrá 20 puntos ###
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.large_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.large_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 6)




def test_full__house():
    ### Si la tirada de los dados es de una pareja y un trío el jugador obtendrá la suma de todos sus dados ###
    assert 8 == Yatzy.full_house(1, 1, 2, 2, 2)
    assert 0 == Yatzy.full_house(2, 2, 3, 3, 4)
    assert 0 == Yatzy.full_house(4, 4, 4, 4, 4)
