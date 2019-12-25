import os

import pytest
import yaml

def get_hehe():
    num_list = []
    with open("./data"+os.sep+"sum.yaml","r",encoding="utf-8")as f:
        data = yaml.safe_load(f)
        for i in  data.values():
            num_list.append(tuple(i.values()))

        return num_list




class Test_add():
    @pytest.mark.parametrize("a,b,c",get_hehe())
    def test_hah(self,a,b,c):

        assert a+b == c

if __name__ == '__main__':
    pytest.main(["test_add.py"])