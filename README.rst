quite: QT UI Extension for Python3
==================================

A simple extension for PySide.

I hope it is useful for you, too. :D


====================
Powerful Signal-Slot
====================

.. code-block:: python

    import quite

    signal = quite.SignalSender()
    executed = [False]

    def slot(a: int, b: int, c: int):
        assert a == 1
        assert b == 2
        assert c == 3
        executed[0] = True

    signal.connect(slot)
    signal.emit(1, 2, 3)
    assert executed[0]


============================
User Friendly Widget Classes
============================

.. code-block:: python

    import quite

    w = quite.Widget()
    w.exec()

And you will get that:

.. image:: docs/images/1.simple.widget.png
    :align: center
    :alt: Simple Widget
