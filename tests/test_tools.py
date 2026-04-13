from lib.tools import assign_angles, assign_offsets


def test_assign_angles():
    """Test."""
    assert assign_angles(1, 0) == [0]
    assert assign_angles(3, -45) == [-45, 0, 45]
    assert assign_angles(5, -15) == [-30, -15, 0, 15, 30]
    assert assign_angles(4, -20) == [-30, -10, 10, 30]


def test_assign_offsets():
    """Test."""
    assert assign_offsets(1, 5) == [0]
    assert assign_offsets(2, 8) == [-32.0, 32.0]
    assert assign_offsets(3, 5) == [-40.0, 0.0, 40.0]
