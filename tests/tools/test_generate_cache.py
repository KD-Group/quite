import unittest
import quite
import os


class MyTestCase(unittest.TestCase):
    @staticmethod
    def find_format_files(format: str = None) -> list:
        assert isinstance(format, str)
        found_file_name = []
        for root, dir, files in os.walk(os.path.dirname(os.getcwd())):
            for file in files:
                if os.path.splitext(file)[1] == format:
                    found_file_name.append(os.path.splitext(file)[0])
        return found_file_name

    def test_generate_cache(self):
        quite.auto_generate_cache(os.path.dirname(os.getcwd()))
        ui_files = self.find_format_files('.ui')
        cache_files = self.find_format_files('.cache')
        ui_files.sort()
        cache_files.sort()
        self.assertEqual(len(ui_files), len(cache_files))
        for i in range(len(ui_files)):
            self.assertEqual(ui_files[i], cache_files[i])

    def tearDown(self):
        cache_dirs = set()
        for root, dir, files in os.walk(os.path.dirname(__file__)):
            for file in files:
                if os.path.splitext(file)[1] == '.cache':
                    os.remove(os.path.join(root, file))
                    cache_dirs.add(os.path.dirname(os.path.join(root, file)))
        for dir in cache_dirs:
            os.rmdir(dir)
