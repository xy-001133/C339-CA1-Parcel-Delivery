import pytest

from parcel_acceptance import is_parcel_accepted


@pytest.mark.parametrize(
    "weight_grams, length_cm, expected",
    [
        (1000, 100, True),
        (1, 1, True),
        (20000, 100, True),
        (20001, 100, False),
        (1000, 199, True),
        (1000, 200, True),
        (1000, 201, False),
        (0, 100, False),
        (1000, 0, False),
    ],
)
def test_parcel_acceptance_returns_expected_result(
    weight_grams, length_cm, expected
):
    assert is_parcel_accepted(weight_grams, length_cm) is expected


@pytest.mark.parametrize("weight_grams, length_cm", [(-1, 100), (1000, -1)])
def test_parcel_acceptance_rejects_negative_measurements(weight_grams, length_cm):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)


@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [(True, 100), (1000, True), (1000, 100.0)],
)
def test_parcel_acceptance_rejects_invalid_types(weight_grams, length_cm):
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)