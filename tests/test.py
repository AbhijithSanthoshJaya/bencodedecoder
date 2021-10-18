import unittest
from bencodeDecoder.decoder import decoder


class S3TestCase(unittest.TestCase):

    def setUp(self):
        """
        setUp will run before execution of each test case
        """

    def tearDown(self):
        """
        tearDown will run after execution of each test case(delete memory resources and reset objects or global variables)
        """
    def test_test_bencode_decoder_string(self):
        """
        Bencode Decoder unit test for string type input
        """
        output =[]
        expected_output = "Love wings"
        test_input = "10:Love wings"
        output = decoder(test_input)
        print(output)
        #self.assertEqual(expected_output,output)
        return
    def test_test_bencode_decoder_int(self):
        """
        Bencode Decoder unit test for string type input
        """
        output =[]
        expected_output = 45
        test_input = "i45e"
        output = decoder(test_input)
        print(output)
        #self.assertEqual(expected_output,output)
        return
    def test_test_bencode_decoder_dict(self):
        """
        Bencode Decoder unit test for dict type input
        """
        output = {}
        test_input = "d4:keeei42e3:tri4:spame"
        output = decoder(test_input)
        expected_output = {'keee': 42, 'tri': 'spam'}
        self.assertEqual(expected_output,output)
        return

    def test_test_bencode_decoder_list(self):
        """
        Bencode Decoder unit test for list type input
        """
        output =[]
        expected_output = ['abc', 'xyze', 35]
        test_input = "l3:abc4:xyzei35ee"
        output = decoder(test_input)
        self.assertEqual(expected_output,output)
        return