import pytest

from parcel_fee import delivery_fee


@pytest.mark.parametrize(
    "weight_grams, expected_fee",
    [
        (1, 500),
        (999, 500),
        (1000, 500),
        (1001, 1000),
        (20000, 1000),
    ],
)
def test_delivery_fee_returns_correct_amount(weight_grams, expected_fee):
    actual_fee = delivery_fee(weight_grams)

    assert type(actual_fee) is int
    assert actual_fee == expected_fee


@pytest.mark.parametrize("weight_grams", [0, 20001])
def test_delivery_fee_rejects_out_of_range_weights(weight_grams):
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)


@pytest.mark.parametrize("weight_grams", [True, 1000.0, "1000"])
def test_delivery_fee_rejects_invalid_types(weight_grams):
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)