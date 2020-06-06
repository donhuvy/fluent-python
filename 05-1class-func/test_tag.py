from tag import tag

import pytest

def test_tag():
    # A single positional argument produces an empty tag with that name
    assert tag('br') == '<br />'
    
    # Any number of arguments after the first are captured by *content as a tuple
    assert tag('p', 'hello') == '<p>hello</p>'
    assert tag('p', 'hello', 'world') == '<p>hello</p>\n<p>world</p>'

    # Keyword arguments not eplicitly named (e.g., id) in the tag signature are captured by **attrs
    # as a dict
    assert tag('p', 'hello', id=33) == '<p id="33">hello</p>'
    
    # The cls parameter can only be passed as a keyword argument, it will never capture unnamed
    # positional arguments
    assert tag('p', 'hello', 'world', cls='sidebar') == \
        '<p class="sidebar">hello</p>\n<p class="sidebar">world</p>'
    
    # Even the first positional argument can be passed as a keyword argument    
    assert tag(content='testing', name="img") == '<img content="testing" />'
    
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    # Prefixing the my_tag dict with ** passes all its items as separate arguments, which are then
    # bound to the named parameters. which the remaining caught by **attrs
    assert tag(**my_tag) == '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'

if __name__ == "__main__":
    pytest.main()
