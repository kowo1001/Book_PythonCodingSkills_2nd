# environment_test.py

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main

class EnvironmentTest(TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_modify_file(self):
        with open(self.test_path / 'data.bin', 'w') as f:
            ...

if __name__ == '__main__':
    main()


# integration_test.py
from unittest import TestCase, main

def setUpModule():
    print('* 모듈 설정')

def tearDownModule():
    print('* 모듈 정리')

class IntegrationTest(TestCase):
    def setUp(self):
        print('* 테스트 설정')

    def tearDown(self):
        print('* 테스트 정리')
    
    def test_end_to_end1(self):
        print('* 테스트 1')

    def test_end_to_end2(self):
        print('* 테스트 2')

if __name__ == '__main__':
    main()