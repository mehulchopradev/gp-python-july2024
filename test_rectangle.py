from rectangle import perimeter_rectangle, area_rectangle

class TestRectangle:
  def test_perimeter(self):
    # test data
    length, breadth = 7, 3
    actual = 20

    # action
    expected = perimeter_rectangle(length=length, breadth=breadth)

    # assertions
    assert actual == expected

  def test_area(self):
    length, breadth = 7, 3
    actual = 21

    # action
    expected = area_rectangle(length=length, breadth=breadth)

    # assertions
    assert actual == expected