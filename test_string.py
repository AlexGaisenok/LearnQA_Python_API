class Test_String:
    def test_string_length(self):
        phrase = input("Enter a phrase: ")
        assert len(phrase)<15, 'Length of a string is more than 15 characters!'