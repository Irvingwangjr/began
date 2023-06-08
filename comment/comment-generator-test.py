import os
import unittest
from comment_generator import traverse_files
class TestTraverseFiles(unittest.TestCase):
    def test_traverse_files(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_dir')
        actual = []
        traverse_files(dir_path)
        for root, dirs, files in os.walk(dir_path):
            level = root.replace(dir_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            actual.extend(os.path.join(root, name) for name in files)
        expected = [
            'test_dir/file1.txt',
            'test_dir/subfolder/file2.py',
            'test_dir/subfolder/file3.pdf'
        ]
        self.assertEqual(expected, actual)

    def test_hidden_folder(self):
        dir_path = os.path.join(os.path.dirname(__file__), 'test_dir_hidden')
        actual = []
        traverse_files(dir_path)
        for root, dirs, files in os.walk(dir_path):
            actual.extend(os.path.join(root, name) for name in files)
        expected = [
            'test_dir_hidden/file1.txt',
            'test_dir_hidden/subfolder/file2.py'
        ]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()