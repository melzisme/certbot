""" Tests for ParserNode interface """

import unittest

from certbot_apache import interfaces
from certbot_apache import parsernode_util as util


class DummyParserNode(interfaces.ParserNode):
    """ A dummy class implementing ParserNode interface """

    def __init__(self, **kwargs):
        """
        Initializes the ParserNode instance.
        """
        ancestor, dirty, filepath = util.parsernode_kwargs(kwargs)
        self.ancestor = ancestor
        self.dirty = dirty
        self.filepath = filepath
        super(DummyParserNode, self).__init__(**kwargs)

    def save(self, msg):  # pragma: no cover
        """Save"""
        pass


class DummyCommentNode(DummyParserNode):
    """ A dummy class implementing CommentNode interface """

    def __init__(self, **kwargs):
        """
        Initializes the CommentNode instance and sets its instance variables.
        """
        comment, kwargs = util.commentnode_kwargs(kwargs)
        self.comment = comment
        super(DummyCommentNode, self).__init__(**kwargs)


class DummyDirectiveNode(DummyParserNode):
    """ A dummy class implementing DirectiveNode interface """

    # pylint: disable=too-many-arguments
    def __init__(self, **kwargs):
        """
        Initializes the DirectiveNode instance and sets its instance variables.
        """
        name, parameters, enabled, kwargs = util.node_kwargs(kwargs)
        self.name = name
        self.parameters = parameters
        self.enabled = enabled

        super(DummyDirectiveNode, self).__init__(**kwargs)

    def set_parameters(self, parameters):  # pragma: no cover
        """Set parameters"""
        pass


class DummyBlockNode(DummyDirectiveNode):
    """ A dummy class implementing BlockNode interface """

    def add_child_block(self, name, parameters=None, position=None):  # pragma: no cover
        """Add child block"""
        pass

    def add_child_directive(self, name, parameters=None, position=None):  # pragma: no cover
        """Add child directive"""
        pass

    def add_child_comment(self, comment="", position=None):  # pragma: no cover
        """Add child comment"""
        pass

    def find_blocks(self, name, exclude=True):  # pragma: no cover
        """Find blocks"""
        pass

    def find_directives(self, name, exclude=True):  # pragma: no cover
        """Find directives"""
        pass

    def find_comments(self, comment, exact=False):  # pragma: no cover
        """Find comments"""
        pass

    def delete_child(self, child):  # pragma: no cover
        """Delete child"""
        pass

    def unsaved_files(self):  # pragma: no cover
        """Unsaved files"""
        pass


interfaces.CommentNode.register(DummyCommentNode)
interfaces.DirectiveNode.register(DummyDirectiveNode)
interfaces.BlockNode.register(DummyBlockNode)

class ParserNodeTest(unittest.TestCase):
    """Dummy placeholder test case for ParserNode interfaces"""

    def test_dummy(self):
        dummyblock = DummyBlockNode(
            name="None",
            parameters=(),
            ancestor=None,
            dirty=False,
            filepath="/some/random/path"
        )
        dummydirective = DummyDirectiveNode(
            name="Name",
            ancestor=None,
            filepath="/another/path"
        )
        dummycomment = DummyCommentNode(
            comment="Comment",
            ancestor=dummyblock,
            filepath="/some/file"
        )

    def test_unknown_parameter(self):
        params = {
            "comment": "x",
            "ancestor": None,
            "dirty": False,
            "filepath": "/tmp",
            "unknown": "x"
        }
        self.assertRaises(TypeError, DummyCommentNode, **params)
        params["name"] = "unnamed"
        params.pop("comment")
        self.assertRaises(TypeError, DummyDirectiveNode, **params)
        self.assertRaises(TypeError, DummyBlockNode, **params)

    def test_missing_required(self):
        params = {
            "ancestor": None,
            "dirty": False,
            "filepath": "/tmp",
        }
        self.assertRaises(TypeError, DummyCommentNode, **params)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
