
# No escribir con caracteres regionales

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

# Los metodos fours, fives, sixes no son estaticos
# Necesitamos un objeto de la clase Yatzy
# Refactorizamos el constructor
# Estructura de datos: una lista, ya que es mutable
# y cada turno consta de 3 tiradas
# Las tuplas no son mutables. Refactorizo los metodos
# anteriores de tupla a lista <= no es necesario:
# ya que son estaticos y no emplean un objeto Yatzy


def test_constructor():
    tirada = Yatzy(1, 1, 1, 1, 1)
    for dado in tirada.dice:
        assert 1 == dado


# La refactorizacion de los metodos fours, fives y sixes
# consiste en simplificar los algoritmos para recorrer
# la tirada de dados y sumar los puntos.

@pytest.fixture
def inyector():
    # es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 4, 5)
    return tirada


def test_fours(inyector):
    ### La suma de todos los CUATROS ###
    valorEsperado = 8
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
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
    '''
    Two pairs:
    If there are two pairs of dice with the same number, the
    player scores the sum of these dice.
    '''
    # La categoria se llama "two pairs": la abstraccion del metodo
    # no es adecuada.
    # Mantengo notacion snake_case
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)


# Three of a kind:
# If there are three dice with the same number, the player
# scores the sum of these dice.
#
# El algoritmo del metodo no es optimo, es complicado e ilegible.

def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)

# Four of a kind:
# If there are four dice with the same number, the player
# scores the sum of these dice.
#
# El algoritmo del metodo no es optimo, es complicado e ilegible.


def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)

# Small straight:
# When placed on "small straight", if the dice read
#   1,2,3,4,5,
# the player scores 15 (the sum of all the dice).
#
# El nombre del metodo no es consistente con la nomenclatura snake_case
# El algoritmo es complicado e ineficiente.


def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.small_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.small_straight(1, 2, 3, 4, 6)


# Large straight:
# When placed on "large straight", if the dice read
#   2,3,4,5,6
# the player scores 20 (the sum of all the dice).
#
# El nombre del metodo no es consistente con la nomenclatura snake_case
# El algoritmo es complicado e ineficiente.

def test_large_straight():
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.large_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.large_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 6)


# Full house:
# If the dice are two of a kind and three of a kind, the
# player scores the sum of all the dice.

def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)
