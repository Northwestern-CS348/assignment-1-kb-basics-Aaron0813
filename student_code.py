import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        is_existed = False
        if fact.name == "fact":
            for f in self.facts:
                if f == fact:
                    is_existed = True
                    print("Existing Facts")
                    break
            if not is_existed:
                self.facts.append(fact)
        elif fact.name == "rule":
            print("This is a rule")
        else:
            print("Not support")
        # print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        list_of_bindings = ListOfBindings()
        is_false_existed = False
        for f in self.facts:
            res = match(f.statement, fact.statement)
            if (not is_false_existed) and (not res):
                is_false_existed = True
            elif res != False:
                list_of_bindings.add_bindings(res)

        if is_false_existed and len(list_of_bindings) == 0:
            return False
        return list_of_bindings
        # print("Asking {!r}".format(fact))
