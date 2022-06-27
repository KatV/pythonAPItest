class TestExample:
    def test_check_match(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a + b == expected_sum, f"Some of variables is not equal to {expected_sum}"

    def test_check_match2(self):
        a = 5
        b = 11
        expected_sum = 14
        assert a + b == expected_sum, f"Some of variables is not equal to {expected_sum}"