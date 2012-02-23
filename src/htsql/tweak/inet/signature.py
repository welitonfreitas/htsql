#
# Copyright (c) 2006-2012, Prometheus Research, LLC
# See `LICENSE` for license information, `AUTHORS` for the list of authors.
#


from ...core.tr.fn.signature import AddSig, SubtractSig


class INetIncrementSig(AddSig):
    pass


class INetDecrementSig(SubtractSig):
    pass


class INetDifferenceSig(SubtractSig):
    pass

