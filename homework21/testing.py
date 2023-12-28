import unittest
from time import time, localtime
from task1 import OpenFile


class TestOpenFile(unittest.TestCase):

    # clean up the log file after test method running
    def tearDown(self) -> None:
        with open("opening_logs.txt", "w") as fw:
            print(f"file {fw.name} has been cleaned")

    def test_get_count(self) -> None:
        self.assertEqual(OpenFile.get_count(), 0, "counter must equals 0 before any opening")
        with OpenFile("my_file.txt") as fr:
            print(fr.mode)
            self.assertEqual(OpenFile.get_count(), 1, "counter must equals 1 after opening")
            with OpenFile("my_file.txt") as fr2:
                print(fr2.encoding)
                self.assertEqual(OpenFile.get_count(), 2, "counter must equals 2 after second opening")
            self.assertEqual(OpenFile.get_count(), 1, "counter must equals 1 after first closing")
        self.assertEqual(OpenFile.get_count(), 0, "counter must equals 0 after all closing")

    def test_logging(self) -> None:
        lt = localtime(time())
        t = f"{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday}  {lt.tm_hour}:{lt.tm_min} ---> "
        with OpenFile("my_file.txt") as fr:
            m = fr.mode
        with open("opening_logs.txt") as lg:
            logs = lg.readlines()
            self.assertEqual(logs[0], f"{t} open file 'my_file.txt' with mode '{m}'\n",
                             "log is wrong (line0)")
            self.assertTrue(logs[1].startswith(f"{t} close file 'my_file.txt'. Exception details: "),
                            "log is wrong (line1)")

        lt = localtime(time())
        t = f"{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday}  {lt.tm_hour}:{lt.tm_min} ---> "
        with OpenFile("my_file.txt", "w") as fw:
            m = fw.mode
            fw.write("some text for testing\nHello, beetroot!")
        with open("opening_logs.txt") as lg:
            logs = lg.readlines()
            self.assertEqual(logs[2], f"{t} open file 'my_file.txt' with mode '{m}'\n",
                             "log is wrong (line2)")
            self.assertTrue(logs[3].startswith(f"{t} close file 'my_file.txt'. Exception details: "),
                            "log is wrong (line3)")


if __name__ == "__main__":
    unittest.main()
