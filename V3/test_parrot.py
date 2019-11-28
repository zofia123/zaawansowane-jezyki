from parrot import EuropeanParrot, AfricanParrot, NorwegianParrot


def test_speed_of_european_parrot():
    parrot = EuropeanParrot()
    assert parrot.speed() == 12.0


def test_speed_of_african_parrot_with_one_coconut():
    parrot = AfricanParrot(1)
    assert parrot.speed() == 3.0


def test_speed_of_african_parrot_with_two_coconuts():
    parrot = AfricanParrot(2)
    assert parrot.speed() == 0


def test_speed_of_african_parrot_with_no_coconuts():
    parrot = AfricanParrot(0)
    assert parrot.speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed():
    parrot = NorwegianParrot(1.5, True)
    assert parrot.speed() == 0.0


def test_speed_norwegian_parrot_with_one_volt():
    parrot = NorwegianParrot(1, False)
    assert parrot.speed() == 12


def test_speed_norwegian_blue_parrot_not_nailed():
    parrot = NorwegianParrot(1.5, False)
    assert parrot.speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage():
    parrot = NorwegianParrot(4, False)
    assert parrot.speed() == 24.0


def test_speed_norwegian_parrot_with_no_volt():
    parrot = NorwegianParrot(0, False)
    assert parrot.speed() == 0
