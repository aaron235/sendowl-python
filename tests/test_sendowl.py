from sendowl_python import SendOwl
import pytest

def test_basic():
	s = SendOwl('this_is_not', 'a_real_set_of_credentials')

	with pytest.raises(RuntimeError, match='Response returned from SendOwl: HTTP Basic: Access denied.'):
		s.get_products()
